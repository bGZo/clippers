---
title: "一键测试脚本bench.sh  |  秋水逸冰"
aliases: "一键测试脚本bench.sh  |  秋水逸冰"
created: 2025-04-05T17:25:47
modified: 2025-04-05T17:25:47
description: "经过几个版本的迭代，一键测试脚本 bench.sh 已经几乎适用于各个 Linux 发行版的网络和 IO 测试。 并将测试结果以较为美观的方式显示出来。 总结一下 bench.sh 的特点： 1、显示各种系统信息； 2、取自 Speedtest 世界多处的数据中心的测试点，网络测试比较全面； 3、支持 IPv6 下载测速； 4、IO 测试（顺序写入 1GB 数据）三次，并显示其平均值。    再配合 unixbench.sh 脚本测试，"
source: "https://teddysun.com/444.html"
tags:
tags-link:
type: "archive-web"
---
[技术](https://teddysun.com/category/tech) [秋水逸冰](https://teddysun.com/author/teddysun) 发布于: 2015-12-28 更新于: 2023-10-16 455132浏览 [99评论](https://teddysun.com/444.html#comments)

[![](https://teddysun.com/wp-content/uploads/2014/linux_2.png "一键测试脚本bench.sh")](https://teddysun.com/444.html)

经过几个版本的迭代，一键测试脚本 bench.sh 已经几乎适用于各个 Linux 发行版的网络和 IO 测试。  
并将测试结果以较为美观的方式显示出来。

### 总结一下 bench.sh 的特点：

1、显示各种系统信息；  
2、取自 Speedtest 世界多处的数据中心的测试点，网络测试比较全面；  
~~3、支持 IPv6 下载测速；~~  
4、IO 测试（顺序写入 1GB 数据）三次，并显示其平均值。

再配合 [unixbench.sh](https://teddysun.com/245.html) 脚本测试，即可全面测试 VPS 的性能。

**使用方法：**  
**命令：**

```
wget -qO- bench.sh | bash
```

或者

```
curl -Lso- bench.sh | bash
```

**备注：**  
bench.sh 既是脚本名，同时又是域名。所以不要怀疑我写错了或者你看错了。

**下载地址：**  
[https://github.com/teddysun/across/blob/master/bench.sh](https://github.com/teddysun/across/blob/master/bench.sh)

### 更新日志

2023 年 10 月 15 日更新：  
1\. 升级 speedtest-cli 的版本到 1.2.0；  
2\. 使用 shfmt 格式（美）化 bash script；  
3\. 新增 ✓ 和 ✗ 的 Emoji 颜文字（絵文字）；  
4\. 修正 CPU 型号中包含字符串 processor 导致的内核数量计算错误，比如有的虚拟机会把 CPU 名称显示为 Common KVM processor；  
![](https://teddysun.com/wp-content/uploads/2023/bench_20231016.png "bench.sh")

2023 年 06 月 10 日更新：  
1\. 新增是否支持 IPv4 和 IPv6 的判断并显示出 Online 或 Offline；  
![](https://teddysun.com/wp-content/uploads/2023/bench_202306111.png "bench.sh")

2022 年 02 月 22 日更新：  
1\. 新增 CPU 是否支持 AES-NI 和 VM-x/AMD-V 的判断；  
2\. 改进了计算硬盘空间的算法；  
3\. 改进了计算 RAM 和 Swap 的算法；  
4\. 改善时间戳显示方式，加入时区显示；  
![](https://teddysun.com/wp-content/uploads/2022/bench_20220223.png "bench.sh")

2022 年 01 月 01 日更新：  
1\. 优化脚本逻辑，美化显示方式；  
2\. 升级 speedtest-cli 的版本到 1.1.1；  
3\. 支持 arm64 (aarch64) 以及 armv7l (armhf) 架构，如下图；  
・arm64 (aarch64)  
![](https://teddysun.com/wp-content/uploads/2022/bench_20220101_2.png "bench.sh")

・armv7l (armhf)  
![](https://teddysun.com/wp-content/uploads/2022/bench_20220101_3.png "bench.sh")

4\. 优化 Speedtest 提供的测速服务器列表。  
・x86\_64  
![](https://teddysun.com/wp-content/uploads/2022/bench_20220101.png "bench.sh")

2020 年 07 月 29 日更新：  
1\. 修改：测速为 Speedtest 提供的，区分上传下载，更实用；  
2\. 增加：TCP Congestion Control；虚拟化方式；IP 信息等。

下图所示的是我的 [Vultr](https://qiu.sh/vultr) 的评测数据：  
![](https://teddysun.com/wp-content/uploads/2020/speedtest.png "bench.sh")

2018 年 01 月 07 日更新：  
修改：显示信息的颜色，分门别类，更容易区分。

下图所示的是我的 Kimsufi KS3C 百兆独服的评测数据：  
![](https://teddysun.com/wp-content/uploads/2018/ks3c_bench.png "bench.sh")

转载请注明：[秋水逸冰](https://teddysun.com/) » [一键测试脚本bench.sh](https://teddysun.com/444.html)