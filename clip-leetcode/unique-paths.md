---
title: unique-paths
aliases:
  - unique-paths
created: 2025-01-15T10:44:29

modified: 2025-01-15T10:44:50
description: 
difficulty: medium
tags: 
type: programming-problem
---

## Description

<iframe src='https://leetcode.cn/problems/unique-paths' style='height:40vh;width:100%' class='iframe-radius' allow='fullscreen'></iframe>
<center>via: <a href='https://leetcode.cn/problems/unique-paths' target='_blank' class='external-link'>https://leetcode.cn/problems/unique-paths</a></center>

## Solutions

## Solution

```cpp
    class Solution {
      public:
      int dp[101]\[101];
      int uniquePaths(int m, int n) {
        for(int i = 1; i<=m; i++) dp[i]\[1] = 1;
        for(int i = 1; i<=n; i++) dp[1]\[i] = 1;
        for(int i = 2; i<=m ; i++){
          for(int j =2; j<=n ; j++){
            dp[i]\[j] = dp[i-1]\[j] + dp[i]\[j-1];
          }
        }
        return dp[m]\[n];
      }
    };
```

- 空间优化没怎么看懂；
- [【组合数学】马拦过河卒 | 潮汐朝夕](https://chengzhaoxi.xyz/ca8807c8.html)
-
