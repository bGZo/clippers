---
created: 2024-10-12T00:00:00
difficulty: hard
tags: bfs 
type: programming-problem
modified: 2025-03-17T22:45:55
---

## Description

  <iframe src="https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations, 50vh, iframe-radius" style="height: 400px"></iframe>

## Solutions
```java
    class Solution {
      // 🌟 abstract trip: (x,y,status)
      final int[][] dirs = {{1,0,0}, {0,1,0}, {0,0,1}};
      public int minimumMoves(int[][] grid) {
        int n = grid.length, step = 1;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0, 0});
        boolean[][][] isVisited = new boolean[n]\[n][2];
        while(!queue.isEmpty()){
          int len = queue.size();
          while(len > 0){
            int[] arr = queue.poll();
            for(int[] dir: dirs){
              int x1 = arr[0] + dir[0],
              y1 = arr[1] + dir[1],
              z1 = arr[2] ^ dir[2]; // 蛇尾
              int x2 = x1 + z1,
              y2 = y1 + (z1 ^ 1); // 蛇头
              // 出界判定
              // 1.⚠ 数组未越界；
              // 2. 不能撞墙；
              // 3. 无重复访问；
              // 4. 🌟 若为旋转操作，则(x1 + 1, y1 + 1)位置不能有障碍物
              if( /** x1 < n && y1<n && */ x2<n && y2<n &&
                 grid[x1]\[y1] != 1 && grid[x2]\[y2] !=1 &&
                 !isVisited[x1]\[y1]\[z1] &&
                 (dir[2]==0 || grid[x1+1]\[y1+1] !=1)
                ){
                if(x1 == n-1 && y1 == n-2) return step;
                isVisited[x1]\[y1]\[z1] = true; // isVisited[x2]\[y2]\[z1] = true;
                queue.offer(new int[]{x1, y1, z1});
              }
            }
            len--;
          }
          step++;
        }
        return -1;
      }
    }
    /** https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/comments/1909674
    grid = [[0,0,0,0,0,1],
                   [1,1,0,0,1,0],
                   [0,0,0,0,1,1],
                   [0,0,1,0,1,0],
                   [0,1,1,0,0,0],
                   [0,1,1,0,0,0]]
     */
```

## Conclusion
-
