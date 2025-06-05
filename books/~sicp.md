---
aliases: Structure and Interpretation of Computer Programs, book/sicp
published: 
tags: TODO
source: https://book.douban.com/subject/
---

## Ch1 [Building Abstractions with Procedures](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-9.html#%_chap_1)
  - The third is separating them from all other ideas that accompany them in their real existence: this is called **abstraction**, and thus all its general ideas are made.
    id: dd297c86-e433-4fba-90b0-a3d7350d9d21
### Expressions
    - 组合
    - 操作数
    - 前缀表示法
    - 它可以容纳可以采用任意数量参数的过程
    - pretty-printing
    - 写入每个长组合，以便操作数垂直对齐
    - 生成的缩进清楚地显示了表达式的结构
    - 这种操作模式通常通过说解释器运行在一个读取评估打印循环
### Naming and the Environment 命名和环境
    - 定义是我们语言中最简单的抽象方式，因为它允许我们使用简单的名称来引用复合运算的结果
    - 复杂的程序是通过逐步构建复杂度不断增加的计算对象来构建的
    - 解释器使这种逐步的程序构造变得特别方便，因为可以在连续交互中逐步创建名称-对象关联。此功能鼓励程序的增量开发和测试
    - 一个Lisp程序通常由大量相对简单的程序组成
    - 将值与符号关联并稍后检索它们的可能性意味着解释器必须维护某种内存来跟踪名称-对象对
    - 环境
    - 全局环境
    - 涉及许多不同的环境
### Evaluating Combinations 评估组合
    - 必须首先对组合的每个元素执行评估过程
    - 评估规则是本质上是递归的
    - 递归的概念可以多么简洁地用于表达在深度嵌套组合的情况下，否则会被视为一个相当复杂的过程
    - 向上渗透
    - 递归是一种非常强大的技术，用于处理分层的树状对象
    - 评估规则的“向上渗透值”形式是一种通用过程的示例，称为树堆积
    - 环境的一般概念作为评估发生的上下文将在我们理解程序执行方面发挥重要作用
    - 特殊形式
    - 各种表达式（每个都有其相关的评估规则）构成编程语言的语法
### Compound Procedures 复合程序
    - 过程
    - 一种更强大的抽象技术，通过它可以给复合操作一个名称，然后将其称为一个单元
    - 过程定义的一般形式是（定义（<名称><形式参数>）<正文>）
### The Substitution Model for Procedure Application 程序应用的替代模型
    - 解释器评估组合的元素并将过程（它是组合的运算符的值）应用于参数（它是组合的操作数的值）
    - 替换的目的是帮助我们思考过程应用，而不是提供解释器如何真正工作的描述
    - 在本书的整个过程中，我们将介绍解释器如何工作的一系列越来越复杂的模型，最终在第5章中实现解释器和编译器。替换模型只是这些模型中的第一个——一种方法开始正式思考评估过程
    - 这种替代的“完全扩展然后减少”评估方法被称为正常顺序评估，与解释器实际使用的“评估参数然后应用”方法相反，该方法称为应用顺序评估
    - 通过避免对表达式进行多次求值获得额外的效率
    - 因为正常顺序求值变得更多当我们离开可以通过替换建模的程序领域时，处理起来很复杂
    - 正态评估
### Conditional Expressions and Predicates 条件表达式和谓词
    - 案例分析
    - cond（代表“条件”）
    - 由符号cond组成
    - 条款
    - 每对中的第一个表达式是谓词——即一个表达式，其值被解释为真或假
    - if表达式的一般形式是
    - and和or是特殊形式，而不是过程，因为子表达式不一定都是求值的
### Example: Square Roots by Newton's Method
### Procedures as Black-Box Abstractions
    - 至关重要的是，每个过程都完成一个可识别的任务，该任务可以用作定义其他过程的模块
    - 一个过程定义应该能够抑制细节
      - 过程嵌套定义有助于隐藏不必要的细节, 但要是像 [[cpp]] 该怎么做呢?
    - 本地名称
## refs
    - [DeathKing/Learning-SICP: MIT视频公开课《计算机程序的构造和解释》中文化项目及课程学习资料搜集](https://github.com/DeathKing/Learning-SICP)
## refs
  - [DeathKing/Learning-SICP: MIT视频公开课《计算机程序的构造和解释》中文化项目及课程学习资料搜集](https://github.com/DeathKing/Learning-SICP)
  - [sarabander/sicp: HTML5/EPUB3 version of SICP](https://github.com/sarabander/sicp)
  - [Structure and Interpretation of Computer Programs - Wikipedia](https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs)