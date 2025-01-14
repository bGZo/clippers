# Nacos源码分析 8:05正式上课

![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1396/1650540523037/b025eb1a9b2b41449fd0e7e92074a336.png)

## 服务注册

从Nacos-Client说起，涉及到服务注册，先来了解一下Nacos客户端将会传递什么信息给服务端，从一个测试类来说起：

1. 服务注册信息封装：

* 基础信息
  * ip
  * 端口
  * 权重。。。。
* 元数据
  * 心跳时间
  * 心跳的超时时间
  * 网络类型
  * Nacos版本。。。

2. NamingServer的实例化

* 服务实例注册
* 服务实例销毁
* 获取服务实例列表
* 订阅
* 取消订阅

3. NamingClientProxyDelegate选择通信方式

* 基于是否是瞬时对象选择协议
  * gRPC实现
  * Http实现

4. 基于gRPC协议请求Nacos注册

* 核心操作
  * 缓存当前实例信息
  * 基于gRPC与Nacos进行通信

## Nacos1.x架构存在的一些问题：

一句话总结：心跳多，无效查询多，心跳续约感知变化慢，连接消耗大，资源空耗严重。

在Nacos2.x版本以后新增gPRC长连接以后，好处在于性能的提高


## 实例客户端注册


![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/fyfile/1396/1650540523037/de9806751a344eab95d3e484076a4b18.png)
