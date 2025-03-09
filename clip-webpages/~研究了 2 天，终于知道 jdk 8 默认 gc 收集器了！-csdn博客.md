---
created: 2024-05-25T12:00:00
source: https://blog.csdn.net/youanyyou/article/details/106464291
type: archive-web
modified: 2025-01-15T11:39:54
---

> JDK 8 到底默认用的是哪款 GC 收集器？

为啥是 JDK8？不是 9 也不是 10？因为 JDK8 还是市场占有率最高的，所以针对这个版本我做了深入的探索。

《深入理解 Java 虚拟机》第三版第 128 页中提到 JDK 9 之前，Server 默认使用 Parallel Scavenge + Serial Old(PS MarkSweep)，那么真的是这样的吗？ 我带着这个疑问做了如下验证

1. 直接使用命令查看一下当前 JVM 默认参数

```
  java -XX:+PrintCommandLineFlags -version
  ```

输入内容如下

```
  -XX:InitialHeapSize=268435456 
  -XX:MaxHeapSize=4294967296 
  -XX:+PrintCommandLineFlags 
  -XX:+UseCompressedClassPointers 
  -XX:+UseCompressedOops 
  -XX:+UseParallelGC
  java version "1.8.0_162"
  Java(TM) SE Runtime Environment (build 1.8.0_162-b12)
  Java HotSpot(TM) 64-Bit Server VM (build 25.162-b12, mixed mode)
  ```

第 6 行我们可以看到使用的是 `-XX:+UseParallelGC` 按照书中或者是网上的文章发现，设置这个参数以后默认就是如下两个组合，新生代用 `Parallel Scavenge` 老年代用 `Serial Old`

```
  Parallel Scavenge + Serial Old
  ```

那么这里再详细科普一下，下面是每个参数对应的回收器的类型

![](assets/2024/x-oss-process=image.png)

将信将疑的我再次开启探索之旅，这时候我使用 `ManagementFactory.getGarbageCollectorMXBeans()` 把具体的回收器打印出来看下不就可以了吗？详细代码如下

```
  import java.lang.management.GarbageCollectorMXBean;
  import java.lang.management.ManagementFactory;
  import java.util.List;
  public class GcCollectorPrinter {
      public static void main(String[] args) {
          List<GarbageCollectorMXBean> beans = ManagementFactory.getGarbageCollectorMXBeans();
          for (GarbageCollectorMXBean bean : beans) {
              System.out.println(bean.getName());
          }
      }
  }
  ```

直接运行输出内容如下

```
  PS Scavenge
  PS MarkSweep
  ```

这意思是 `PS MarkSweep` 是 `Serial Old` 的意思对吗？那么 `-XX:+UseParallelOldGC` 打印出来的结果又是什么呢？我配置好参数再次运行如下两个命令

```
  javac GcCollectorPrinter.java 
  java -XX:+UseParallelOldGC GcCollectorPrinter
  ```

如下是打印结果

```
  PS Scavenge
  PS MarkSweep
  ```

等等，我更加疑惑了？`-XX:+UseParallelOldGC` 和 `-XX:+UseParallelGC` 的输出结果都是 `PS MarkSweep`，那么他究竟是 `Serial Old` 还是 `Parallel Old`？

  这时候我有两个猜想

1. `PS MarkSweep` 只是回收器的别名，他可以指代 `Serial Old` 和 `Parallel Old`，毕竟他们的实现基本一样。

  2. `-XX:+UseParallelGC` 和 `-XX:+UseParallelOldGC` 结果一样，都是用的 `Parallel Old`

好的那么接下来开启 GC 之旅，这个 " 别名 " 一样没办法了，我直接打印一下 GC 的日志，看下日志里面显示什么，`-XX:+PrintGCDetails` 这个参数就上场了，他可以输出 GC 详细的分区分析，我们再次运行刚才的两个例子如下

```
  java -XX:+UseParallelOldGC -XX:+PrintGCDetails GcCollectorPrinter
  java -XX:+PrintGCDetails GcCollectorPrinter
  
  ```

结果惊人的一致

```
  PS Scavenge
  PS MarkSweep
  Heap
   PSYoungGen      total 76288K, used 3932K [0x000000076ab00000, 0x0000000770000000, 0x00000007c0000000)
    eden space 65536K, 6% used [0x000000076ab00000,0x000000076aed7240,0x000000076eb00000)
    from space 10752K, 0% used [0x000000076f580000,0x000000076f580000,0x0000000770000000)
    to   space 10752K, 0% used [0x000000076eb00000,0x000000076eb00000,0x000000076f580000)
   ParOldGen       total 175104K, used 0K [0x00000006c0000000, 0x00000006cab00000, 0x000000076ab00000)
    object space 175104K, 0% used [0x00000006c0000000,0x00000006c0000000,0x00000006cab00000)
   Metaspace       used 2729K, capacity 4486K, committed 4864K, reserved 1056768K
    class space    used 297K, capacity 386K, committed 512K, reserved 1048576K
   
  ```

可以看到 老年代都是用的 `ParOldGen` 那么一点可以断定了，`-XX:+UseParallelGC` 和 `-XX:+UseParallelOldGC` 结果一样，都是用的 `Parallel Old`。

那么我们继续验证第二个疑问，`PS MarkSweep` 只是回收器的别名，他可以指代 `Serial Old` 和 `Parallel Old`，可以直接使用如下命令验证，我用的不是 `+` 而是 `-`，这样就一定强制去掉了 `Parallel Old` 收集器，我们看下效果

```
      java -XX:-UseParallelOldGC -XX:+PrintGCDetails GcCollectorPrinter
       
  
      PS Scavenge
      PS MarkSweep
      Heap
       PSYoungGen      total 76288K, used 3932K [0x000000076ab00000, 0x0000000770000000, 0x00000007c0000000)
        eden space 65536K, 6% used [0x000000076ab00000,0x000000076aed7240,0x000000076eb00000)
        from space 10752K, 0% used [0x000000076f580000,0x000000076f580000,0x0000000770000000)
        to   space 10752K, 0% used [0x000000076eb00000,0x000000076eb00000,0x000000076f580000)
       PSOldGen        total 175104K, used 0K [0x00000006c0000000, 0x00000006cab00000, 0x000000076ab00000)
        object space 175104K, 0% used [0x00000006c0000000,0x00000006c0000000,0x00000006cab00000)
       Metaspace       used 2728K, capacity 4486K, committed 4864K, reserved 1056768K
        class space    used 297K, capacity 386K, committed 512K, reserved 1048576K
       
  ```

唯一的变化就是 `ParOldGen` 换成了 `PSOldGen`，经过查询我们可以确定 `PSOldGen` 就是 `Serial Old` 所以终于有了答案。

1. `PS MarkSweep` 只是回收器的别名，他可以指代 `Serial Old` 和 `Parallel Old`。

  2. `-XX:+UseParallelGC` 和 `-XX:+UseParallelOldGC` 结果一样，都是用的 `Parallel Old`

那书上说的还能有假？保险起见还是去找一些资料吧

在 JDK 8 的官网找到了一些蛛丝马迹

  链接：https://urlify.cn/67NnEz

```
  Parallel compaction is enabled by default if the option -XX:+UseParallelGC has been specified. The option to turn it off is -XX:-UseParallelOldGC.
  ```

大致意思就是说 `-XX:+UseParallelGC` 就会开始 `Parallel` 收集器除非手动关闭，那么可是书上为什么说是 `Serial` 呢？

终于我在 JDK 源码 commit 记录里面找到了答案，在 JDK 7U4 之前确实 `UserParallelGC` 用的就是 `Serial`，在这个版本之后 `Parallel` 已经很成熟了，所以直接替换了旧的收集器，所以 JDK 7u4 以后的 7 和 JDK 8 老年代默认使用的都是 `Parallel` 收集器，只是书中没有更新这个细节。

  网址：

  https://bugs.openjdk.java.net/browse/JDK-6679764

  http://hg.openjdk.java.net/jdk8u/jdk8u/hotspot/rev/24cae3e4cbaa

  原文：

```
  Server-class machine ergonomics was introduced in jdk5. If the machine upon which
  the jvm is running is powerful enough (currently, at least 2 physical cores plus
  at least 2gb of memory), the server jvm is invoked using the parallel scavenger
  rather than the serial scavenger. Currently the old gen collector used is
  serial mark-sweep-compact. Now that the parallel old gen collector is mature,
  we should change to using it instead.
  Issue Links
  
  ```

觉得不错，欢迎在看、转发哟～
