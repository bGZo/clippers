---
title: "对虚拟机（JVM）了解不足"
created: 2025-04-05T18:02:30
modified: 2025-04-05T18:02:30
source: https://program-think.blogspot.com/2009/05/defect-of-java-beginner-5-jvm.html
tags:
tags-link:
type: archive-web
---
#jvm

关于基本类型和引用类型

关于垃圾回收（Garbage Collection）

GC 是如何判断哪些对象已经失效？

GC 对性能会有哪些影响？

如何通过 JVM 的参数调优 GC 的性能？

关于字符串

对于 Java 提供的 String 和 StringBuilder，想必很多人都知道：String 用于常量字符串，StringBuilder 用于可变字符串。那 Java 当初为什么要这样设计捏？为啥不用一个类来统一搞定捏？

关于范型（Generic Programming）

GP 是在编译时实现的还是在运行时实现的？为什么要这么实现？

GP 的类型擦除机制是咋回事？有啥优点/缺点？

使用范型容器（相对于传统容器）在性能上有啥影响？为什么？

关于多线程

synchronized 关键字是怎么起作用滴？

synchronized 的颗粒度（或者说作用域）如何？是针对某个类还是针对某个类对象实例？

synchronized 对性能有没有影响？为什么？

volatile 关键字又是派啥用滴？啥时候需要用这个关键字捏？