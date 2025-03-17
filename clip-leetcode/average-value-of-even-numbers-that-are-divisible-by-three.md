---
created: 2023-05-29
difficulty: easy
type: programming-problem
---

## Description
<iframe src="https://leetcode.cn/problems/average-value-of-even-numbers-that-are-divisible-by-three"></iframe>
## Solution
```cpp
    class Solution {
      public:
      int averageValue(vector<int>& nums) {
        int ans = 0, count = 0;
        for( auto num : nums){
          if(num % 6 == 0){
            ans += num;
            count++;
          }
        }
        if(count) return ans/count;
        else return 0;
      }
    };
```
## Conclusion
-