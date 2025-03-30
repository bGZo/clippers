
## 2024-11-09 15:25:49

![](assets/microblock_pub/20250319_131632_408569.jpg) 

极客湾在骚测啥啊... 拿llama.cpp这b东西测速度，测出来结果72b int4把6000 Ada 48g干满了...这是多长的上下文/kv cache
很明显这oom以后llama.cpp全他妈把东西offload到内存里去算 完事果子的ddr5和内存带宽（比上不足比下有余）优势就出来了 我都不知道这到底是故意的还是不小心的了
但凡测显存内速度或者用vllm 果子（特别是 M4）那个小显存带宽都是被橄榄的命
https://t.me/microblock_pub/639

## 2024-11-03 01:20:47



我超我超我超 Chrome 131  上Direct Socket（TCP/UDP裸流）支持了！
https://chromestatus.com/feature/6398297361088512

可能群友还不知道这意味着什么 意思是现在电脑上99%的app都真的可以用浏览器完整实现了，比如什么b站视频下载，完全可以做成一个独立的网页（IWA）了，你甚至可以用浏览器写一个 HTTP Server！这实在是太酷了！
https://t.me/microblock_pub/629

## 2024-08-09 20:51:39

![](assets/microblock_pub/20250319_131701_385864.jpg) 

修了一年的bug总算修好了 结果居然是因为
真受不了了

一年啊 一年
你知道我这一年都怎么过的吗
https://t.me/microblock_pub/453

## 2025-01-09 18:36:36

![](assets/microblock_pub/20250319_131711_91878.jpg) 

[source](https://www.zhihu.com/question/666442307/answer/73325358117)
https://t.me/microblock_pub/762

## 2024-12-15 12:50:53



最近终于出了一个万众期待的新 CSS 特性：transition 支持关键字等的动画效果了
一个很简单的例子就是，如果写一个按钮，hover 前固定宽度，hover 后为 auto，开启前后的效果如视频所示
这个效果在有这个功能之前做起来非常麻烦，纯 CSS 应该是做不出来的，JS 写也特别麻烦
这个功能目前仅 Chrome 129+ 提供了支持，不过大家也可以用起来了，毕竟只是增强效果，不影响排版什么的
一些相关链接：
https://developer.mozilla.org/en-US/docs/Web/CSS/interpolate-size
https://developer.chrome.com/docs/css-ui/animate-to-height-auto
https://caniuse.com/?search=interpolate-size
https://t.me/microblock_pub/707

## 2024-12-15 12:50:53




https://t.me/microblock_pub/706
