---
created: 2025-01-16T21:37:52
difficulty: medium
type: programming-problem
title: alert-using-same-key-card-three-or-more-times-in-a-one-hour-period
aliases:
  - alert-using-same-key-card-three-or-more-times-in-a-one-hour-period
modified: 2025-01-16T21:37:52
description: 
tags:
---

## Description
<iframe src='https://leetcode.cn/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://leetcode.cn/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period' target='_blank' class='external-link'>https://leetcode.cn/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period</a></center>

## Solutions
## Conclusion
  - 多声明局部变量是一个好习惯，有时候为了紧凑的写法，而不考虑写更清晰的局部变量非常不明智 #code-style
```java
      for(int i = 0; i<keyName.length; i++){
        hm.putIfAbsent(keyName[i], new ArrayList<>());
        Integer hour = (keyTime[i].charAt(0) -'0')* 10 + (keyTime[i].charAt(1) - '0');
        Integer minute = (keyTime[i].charAt(3) - '0')* 10 + (keyTime[i].charAt(4) - '0');
        timeMap.get(keyName[i]).add(hour*60+minute);
      }
      // Integer hour = (keyTime[i].charAt(0) -'0')* 10 + (keyTime[i].charAt(1) - '0');
      //                                                    ↑
      // 这里非常容易写错，是冗余的写法；
      for (int i = 0; i < n; i++) {
        String name = keyName[i];
        String time = keyTime[i];
        timeMap.putIfAbsent(name, new ArrayList<Integer>());
        int hour = (time.charAt(0) - '0') * 10 + (time.charAt(1) - '0');
        int minute = (time.charAt(3) - '0') * 10 + (time.charAt(4) - '0');
        timeMap.get(name).add(hour * 60 + minute);
      }
```
```
    *// error        ArrayList<String> key_time = (ArrayList<String>) Arrays.asList(keyTime);
    **// right        ArrayList<String> key_time = new ArrayList<>(Arrays.asList(keyTime));
    *
```