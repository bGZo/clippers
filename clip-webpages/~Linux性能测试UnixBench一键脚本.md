---
title: "Linux性能测试UnixBench一键脚本  |  秋水逸冰"
aliases: "Linux性能测试UnixBench一键脚本  |  秋水逸冰"
created: 2025-04-05T17:35:33
modified: 2025-04-05T17:35:33
description: "UnixBench是一个类unix系（Unix，BSD，Linux）统下的性能测试工具，一个开源工具，被广泛用与测试linux系统主机的性能。Unixbench的主要测试项目有：系统调用、读写、进程、图形化测试、2D、3D、管道、运算、C库等系统基准性能提供测试数据。   最新版本UnixBench5.1.3，包含system和graphic测试，如果你需要测试graphic，则需要修改Makefile,不要注释掉'GRAPHIC_TE"
source: "https://teddysun.com/245.html"
tags:
tags-link:
type: "archive-web"
---
[![unixbench](https://teddysun.com/wp-content/uploads/2013/07/unixbench.png "Linux性能测试UnixBench一键脚本")](https://teddysun.com/wp-content/uploads/2013/07/unixbench_large.png)

UnixBench是一个类unix系（Unix，BSD，Linux）统下的性能测试工具，一个开源工具，被广泛用与测试linux系统主机的性能。Unixbench的主要测试项目有：系统调用、读写、进程、图形化测试、2D、3D、管道、运算、C库等系统基准性能提供测试数据。

最新版本UnixBench5.1.3，包含system和graphic测试，如果你需要测试graphic，则需要修改Makefile,不要注释掉”GRAPHIC\_TESTS = defined”，同时需要系统提供x11perf命令gl\_glibs库。  
下面的脚本使用了最新版UnixBench5.1.3来测试，注释了关于graphic的测试项（大多数VPS都是没有显卡或者是集显，所以图像性能无需测试），运行10-30分钟后（根据CPU内核数量，运算时间不等）得出分数，越高越好。

**测试方法：**

```
wget --no-check-certificate https://github.com/teddysun/across/raw/master/unixbench.sh
chmod +x unixbench.sh
./unixbench.sh
```

**测试项目：**  
Dhrystone 2 using register variables  
此项用于测试 string handling，因为没有浮点操作，所以深受软件和硬件设计（hardware and software design）、编译和链接（compiler and linker options）、代码优化（code optimazaton）、对内存的cache（cache memory）、等待状态（wait states）、整数数据类型（integer data types）的影响。

Double-Precision Whetstone  
这一项测试浮点数操作的速度和效率。这一测试包括几个模块，每个模块都包括一组用于科学计算的操作。覆盖面很广的一系列 c 函数：sin，cos，sqrt，exp，log 被用于整数和浮点数的数学运算、数组访问、条件分支（conditional branch）和程序调用。此测试同时测试了整数和浮点数算术运算。

Execl Throughput  
此测试考察每秒钟可以执行的 execl 系统调用的次数。 execl 系统调用是 exec 函数族的一员。它和其他一些与之相似的命令一样是 execve（） 函数的前端。

File copy  
测试从一个文件向另外一个文件传输数据的速率。每次测试使用不同大小的缓冲区。这一针对文件 read、write、copy 操作的测试统计规定时间（默认是 10s）内的文件 read、write、copy 操作次数。

Pipe Throughput  
管道（pipe）是进程间交流的最简单方式，这里的 Pipe throughtput 指的是一秒钟内一个进程可以向一个管道写 512 字节数据然后再读回的次数。需要注意的是，pipe throughtput 在实际编程中没有对应的真实存在。

Pipe-based Context Switching  
这个测试两个进程（每秒钟）通过一个管道交换一个不断增长的整数的次数。这一点很向现实编程中的一些应用，这个测试程序首先创建一个子进程，再和这个子进程进行双向的管道传输。

Process Creation  
测试每秒钟一个进程可以创建子进程然后收回子进程的次数（子进程一定立即退出）。process creation 的关注点是新进程进程控制块（process control block）的创建和内存分配，即一针见血地关注内存带宽。一般说来，这个测试被用于对操作系统进程创建这一系统调用的不同实现的比较。

System Call Overhead  
测试进入和离开操作系统内核的代价，即一次系统调用的代价。它利用一个反复地调用 getpid 函数的小程序达到此目的。

Shell Scripts  
测试一秒钟内一个进程可以并发地开始一个 shell 脚本的 n 个拷贝的次数，n 一般取值 1，2，4，8。（我在测试时取 1， 8）。这个脚本对一个数据文件进行一系列的变形操作（transformation）。

下面是我的一个512MB，2核，OpenVZ的VPS的跑分结果：

```
   BYTE UNIX Benchmarks (Version 5.1.3)

   System: vpn: GNU/Linux
   OS: GNU/Linux -- 2.6.32-042stab076.8 -- #1 SMP Tue May 14 20:38:14 MSK 2013
   Machine: i686 (i386)
   Language: en_US.utf8 (charmap="UTF-8", collate="UTF-8")
   CPU 0: Intel(R) Xeon(R) CPU L5520 @ 2.27GHz (4533.6 bogomips)
          Hyper-Threading, x86-64, MMX, Physical Address Ext, SYSENTER/SYSEXIT, SYSCALL/SYSRET, Intel virtualization
   CPU 1: Intel(R) Xeon(R) CPU L5520 @ 2.27GHz (4533.6 bogomips)
          Hyper-Threading, x86-64, MMX, Physical Address Ext, SYSENTER/SYSEXIT, SYSCALL/SYSRET, Intel virtualization
   09:41:17 up 31 days,  9:21,  1 user,  load average: 0.23, 0.05, 0.02; runlevel 3

------------------------------------------------------------------------
Benchmark Run: Mon Jul 29 2013 09:41:17 - 10:09:29
2 CPUs in system; running 1 parallel copy of tests

Dhrystone 2 using register variables       17172222.3 lps   (10.0 s, 7 samples)
Double-Precision Whetstone                     2600.2 MWIPS (10.0 s, 7 samples)
Execl Throughput                               4152.8 lps   (30.0 s, 2 samples)
File Copy 1024 bufsize 2000 maxblocks        622759.5 KBps  (30.0 s, 2 samples)
File Copy 256 bufsize 500 maxblocks          172634.3 KBps  (30.0 s, 2 samples)
File Copy 4096 bufsize 8000 maxblocks       1218236.9 KBps  (30.0 s, 2 samples)
Pipe Throughput                             1416230.5 lps   (10.0 s, 7 samples)
Pipe-based Context Switching                 206509.4 lps   (10.0 s, 7 samples)
Process Creation                               8568.6 lps   (30.0 s, 2 samples)
Shell Scripts (1 concurrent)                   3145.9 lpm   (60.0 s, 2 samples)
Shell Scripts (8 concurrent)                    528.3 lpm   (60.0 s, 2 samples)
System Call Overhead                        1528474.7 lps   (10.0 s, 7 samples)

System Benchmarks Index Values               BASELINE       RESULT    INDEX
Dhrystone 2 using register variables         116700.0   17172222.3   1471.5
Double-Precision Whetstone                       55.0       2600.2    472.8
Execl Throughput                                 43.0       4152.8    965.8
File Copy 1024 bufsize 2000 maxblocks          3960.0     622759.5   1572.6
File Copy 256 bufsize 500 maxblocks            1655.0     172634.3   1043.1
File Copy 4096 bufsize 8000 maxblocks          5800.0    1218236.9   2100.4
Pipe Throughput                               12440.0    1416230.5   1138.4
Pipe-based Context Switching                   4000.0     206509.4    516.3
Process Creation                                126.0       8568.6    680.0
Shell Scripts (1 concurrent)                     42.4       3145.9    742.0
Shell Scripts (8 concurrent)                      6.0        528.3    880.5
System Call Overhead                          15000.0    1528474.7   1019.0
                                                                   ========
System Benchmarks Index Score                                         960.4

------------------------------------------------------------------------
Benchmark Run: Mon Jul 29 2013 10:09:29 - 10:39:56
2 CPUs in system; running 2 parallel copies of tests

Dhrystone 2 using register variables       16851634.7 lps   (10.0 s, 7 samples)
Double-Precision Whetstone                     5182.9 MWIPS (10.0 s, 7 samples)
Execl Throughput                               4101.9 lps   (30.0 s, 2 samples)
File Copy 1024 bufsize 2000 maxblocks        635244.9 KBps  (30.0 s, 2 samples)
File Copy 256 bufsize 500 maxblocks          174430.2 KBps  (30.0 s, 2 samples)
File Copy 4096 bufsize 8000 maxblocks       1219982.0 KBps  (30.0 s, 2 samples)
Pipe Throughput                             1387297.9 lps   (10.0 s, 7 samples)
Pipe-based Context Switching                 196296.1 lps   (10.0 s, 7 samples)
Process Creation                              10889.9 lps   (30.0 s, 2 samples)
Shell Scripts (1 concurrent)                   4073.7 lpm   (60.0 s, 2 samples)
Shell Scripts (8 concurrent)                    550.5 lpm   (60.2 s, 2 samples)
System Call Overhead                        1538517.4 lps   (10.0 s, 7 samples)

System Benchmarks Index Values               BASELINE       RESULT    INDEX
Dhrystone 2 using register variables         116700.0   16851634.7   1444.0
Double-Precision Whetstone                       55.0       5182.9    942.3
Execl Throughput                                 43.0       4101.9    953.9
File Copy 1024 bufsize 2000 maxblocks          3960.0     635244.9   1604.2
File Copy 256 bufsize 500 maxblocks            1655.0     174430.2   1054.0
File Copy 4096 bufsize 8000 maxblocks          5800.0    1219982.0   2103.4
Pipe Throughput                               12440.0    1387297.9   1115.2
Pipe-based Context Switching                   4000.0     196296.1    490.7
Process Creation                                126.0      10889.9    864.3
Shell Scripts (1 concurrent)                     42.4       4073.7    960.8
Shell Scripts (8 concurrent)                      6.0        550.5    917.5
System Call Overhead                          15000.0    1538517.4   1025.7
                                                                   ========
System Benchmarks Index Score                                        1058.3
```

**参考链接：**  
[http://blog.sina.com.cn/s/blog\_7695e9f40100yimf.html](http://blog.sina.com.cn/s/blog_7695e9f40100yimf.html)

转载请注明：[秋水逸冰](https://teddysun.com/) » [Linux性能测试UnixBench一键脚本](https://teddysun.com/245.html)