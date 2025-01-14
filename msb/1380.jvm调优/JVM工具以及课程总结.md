# JVM工具以及课程总结         55分我上麦         讲师：严镇涛

## **性能监控工具**

### jconsole

**JConsole工具是JDK自带的图形化性能监控工具。并通过JConsole工具， 可以查看Java应用程序的运行概况， 监控堆信息、 元空间使用情况及类的加载情况等。**

JConsole程序在%JAVA_HOM E%/bin目录下

或者你可以直接在命令行对他进行打印

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/12597031b6e44327b0c12ac06244244a.png)

会显示如下界面：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/889f8f9b80354e588892b3eb3ae87c1c.png)

#### JConsole的连接方式

JConsole分为本地连接以及远程连接，一般我们本地连接在小型单体项目中用于本地分析较多，大型项目以及线上生产环境一般采用远程连接的方式。

##### 本地连接：

Jconsole会在本地自动寻找当前的可监控进程，所以我们可以只要本地启动项目，就可以自动匹配并点击进去。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/242f9982bf274d099b25df1c28963b90.png)

##### 远程连接：

1. 设置被监控的Java虚拟机启动的參数，一般的情况下，会有下面三个參数，各自是：

-Dcom.sun.management.jmxremote.port=1090

-Dcom.sun.management.jmxremote.ssl=false

-Dcom.sun.management.jmxremote.authenticate=false

也就是说，你需要在启动参数后面加上这几个参数

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/1c16f91a0f1246778332e8f590974262.png)

被监控的虚拟机启动以后，我们就能够其他电脑上通Jconsole进行远程连接。

连接的过程例如以下：

1.打开cmd，输入jconsole，就会出现jconsole控制台，

然后，我们输入要被监控的Java虚拟机的IP地址和port号，如果输入正确，连接button就上生效如果设计的监控port号为8082，连接的IP为：10.20.618.11（这个需要你防火墙以及端口都处于开放状态），例如以下图所看到的：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/b2f94d65785a4acfbc85d5535889fbab.png)

点击连接后，就会进入到正常的显示界面，说明就连接成功了。

#### JConsole的显示界面：

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/4f1e3fa6d8994f3892000fc84208b20f.png)

**概述** ：记录了“堆内存使用情况”、“线程”、“类”、“CPU使用情况”共四个资源的实时情况；

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/efb1b06e892f4a229ba574aad14fb713.png)

并且在时间范围可以选择从1分钟到1年的显示情况

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/1b9494333e5b49b5bc39053c1b3aab5a.png)

**内存**  ：可以选择查看“堆内存使用情况”、“非堆内存使用情况”、“内存池"PS Eden Space"”等内存占用的实时情况；界面右下角还有图形化的堆一级、二级、三级缓存（从左到右）占用情况，当然，如果三级缓存被全部占用也就是很可能内存溢出啦！这时可以去查看服务器的tomcat日志，应该会有“outofmemory"的异常日志信息。界面右上角处还提供了一个“执行GC”的手动垃圾收集功能，这个也很实用~而且界面下方还有详细的GC信息记录。，整个界面提供了关于垃圾收集必须的各项基础指标查询。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/059844d8479d4b6895ddad61ac6bd895.png)

**线程** ：界面上部显示实时线程数目。下部还能查看到详细的每个进程及相应状态、等待、堆栈追踪等信息；

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/45c682b9d11e45418add74b5f1142b7c.png)

并且在右下角，我们还可以检测死锁的情况。如果当前线程没有出现死锁，那么会显示未出现死锁。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/73785f956bf447cf858f15255fd211a7.png)

但是如果出现了死锁，这里也会进行相应的检测。会直接显示死锁的页面，并且我们可以通过点击对应的线程来查看死锁的信息。

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/b6d4ddf4763f473b9e7416ad225677e6.png)

**类** ：显示“已装入类的数目”、“已卸载类的数目”信息；

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/ae89012cdda545aa884e405d3e68cee2.png)

**VM摘要** ：显示服务器详细资源信息，包括：线程、类、OS、内存等；

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/8e41461bfa03410cb3ad8efedfd66bfc.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/18602db0ff9741ad8d4719359c8feaff.png)

**MBean** : 可在此页进行参数的配置。

*MBean就是被JMX管理的资源。* 一般有两种类型的MBean,标准的和动态的。 标准类型的MBean最简单,它能管理的资源(包括属性,方法,时间)必须定义在接口中,然后MBean必须实现这个接口。它的命名也必须遵循一定的规范,例如我们的MBean为User,则接口必须为UserMBean。 动态MBean必须实现javax.management.DynamicMBean接口,所有的属性,方法都在运行时定义。

这个一般情况下互联网交互式企业级开发用到的可能性没有那么高。因为现在JMX架构用得没那么多。

#### 测试垃圾回收案例：

```java
package com.example.jvmcase.test;


import com.google.common.collect.Lists;

import java.util.ArrayList;

public class JconsoleTest1 {
    //将bytes设置为全局变量
    public byte[] bytes = new byte[1024*1024];
    //测试内存的变化情况
    public static void main(String[] args) {
        try {
            Thread.sleep(3000);//为了能看到效果
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("开始..");
        fillHeap(1000);
    }

    public static void fillHeap(int count){
        ArrayList<JconsoleTest1> jts = Lists.newArrayList();

        for(int i=0;i<count;i++){
            try {
                //这里睡3S，出效果
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            jts.add(new JconsoleTest1());
        }
    }
}


```

监控JVM内存情况，发现持续不回收，内存持续上升。

接下来，将bytes放进构造函数中，变成局部变量。如果没有使用的情况下，垃圾回收器是会光顾。现在再去看内存情况，发现内存在垃圾回收时候会形成波峰。

```java
 public  JconsoleTest2(){
        //将bytes设置为局部变量
        byte[] bytes = new byte[1024 * 1024];
    }
```

### jvisualvm

官网：https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jvisualvm.html

官方描述：

> ```
> Description
> Java VisualVM is an intuitive graphical user interface that provides detailed information about Java technology-based applications (Java applications) while they are running on a specified Java Virtual Machine (JVM). The name Java VisualVM comes from the fact that Java VisualVM provides information about the JVM software visually.
>
> Java VisualVM combines several monitoring, troubleshooting, and profiling utilities into a single tool. For example, most of the functionality offered by the standalone tools jmap, jinfo, jstat, and jstack were integrated into Java VisualVM. Other functionality, such as some that offered by the jconsole command, can be added as optional plug-ins.
>
> Java VisualVM is useful to Java application developers to troubleshoot applications and to monitor and improve the applications' performance. Java VisualVM enables developers to generate and analyze heap dumps, track down memory leaks, perform and monitor garbage collection, and perform lightweight memory and CPU profiling. You can expand the Java VisualVM functionality with plug-ins. For example, most of the functionality of the jconsole command is available through the MBeans Tab and JConsole Plug-in Wrapper plug-ins. You can choose from a catalog of standard Java VisualVM plug-ins by selecting Tools and then Plugins in the Java VisualVM menus.
>
> Start Java VisualVM with the following command:
>
> %  jvisualvm <options>
> ```

**大致意思：**

Java VisualVM 是一个直观的图形用户界面，可在基于 Java 技术的应用程序（Java 应用程序）在指定的 Java 虚拟机 (JVM) 上运行时提供有关它们的详细信息。

Java VisualVM 将多个监控、故障排除和分析实用程序组合到一个工具中。例如，独立工具jmap、jinfo和提供jstat,的大部分功能jstack都集成到 Java VisualVM 中。其他功能，例如jconsole命令提供的一些功能，可以作为可选插件添加。

Java VisualVM 对于 Java 应用程序开发人员对应用程序进行故障排除以及监控和改进应用程序的性能非常有用。Java VisualVM 使开发人员能够生成和分析堆转储、跟踪内存泄漏、执行和监视垃圾收集以及执行轻量级内存和 CPU 分析。

使用以下命令启动 Java VisualVM：

% jvisualvm &#x3c;选项>

#### 监控本地Java进程

可以监控本地的java进程的CPU，类，线程等

#### 监控远端Java进程

（1）在visualvm中选中“远程”，右击“添加”

（2）主机名上写服务器的ip地址，比如39.100.39.63，然后点击“确定”

（3）右击该主机"39.100.39.63"，添加“JMX”，也就是通过JMX技术具体监控远端服务器哪个Java进程

（4）要想让服务器上的tomcat被连接，需要改一下Catalina.sh这个文件

> **注意下面的8998不要和服务器上其他端口冲突**

```shell
JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote -
Djava.rmi.server.hostname=39.100.39.63 -Dcom.sun.management.jmxremote.port=8998
-Dcom.sun.management.jmxremote.ssl=false -
Dcom.sun.management.jmxremote.authenticate=true -
Dcom.sun.management.jmxremote.access.file=../conf/jmxremote.access -
Dcom.sun.management.jmxremote.password.file=../conf/jmxremote.password"
```

（5）在../conf文件中添加两个文件jmxremote.access和jmxremote.password

**jmxremote.access**

```
guest readonly
manager readwrite
```

**jmxremote.password**

```
guest guest
manager manager
```

授予权限：chmod 600 *jmxremot*

（6）将连接服务器地址改为公网ip地址

```shell
hostname -i   查看输出情况
	172.26.225.240 172.17.0.1
vim /etc/hosts
	172.26.255.240 39.100.39.63
```

（7）设置上述端口对应的阿里云安全策略和防火墙策略

（8）启动tomcat，来到bin目录

```
./startup.sh
```

（9）查看tomcat启动日志以及端口监听

```
tail -f ../logs/catalina.out
lsof -i tcp:8080
```

（10）查看8998监听情况，可以发现多开了几个端口

```shell
lsof -i:8998    得到PID
netstat -antup | grep PID
```

（11）在刚才的JMX中输入8998端口，并且输入用户名和密码则登录成功

```
端口:8998
用户名:manager
密码:manager
```

### arthas

> `github`：https://github.com/alibaba/arthas
>
> ```
> Arthas allows developers to troubleshoot production issues for Java
> applications without modifying code or restarting servers.
> ```
>
> Arthas 是Alibaba开源的Java诊断工具，采用命令行交互模式，是排查jvm相关问题的利器。

#### 3.3.3.1 下载安装

```shell
curl -O https://alibaba.github.io/arthas/arthas-boot.jar
java -jar arthas-boot.jar
or 
java -jar arthas-boot.jar -h
# 然后可以选择一个Java进程
```

#### 3.3.3.2 常用命令

> 具体每个命令怎么使用，大家可以自己查阅资料

```
version:查看arthas版本号
help:查看命名帮助信息
cls:清空屏幕
session:查看当前会话信息
quit:退出arthas客户端
---
dashboard:当前进程的实时数据面板
thread:当前JVM的线程堆栈信息
jvm:查看当前JVM的信息
sysprop:查看JVM的系统属性
---
sc:查看JVM已经加载的类信息
dump:dump已经加载类的byte code到特定目录
jad:反编译指定已加载类的源码
---
monitor:方法执行监控
watch:方法执行数据观测
trace:方法内部调用路径，并输出方法路径上的每个节点上耗时
stack:输出当前方法被调用的调用路径
......
```

## 内存分析工具

### MAT（Memory Analyzer Tool）

MAT是一款非常强大的内存分析工具，在Eclipse中有相应的插件，同时也有单独的安装包。在进行内存分析时，只要获得了反映当前设备内存映像的hprof文件，通过MAT打开就可以直观地看到当前的内存信息。一般说来，这些内存信息包含：

* 所有的对象信息，包括对象实例、成员变量、存储于栈中的基本类型值和存储于堆中的其他对象的引用值。
* 所有的类信息，包括classloader、类名称、父类、静态变量等
* GCRoot到所有的这些对象的引用路径
* 线程信息，包括线程的调用栈及此线程的线程局部变量（TLS）

那么接下来  我们可以尝试去分析一下内存泄漏场景：

```java
package com.example.jvmcase.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;

@RestController
public class TLController {
    @GetMapping(value = "/tl")
    public String tl(HttpServletRequest request) {
        ThreadLocal<Byte[]> tl = new ThreadLocal<Byte[]>();
        tl.set(new Byte[1024 * 1024]);
        return "ok";
    }
}
```

在这个代码中，很明显我们的代码没有去进行remove，所以会造成内存泄漏。而内存泄漏的堆积会导致内存溢出。所以我考虑用这个场景进行分析。

项目启动参数

```shell
-Xms100M -Xmx100M -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=jvm.hprof 
```

这个时候hprof文件导出，一般生产环境中，我们的要考虑远程导出可能会导致系统卡断或者直接宕机。或者dump出的文件特别大，这个时候需要设置内存。

需要在mat目录下的MemoryAnalyzer.ini文件种改一下配置，最大占用内存设大一点，Xmx参数

```java
 -Xmx10240M            这个数字根据你文件大小设置
```

设置后重启生效

手动转储

```java
jmap -histo:live PID | more
获取到jvm.hprof文件，上传到指定的工具分析，比如MAT
```

### heaphero

[https://heaphero.io/](https://heaphero.io/)

### perfma

笨马是一个JVM调优工具，甚至会给你相应的JVM调优建议，但是他是一个收费工具，不过如果你仅仅是希望调优参数，可以使用试用版。但是他的调优建议都是简单的参数设置。

[https://console.perfma.com/](https://console.perfma.com/)

## 日志分析工具

> 要想分析日志的信息，得先拿到GC日志文件才行，所以得先配置一下，根据前面参数的学习，下面的配置很容易看懂。比如打开windows中的catalina.bat，在第一行加上

```
XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintGCDateStamps 
-Xloggc:$CATALINA_HOME/logs/gc.log
```

#### 不同收集器日志

这样使用startup.bat启动tomcat的时候就能够在当前目录下拿到gc.log文件，可以看到默认使用的是ParallelGC。

（1）Parallel GC

> 【吞吐量优先】
>
> ```
> 2019-06-10T23:21:53.305+0800: 1.303: [GC (Allocation Failure) [PSYoungGen: 65536K[Young区回收前]->10748K[Young区回收后](76288K[Young区总大小])] 65536K[整个堆回收前]->15039K[整个堆回收后](251392K[整个堆总大小]), 0.0113277 secs] [Times: user=0.00 sys=0.00, real=0.01 secs] 
> ```
>
>> `注意`如果回收的差值中间有出入，说明这部分空间是Old区释放出来的
>>

![](images/54.png)

（2）CMS

> 【停顿时间优先】
>
> ```
> 参数设置：-XX:+UseConcMarkSweepGC -Xloggc:cms-gc.log
> ```

重启tomcat获取gc日志，这里的日志格式和上面差不多，不作分析。

（3）G1

G1日志格式参考链接：https://blogs.oracle.com/poonam/understanding-g1-gc-logs

> 【停顿时间优先】
>
> ```
> 参数设置：-XX:+UseG1GC -Xloggc:g1-gc.log
> ```
>
> ```shell
> -XX:+UseG1GC  # 使用了G1垃圾收集器
>
> # 什么时候发生的GC，相对的时间刻，GC发生的区域young，总共花费的时间，0.00478s，
> # It is a stop-the-world activity and all
> # the application threads are stopped at a safepoint during this time.
> 2019-12-18T16:06:46.508+0800: 0.458: [GC pause (G1 Evacuation Pause)
> (young), 0.0047804 secs]
>
> # 多少个垃圾回收线程，并行的时间
> [Parallel Time: 3.0 ms, GC Workers: 4]
>
> # GC线程开始相对于上面的0.458的时间刻
> [GC Worker Start (ms): Min: 458.5, Avg: 458.5, Max: 458.5, Diff: 0.0]
>
> # This gives us the time spent by each worker thread scanning the roots
> # (globals, registers, thread stacks and VM data structures).
> [Ext Root Scanning (ms): Min: 0.2, Avg: 0.4, Max: 0.7, Diff: 0.5, Sum: 1.7]
>
> # Update RS gives us the time each thread spent in updating the Remembered
> Sets.
> [Update RS (ms): Min: 0.0, Avg: 0.0, Max: 0.0, Diff: 0.0, Sum: 0.0]
> ...
>
> # 主要是Eden区变大了，进行了调整
> [Eden: 14.0M(14.0M)->0.0B(16.0M) Survivors: 0.0B->2048.0K Heap:
> 14.0M(256.0M)->3752.5K(256.0M)]
> ```

![](images/55.png)![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/1a36df96b353454c9d27722b7d87fdc4.png)

### GCViewer

java -jar gcviewer-1.36-SNAPSHOT.jar

![](images/56.png)![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/be199bbcb4534c08aa852db802f4d9bf.png)

### gceasy

http://gceasy.io

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/2d2e103191594bedacae1ddbcfc84976.png)

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/1b2f0255426a40009c8deaa1f72d3dfa.png)

### gcplot

https://it.gcplot.com/

这个是young区的信息

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1463/1656048868088/16e2219fe38d4735b718db1c12a54025.png)




课程章节总结：

1.JVM之走进类加载

你了解类加载嘛

装载     链接  初始化

类加载器    双亲委派    三大特性 以及打破双亲委派    SPI

2.JVM之深入运行时数据区

栈帧    要把运行时数据区跟其他知识结合起来

3.对象的内存布局

指针压缩问题：

4.内存模型以及对象已死问题

面试问到对象生命周期即可          第三方的图片缓存     图片缓存导致内存泄漏

5.垃圾回收算法

动态分配规则          常规的三大垃圾回收算法     整理算法      分代回收三大假说

6.垃圾收集器浅析

常用参数    以及常规的垃圾收集器

7.CMS垃圾收集器

* CMS的两种模式与一种特殊策略
* 可中止的预处理
* 三色标记
* CMS的参数调优

8.G1垃圾收集器

Rset三大数据类型

G1特性

G1参数

9.G1垃圾收集器（下）

三大回收流程

10.ZGC深入解析

ZGC三大核心技术

ZGC垃圾回收触发时机

11.JVM命令以及执行引擎

JVM的分层编译5大级别：

code  cache

12.JVM的性能优化

案例优化   你要找到一个高并发的案例

13.JVM常见工具使用

监控工具

内存分析

日志分析
