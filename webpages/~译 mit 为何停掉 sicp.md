---
created: 2024-03-19T12:00:00
source: https://segmentfault.com/a/1190000005064958
type: archive-web
modified: 2025-01-15T11:38:21
---

原文： http://www.posteriorscience.net/?p=206

以下是不太严格的译文。

在纽约举行的一次 Lisp 集会上，Gerry Sussman 被问到 MIT 为何停掉著名的 6.001 课程。这门课所用的教材是 Sussman 与 Abelson 所写的《Structure and Interpretation of Computer Programs》(中译《计算机程序的构造与解释》)。Sussman 的回答如下：

他与 Hal Abelson 年事已经高，力不从心（他们从上个世纪 80 年代就开始教这门课），因此在 1997 年，他俩走进系主任办公室，扔下一句话『我们不干了，你们看着办吧』。

更重要的是，他们觉得 SICP 课程不适合培养现代的软件工程师了。Sussman 说，上个世纪八、九十年代的软件工程师们通过组合简单并且易于理解的部件的方式来构造复杂系统。SICP 的目标就是为推理论证这些复杂系统而提供一种抽象语言。

时至今日，情况变了。Sussman 指出，现代的软件工程师们的主要工作是为那些他们并不完全理解的复杂的硬件（由于商业机密的缘故，也不可能理解）而写代码。软件层面也存在同样的情况，编程环境是由无所不能的巨大的程序库构成。Sussman 说，他的学生们要玩转这些库，需要花费很多时间去阅读这些库的手册。他说，编程这件事在今天『很像科学研究』，你盯着库的某个一个局部去刺探它——写一个程序用于刺探，观察这个程序的行为，确认这个库能否满足自己需求。SICP 中的『合成分析』（Analysis-by-synthesis）的观点——基于小的简单的部件构建大的系统——现在变得无关紧要了。时下，大家是在刺探式编程。

至于为何选择 Python 来替代 Scheme，Sussman 开了个玩笑，说这是『后期绑定』策略。Python 有大量的库可用，这些库能够满足这门课的教师们所承担的项目的需求（例如编写用于控制机器人的软件）。

Sussman 认为曾经的 SICP 课程要比他们现在所开的课『更为清晰连贯』，而且他们依然没有弄明白什么才是正确的课程。

SICP 的在线版本见 https://mitpress.mit.edu/sicp/full-text/book/book.html

Sussman 与 Abelson 从 1986 年开始的在 HP 公司的授课视频见 http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video-lectures/
-
