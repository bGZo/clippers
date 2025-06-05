---
title: "C++algorithm中可提高编程效率的几个算法函数 - 斐斐のBlog"
created: 2025-04-05T16:38:21
modified: 2025-04-05T16:38:21
description: "binary_search：二分查找lower_bound：通过二分查找，返回容器中第一个大于或等于n的位置upper_bound：通过二分查找，返回容器中第一个大于n的位置copy：容器拷贝count：通过等于运算符计算容器中特定元素出现次数。（对于struct等，可以重载等于号）find：容器中查找元素，返回迭代器（指针）max_element/min_element：返回容器最大/最小值的迭…"
source: "https://www.mmuaa.com/post/1267ae8bd420c6a6.html"
tags:
tags-link:
type: "archive-web"
---
## binary\_search：二分查找

![blob.png](https://www.mmuaa.com/wp-content/uploads/image/20181227/1545889977159223.png "1545889977159223.png")

## lower\_bound：通过二分查找，返回容器中第一个大于或等于n的位置

## upper\_bound：通过二分查找，返回容器中第一个大于n的位置

![blob.png](https://www.mmuaa.com/wp-content/uploads/image/20181227/1545891730509980.png "1545891730509980.png")

## copy：容器拷贝  

![blob.png](https://www.mmuaa.com/wp-content/uploads/image/20181227/1545890274976456.png "1545890274976456.png")

## count：通过等于运算符计算容器中特定元素出现次数。（对于struct等，可以重载等于号）  

![blob.png](https://www.mmuaa.com/wp-content/uploads/image/20181227/1545890502536150.png "1545890502536150.png")

## find：容器中查找元素，返回迭代器（指针）  

![blob.png](https://www.mmuaa.com/wp-content/uploads/image/20181227/1545890648315402.png "1545890648315402.png")

## max\_element/min\_element：返回容器最大/最小值的迭代器（指针）

![blob.png](https://www.mmuaa.com/wp-content/uploads/image/20181227/1545891131877406.png "1545891131877406.png")

## \_\_gcd：返回两个元素的最小公约数

![blob.png](https://www.mmuaa.com/wp-content/uploads/image/20181227/1545891467362945.png "1545891467362945.png")

## 此外，还有一些常见的：

sort/stable\_sort：前者排序，后者稳定排序（保证元素相同时，前后元素按照原来的顺序）

swap：交换元素的值

reverse：反转容器

fill：填充容器，使容器全部赋成某个值

replace：替换容器的值