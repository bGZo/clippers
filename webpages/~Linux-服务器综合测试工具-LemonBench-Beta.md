---
title: "Linux服务器综合测试工具 LemonBench (Beta) - 极光星空"
created: 2025-04-05T15:50:57
modified: 2025-04-05T15:50:57
source: https://blog.ilemonrain.com/linux/LemonBench.html
tags:
tags-link:
type: archive-web
---

# Linux服务器综合测试工具 LemonBench (Beta) 

  * 博主： [ iLemonrain](https://blog.ilemonrain.com/author/1/)
  * 发布时间：2019 年 01 月 04 日
  * 18122次浏览
  * 6 条评论
  * 2380字数
  * 分类： [Linux技术](https://blog.ilemonrain.com/category/linux/)



  1. [首页](https://blog.ilemonrain.com/)
  2. 正文  


极光星空(iLemonrain) 原创作品！  
欢迎转载文章及工具，源代码开源，请遵守相关开源协议进行二次开发！

LemonBench TG交流群： <https://t.me/LemonBench>[](https://t.me/LemonBench)

LemonBench工具(别名LBench、柠檬Bench)，是一款针对Linux服务器设计的服务器性能测试工具。通过综合测试，可以快速评估服务器的综合性能，为使用者提供服务器硬件配置信息。

LemonBench目前涵盖了如下测试：

  * **服务器基础信息** (CPU信息/内存信息/Swap信息/磁盘空间信息/网络信息等)
  * **流媒体解锁测试** (目前支持HBO Now/动画疯/B站港澳台/B站台湾限定)
  * **系统性能测试 (CPU/内存/磁盘)**
  * **Speedtest网速测试** (本地到最近源及国内各地域不同线路的网速)
  * **路由追踪测试** (追踪到国内和海外不同线路的路由信息)


LemonBench使用起来非常简单，只需要复制粘贴再来个回车就可以轻松启动测试。

由于LemonBench还在开发中，程序的功能可能会做适当添加与删除。  
所以目前的版本品质仅供参考！也欢迎随时反馈BUG！

## 使用方法

### 快速测试

如果你的服务器上安装有 curl 工具，请使用以下命令执行脚本：
    
    
    curl -fsSL http://ilemonra.in/LemonBenchIntl | bash -s fast

如果你的服务器上安装有 wget 工具，请使用以下命令执行脚本：
    
    
    wget -qO- http://ilemonra.in/LemonBenchIntl | bash -s fast

### 完整测试

如果你的服务器上安装有 curl 工具，请使用以下命令执行脚本：
    
    
    curl -fsSL http://ilemonra.in/LemonBenchIntl | bash -s full

如果你的服务器上安装有 wget 工具，请使用以下命令执行脚本：
    
    
    wget -qO- http://ilemonra.in/LemonBenchIntl | bash -s full

由于测试用时较长，为防止发生SSH断线意外，推荐放在screen中运行！

## 测试项目

以下测试项目列表，为20191007版本的项目列表！测试内容随时可能发生变化，以实际版本为准！

  * **系统信息收集**
    * 系统名称 (包括版本号、系统位数)
    * CPU信息 (型号、缓存大小)
    * CPU数量检测 (自适应识别区分虚拟机(即VPS)与独立服务器)
    * 内存使用率
    * Swap使用率
    * 引导设备 (开机磁盘)
    * 系统负载 (1分钟/5分钟/15分钟，测试结果取启动测试时的实时结果)
  * **网络信息收集**
    * 本机IPV4地址及相关信息（ASN/归属地/运营商）
    * 本机IPV6地址及相关信息（ASN/归属地/运营商）
  * **流媒体解锁测试 (Beta)**
    * HBO Now 解锁测试
    * 巴哈姆特动画疯解锁测试
    * 哔哩哔哩 港澳台 及 台湾限定 解锁测试
  * **系统性能测试**
    * CPU性能测试
    * 内存性能测试
    * 磁盘性能测试 (4K测试结果适用于SSD介质磁盘，1M测试结果适用于SSD介质与HDD介质磁盘)
  * **Speedtest网速测试**
    * 最近测速点
    * 中国东北地区 (联通/移动)
    * 中国华北地区 (联通/移动)
    * 中国华中地区 (联通/电信)
    * 中国华东地区 (联通/移动)
    * 中国华南地区 (电信/移动)
    * 中国西南地区 (联通/移动)
    * 中国西北地区 (联通/电信/移动)
  * **路由追踪测试** (回程测试)
    * 国内部分：联通/电信/移动/联通精品网/电信CN2/鹏博士/教育网/科技网/广电网
    * 香港部分：CU/CT/CN2/HGC/HKBN/PCCW/TGT/WTT
    * 新加坡部分：CT/CN2/Singtel/StarHub/M1/AWS
    * 日本部分：NTT/IIJ/SoftBank/KDDI/CT/CN2/AWS
    * 韩国部分：KT/SK/LG/CN2/AWS
    * 台湾部分：Chief/APTG/CHT/TFN/FET/KBT/TAIFO
    * 美国部分：CT/CN2/PCCW/HE/GTT/ATT/TATA/NTT/Level3/ZAYO/Cogentco
    * 欧洲部分：Telekom/O2/Vodafont/CT/CN2/GTT/Cogentco/BT/TATA/RT/TTK/MTS
    * IPV6部分：联通/电信/移动/教育网 (CERNET2)
