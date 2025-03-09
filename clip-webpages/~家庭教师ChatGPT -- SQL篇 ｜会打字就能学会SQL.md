---
created: 2023-04-08T12:00:00
source: "https://blog.simona.life/posts/chatgpt_sql"
type: "archive-web"
modified: 2025-01-15T11:38:18
---

![alt text](https://i.typlog.com/simona/8320703910_016098.png)朋友们，想转行数据吗？那我的第一个问题就会是，你会写 SQL 吗？

之前有 [推荐过几个SQL的课程](https://blog.simona.life/posts/how-to-start-learning-data-analytics-with-zero-background)，其实有了 ChatGPT 之后，连 SQL 课程都不需要了。甚至连在电脑上安装 SQL，这件曾经让我很崩溃，几乎要放弃 SQL 的事情也不需要了。家庭教师 ChatGPT 都可以提供！

\[ ⚠️ \] 以下会有大量中英文夹杂，因为我不会翻译，介意的朋友可以优雅离场了。

今天来分享一下我测试 ChatGPT 来学习 SQL 的全过程，以及我用的 prompt。有了 ChatGPT，只要会打字就能学会 SQL！

以下内容包括：

1. 让 ChatGPT 给一个 study plan；
2. 让 ChatGPT 给题目，不要给答案，并且 visualize 表格；
3. 让 ChatGPT 分析解题思路；
4. 让 ChatGPT 出面试题目；
5. 让 ChatGPT 辅导写 Leetcode

直接开始！

`i don't have SQL on my computer, can you act as mysql `

首先我问了 ChatGPT 它可不可以 act as SQL server。它说不行。但是后面测试的时候，只要在对话框里打 SQL syntax，它就可以理解啦。所以不用担心！

`what are the most basic sql i should know about`

接着我问它需要知道 SQL 最基础的内容。它给了回答。

![Screenshot 2023-03-20 at 2.24.18 PM.png](https://i.typlog.com/simona/8320706521_507283.png)

`can you come up with a study plan for SQL. i want to learn the basics one by one with practices.`

![Screenshot 2023-03-20 at 3.01.19 PM.png](https://i.typlog.com/simona/8320704308_946776.png)

`can you give me a basic sql question practicing select statement only. please do not give me answer yet. please visualize the example tables with examples.`

下一步的话，我们就可以开始练习啦！可以从最上面的一条 `SELECT` 开始，让 ChatGPT 出题目。记得让它不要给答案先哦。并且可以让它数据的时候可以给一个例子。

![Screenshot 2023-03-20 at 2.29.07 PM.png](https://i.typlog.com/simona/8320706230_761635.png)

![Screenshot 2023-03-20 at 2.29.15 PM.png](https://i.typlog.com/simona/8320706224_805501.png)

`how should i start thinking about this question. `

但是我完全不会写 SQL 怎么办呢，那就问家庭教师呀。（不得不说，思路很清晰！）

![Screenshot 2023-03-20 at 2.31.08 PM.png](https://i.typlog.com/simona/8320706112_474162.png)

![Screenshot 2023-03-20 at 2.31.14 PM.png](https://i.typlog.com/simona/8320706104_640097.png)

到这里，我们就可以开始写写看。我故意写了错的答案，看一下它会怎么指导我。

`select first name, last name, salary, from employees where salary >1000`

![Screenshot 2023-03-20 at 2.34.55 PM.png](https://i.typlog.com/simona/8320705891_812887.png)

这个题目比较简单。`JOIN` 是面试的时候经常会考到的题目，并且会考不同的 JOIN 之间的区别。所以我让 ChatGPT 给我一道 JOIN 的题目，但是不要告诉我是哪一种 JOIN。

`i want to practice join, including INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN. please give me a question to practice one of the joins. do not tell me which type of join i should use. visualize the example tables.  `

![Screenshot 2023-03-20 at 2.38.01 PM.png](https://i.typlog.com/simona/8320705707_534856.png)

`how the output should look like? can you visualize the output table`

如果你觉得这个题目有一点点复杂，可以先让 ChatGPT 给一个 output 的样子，帮助理解。

![Screenshot 2023-03-20 at 2.40.11 PM.png](https://i.typlog.com/simona/8320705576_295177.png)

`how should i think about this question`

还是觉得有一点不知道如何下手，那就让 ChatGPT 一步步拆解。

![Screenshot 2023-03-20 at 2.41.52 PM.png](https://i.typlog.com/simona/8320705476_288057.png)

`how to determine which type of join to use in this question?`

在关于 JOIN 的题目里，决定哪一种 JOIN 是最重要的一步，我们也可以问 ChatGPT。

![Screenshot 2023-03-20 at 2.45.12 PM.png](https://i.typlog.com/simona/8320705276_887144.png)

`select first_name, last_name, department_name, salary from employees join departments on department_id = department_id `

这里我又故意给了错误的回答，在 department\_id 前面没有加上 table 的名字。

ChatGPT 就指出了这个错误，并且教我使用 aliases。

![Screenshot 2023-03-20 at 2.48.43 PM.png](https://i.typlog.com/simona/8320705065_630814.png)

在各种练习之后，我们可以开始准备面试了！

`can you find a question used by facebook during data engineer interview`

![Screenshot 2023-03-20 at 2.49.55 PM.png](https://i.typlog.com/simona/8320704994_059797.png)

`can you give me a more complex question that has been used in data engineer interviews`

上面这个问题有一点点太简单啦，我就问有没有更难的问题。

![Screenshot 2023-03-20 at 2.51.31 PM.png](https://i.typlog.com/simona/8320704898_084246.png)

最后的话来看一下 ChatGPT 如何辅导 Leetcode SQL 题目。 我随便找了一道 Leetcode database 的题目，[https://leetcode.cn/problems/second-highest-salary/](https://leetcode.cn/problems/second-highest-salary/)，复制粘贴给 ChatGPT。

![Screenshot 2023-03-20 at 3.12.55 PM.png](https://i.typlog.com/simona/8320703613_022677.png)

`can you explain?`

![Screenshot 2023-03-20 at 3.14.44 PM.png](https://i.typlog.com/simona/8320703505_05631.png)

`what if we want to get the Nth highest salary? `

![Screenshot 2023-03-20 at 3.16.44 PM.png](https://i.typlog.com/simona/8320703384_795472.png)

`what does 'LIMIT n-1, 1 ' mean? `

这里出现了一个新的概念 Offset，于是就追问一下。

![Screenshot 2023-03-20 at 3.18.55 PM.png](https://i.typlog.com/simona/8320703252_930332.png)

---

### 总结一下：

上面是我测试如果用 ChatGPT 来自学 SQL 的实录。总结一下：

1. ChatGPT 教得很好；
2. SQL 最主要的学习方式就是练习以及解题思路，可以让 ChatGPT 给很多练习题，并且让它给出如何一步步思考的过程；
3. 遇到不会写的题目，就拿给 ChatGPT 吧！

---

### About Me：

很开心遇见你！我是穿堂风，也是 Simona。曾经的资深互联网数据打工人（Data Engineer），2022 年 11 月被 Facebook 裁员后，开启数字游民生活。

我正在做的项目和提供的服务在我的个人主页。[https://simona.life/](https://simona.life/)

---

### 家庭教师 ChatGPT 系列

[ChatGPT教我写网页实录](https://thepodluckclub.com/club-only-ywdp-075/)
