---
title: "同步异步、阻塞非阻塞、并发并行的理解 - 斐斐のBlog"
created: 2025-04-05T15:50:58
modified: 2025-04-05T15:50:58
source: https://www.mmuaa.com/post/c02504ee02980387.html
tags:
tags-link:
type: archive-web
---

  * [首页](https://www.mmuaa.com/)
  * [归档](https://www.mmuaa.com/%e5%bd%92%e6%a1%a3)
  * [PAT真题](https://www.mmuaa.com/post/category/oj/pat)
  * [友情链接](https://www.mmuaa.com/%e5%8f%8b%e6%83%85%e9%93%be%e6%8e%a5)
  * [About Me](https://www.mmuaa.com/post/f37d1d793e8f236e.html)





Sign inMusic

[![](data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill-opacity="0"/></svg>)](https://www.mmuaa.com/)

[![](data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill-opacity="0"/></svg>)](https://www.mmuaa.com/)

#### 斐斐のBlog

@kidultff

  * [首页](https://www.mmuaa.com/)
  * [归档](https://www.mmuaa.com/%e5%bd%92%e6%a1%a3)
  * [PAT真题](https://www.mmuaa.com/post/category/oj/pat)
  * [友情链接](https://www.mmuaa.com/%e5%8f%8b%e6%83%85%e9%93%be%e6%8e%a5)
  * [About Me](https://www.mmuaa.com/post/f37d1d793e8f236e.html)



[首页](https://www.mmuaa.com/) » [计算机组成原理](https://www.mmuaa.com/post/category/ccp) » 同步异步、阻塞非阻塞、并发并行的理解

## 斐斐のBlog

@kidultff

  * 天津大学·智算学部
  * [www.mmuaa.com](https://www.mmuaa.com/)
  * 主人在20小时前来过。


[发送邮件](mailto:i@mmuaa.com)

# 同步异步、阻塞非阻塞、并发并行的理解

发布于 2018年11月26日 / [计算机组成原理](https://www.mmuaa.com/post/category/ccp) / 0 条评论

# 同步与异步：  


  * 同步：事情一件一件的做。执行事件A时，需要等A完成，再去做事件B。

  * 异步：事情可以一起做。执行事件A时，在等待事件A的结果的同时可以去做事件B。



  * 状态：等待事件A的结果的同时去做事件B，在做事件B时，每隔一段时间询问一次（轮询）事件A的状态如何，是否完成。

  * 通知：等待事件A的结果的同时去做事件B，并让A完成后通知一下调用者。

  * 回调：等待事件A的结果的同时去做事件B，并让A完成后执行一个函数，这个函数叫做回调函数。




# 阻塞与非阻塞：  


  * 阻塞：调用结果返回之前，线程被挂起，处于等待状态，直到结果返回

  * 非阻塞：调用不会使进程挂起，不会阻塞当前线程




# 并发与并行：

  * 并发：计算机只有一个CPU，却要运行辣么多线程，不可能同时进行，所以将CPU分成若干个时间段，分给不同的线程。当CPU在忙某个线程时，其他线程被挂起

  * 并行：计算机装有多个CPU或者CPU多线程，多个线程可以同时进行，这样叫做并行




转载原创文章请注明，转载自： [斐斐のBlog](https://www.mmuaa.com/ "斐斐のBlog") » [同步异步、阻塞非阻塞、并发并行的理解](https://www.mmuaa.com/post/c02504ee02980387.html "同步异步、阻塞非阻塞、并发并行的理解")

![](data:image/jpeg;base64,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)

插入图片
  * 取消
  * 提交



目前还没有评论，快来抢沙发吧~

网站已运行**2112** 天 /  [Statistics](https://new.cnzz.com/v1/login.php?siteid=1261166373) /  [Sitemap](https://www.mmuaa.com/sitemap.xml) /  [蒙ICP备16004866号-1](https://beian.miit.gov.cn/)

  * 作词 : 任盈洁/王家杰
  * 作曲 : 王宗贤/下川和己
  * 制作人 : 王宗贤/下川和己
  * 配唱制作人 : 任寒冰/陈嬛
  * 录音 : 任寒冰@行人Studio
  * Chinatown, a world full of dreams
  * But opportunity isn’t as easy as it seems
  * You gotta rise up to the extreme and work like busy bee
  * Channel all your energy to fulfill your fantasies
  *   * City lights, what a sight crawling over the night
  * Shaped like bright fireflies and dragons with a bite
  * This is Chinatown nothing here is black or white
  * Fireworks ignite, this is a city that excites
  *   * Welcome to my world, Chinatown! (唐人街!)
  * 各个是高手, 又怎样? (唐人街!)
  * 要世界转我的方向 (唐人街!)
  * 火力全开吶喊着梦想 ！向前闯
  *   * Working long nights but I’m acting brave
  * I am in charge of the road I pave
  * It’s time for me to complete this race
  * Finish out the day strong in first place
  *   * Here I go again in Chinatown doing my daily grind
  * Daily climb up to my apartment stairs I don’t mind
  * I just hope its a sign that if I try I will find
  * A place like this all the time
  * Everywhere, in all mankind
  *   * Welcome to my world, Chinatown! (唐人街!)
  * 各个是高手, 又怎样? (唐人街!)
  * 要世界转我的方向 (唐人街!)
  * 火力全开吶喊着梦想 (唐人街!) 向前闯
  *   * Chi-na-town!
  *   * If you feel lost or torn apart
  * If you need to depart for a fresh start,
  * If you need to move to a new city
  * If you need to find a new committee, ask
  * Chi-na-town!
  *   * Welcome to my world, Chinatown! (唐人街!)
  * 各个是高手, 又怎样? (唐人街!)
  * 要世界转我的方向 (唐人街!)
  * 火力全开吶喊着梦想 (唐人街!) 向前闯
  *   * Welcome to my world, Chinatown! (唐人街!)
  * 胆敢小看我的力量? (唐人街!)
  * 快放手一搏, 別傍徨 (唐人街!)
  * 越战越勇气魄震全场 (唐人街!) 向前闯


![](data:,)
