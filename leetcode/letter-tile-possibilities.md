---
created: 2023-05-19T00:00:00
difficulty: medium
type: programming-problem
modified: 2025-03-17T22:45:09
---

## Description

<iframe src="https://leetcode.cn/problems/letter-tile-possibilities"></iframe>

## Solution
```cpp
    class Solution {
      public:
      int numTilePossibilities(string tiles) {
        int count[26] = {0};
        for(char ch: tiles){
          count[ch-'A']++;
        }
        return dfs(count);
      }
      int dfs(int count[]){
        int res = 0;
        for(int i =0; i< 26; i++){
          if(count[i]==0)
            continue;
          res++;
          count[i]--;
          res += dfs(count); // NOTE!!!
          count[i]++;
        }
        return res;
      }
    };
```

## Conclusion
  - tree hashtable backtracking
  - ![msedge_545.gif](../assets/msedge_545_1684489334618_0.gif)
    [LeetCode 第 1079 题：“活字印刷”题解 | LeetCode 题解 (liweiwei1419.github.io)](https://liweiwei1419.github.io/leetcode-solution-blog/leetcode-problemset/backtracking/1079-letter-tile-possibilities.html#%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%EF%BC%88python-%E4%BB%A3%E7%A0%81%EF%BC%89)
    [回溯算法（设计递归函数的返回值） - 活字印刷 - 力扣（LeetCode）](https://leetcode.cn/problems/letter-tile-possibilities/solution/hui-su-suan-fa-python-dai-ma-by-liweiwei1419/)
    - 题解的配图太棒了
