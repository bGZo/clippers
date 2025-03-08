---
title: "如何使用JS获取系统内存、CPUGPU、电量等信息-«-张鑫旭-鑫空间-鑫生活"
created: 2025-03-02T20:31:25
modified: 2025-03-02T20:31:25
description: "有些前端开发可能还不知道，JavaScript是有能力获取操作系统的内存、CPU/GPU、电量、蓝牙、掉线等信息的。"
source: "https://www.zhangxinxu.com/wordpress/2024/12/js-get-memory-cpu-gpu-battery/"
tags:
tags-link:
type: "archive-web"
---
by [zhangxinxu](https://www.zhangxinxu.com/) from [https://www.zhangxinxu.com/wordpress/?p=11498](https://www.zhangxinxu.com/wordpress/?p=11498)  
本文可全文转载，独立域名个人网站无需授权，但需要保留原作者、出处以及文中链接，任何网站均可摘要聚合，商用请联系授权。

![封面图 JS系统 圣诞](https://image.zhangxinxu.com/image/blog/202412/js-system-cover.jpg)

目前，浏览器是有能力获取系统的一些信息的，包括内存大小，CPU/GPU、电量等。

### 一、JS获取内存大小

很简单，下面一行代码即可：

```undefined
navigator.deviceMemory
```

例如在我的Chrome浏览器控制台的输出结果就是：

![设备内存大小获取](https://image.zhangxinxu.com/image/blog/202412/2024-12-20_201551.png)

`deviceMemory`的兼容性如下截图所示，目前仅Chrome浏览器支持。

![deviceMemory设备内存获取兼容性](https://image.zhangxinxu.com/image/blog/202412/2024-12-20_201721.png)

### 二、JavaScript get cpu信息

目前Web没法获取CPU具体的参数信息，但是可以获取CPU的核数。

同样是navigator对象，不过属性值看不到CPU三个字母的影子，名为hardwareConcurrency，表示可以并行运行的硬件数量。

代码示意：

```undefined
navigator.hardwareConcurrency
```

运行结果示意：

![CPU核数示意](https://image.zhangxinxu.com/image/blog/202412/2024-12-20_202201.png)

没想到，我的破电脑CPU是12核的，应该与去年换主板有关，不过没看出性能有多少提升。

不过Mac下貌似可以看出芯片的品牌，例如我的Mac办公电脑运行`navigator.platform`返回的是`'MacIntel'`。

`hardwareConcurrency`值的兼容性比`deviceMemory`好多了，参见下图，可以看到所有标准浏览器都是支持的：

![硬件并行数量兼容性](https://image.zhangxinxu.com/image/blog/202412/2024-12-20_203158.png)

### 三、GPU也是可以获取的

也是一行语法：

```undefined
navigator.gpu
```

不过`navigator.gpu`返回的并不是具体的数值，而是GPU对象，这个对象和WebGPU API关联密切。

支持一个属性和两个方法，属性是`wgslLanguageFeatures`，方法为`requestAdapter()`和`getPreferredCanvasFormat()`。

而`navigator.gpu.wgslLanguageFeatures.size`返回的是当前Web环境支持的WGSL语言特征数量，例如我的电脑windows电脑返回的是4，Mac笔记本也是4，有些GPU比较老，数量就不会是4.

不过这个API……怎么说呢，跟想象的有些不一样，检测的其实是浏览器是否支持WebGPU，以及是否可以调用适配器，以使用WebGL等功能。

我看来下兼容性，嘿，最新的Safari和Firefox都已经支持了，还挺巧的。

![GPU属性兼容性](https://image.zhangxinxu.com/image/blog/202412/2024-12-20_204918.png)

### 四、设备的电量识别

电量获取使用getBattery()方法，使用示意：

```javascript
let batteryIsCharging = false;

navigator.getBattery().then((battery) => {
  
  console.log(battery.level);
  
  batteryIsCharging = battery.charging;
  
  
  battery.addEventListener("chargingchange", () => {
    batteryIsCharging = battery.charging;
  });
});
```

通过上述代码，我们就可以获悉当前设备的电量状态，以及是否是充电状态。

像是PC电脑，接电源的，没电池的，只要设备运行，电量范围就一定是1，但是移动笔记本就会不一样。

我们可以据此，显示自定义的电池进度，充电动画，或者低电量模式的交互提醒（例如，关闭不必要的动画以帮助用户省电）等。

这个API其实和用户体验还是走得蛮近的，兼容性的话，我看看，是这样的：

![getBattery兼容性](https://image.zhangxinxu.com/image/blog/202412/2024-12-20_205839.png)

有些遗憾，仅仅Chrome浏览器支持，怪不得社区很少见到有对此API的讨论。

而且从Chrome开始支持的时间来看，短时间内，看不到Safari浏览器支持的迹象。

这么好的API，目前也只能当做玩具使用了。

### 五、其他一些硬件与设备的识别

`navigator`对象还提供了很多其他的硬件识别，例如蓝牙，虚拟键盘，USB，外置摄像头，是否掉线（navigator.onLine）等。

篇幅原因，我就不一一展示了，有兴趣可以访问对应的文档。

只要遇到类似的场景，知道Web有这样的能力就可以了。

ok，就这样吧，轻轻松松，又水了一篇文章，佛佛佛。

![佛佛佛](https://image.zhangxinxu.com/image/blog/202412/2024-12-23_002114.jpeg)

（本篇完） ![](https://image.zhangxinxu.com/image/emtion/emoji/1f44d.svg) 是不是学到了很多？可以分享到微信！  
![](https://image.zhangxinxu.com/image/emtion/emoji/1f44a.svg) 有话要说？点击[这里](https://www.zhangxinxu.com/wordpress/2024/12/js-get-memory-cpu-gpu-battery/#comment "点击定位到评论")。