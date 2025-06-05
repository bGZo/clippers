---
aliases:
  - books/Effective_Python,
  - Effective Python 90 Specific Ways to Write Better Python
tags: 
author:
  - 布雷特·斯拉特金
translator: 爱飞翔
publisher: 机械工业出版社
published: 20210101
isbn: 9787111674023
created: 2023-02-12
douban: https://book.douban.com/subject/35334595/
weread: https://weread.qq.com/web/bookDetail/c2932f9072620d81c29c1ed
description: 本书可以帮你掌握真正的 Pythonic 编程方式，令你能够完全发挥出 Python 语言的强大功能，并写出健壮而高效的代码。Scott Meyers 在畅销书《Effective C++》中开创了一种以使用场景为主导的精练教学方式，本书作者 Brett Slatkin 就以这种方式汇聚了 90 条实践原则、开发技巧和便捷方案，并以实用的代码范例来解释它们。Slatkin 根据自己在 Google 公司多年开发 Python 基础架构所积累的经验，揭示 Python 语言中一些鲜为人知的微妙特性，并给出了能够改善代码功能及运行效率的习惯用法。通过本书，你能够了解到解决关键编程任务所用的奇妙方式，并学会编写易于理解、便于维护且利于改进的代码。
---
 
2020年出版...

## ![Effective Python: 90 Specific Ways to Write Better Python, Second Edition](../assets/books_Effective_Python_90_Specific_Ways_to_Write_Better.pdf)
## Contents
  - 第1章 培养Pythonic思维
    - 第1条 查询自己使用的Python版本
```shell
        python --version
        python3 --version
```
```python
        import sys
        print(sys.version_info)
        print(sys.version)
```
      - ]最后一个稳定的Python 2版本是2.7.17
    - 第2条 遵循PEP 8风格指南
      - title: Python Enhancement Proposal \#8
        aliases: PEP 8
        description: 一份针对Python代码格式而编订的风格指南。尽管只要语法正确，代码随便怎么写都行，但采用一致的风格可以使代码更易读、更易懂。
        document: [PEP 8 – Style Guide for Python Code | peps.python.org](https://peps.python.org/pep-0008/)
#### 与空白有关的建议
        - 用空格（space）表示缩进，而不要用制表符（tab）
        - 和语法相关的每一层缩进都用4个空格表示
        - **每行不超过79个字符**
        - 对于占据多行的长表达式来说，除了首行之外的其余各行都应该在通常的缩进级别之上再加4个空格
        - 在同一份文件中，**函数与类之间用两个空行隔开**
        - 在同一个类中，方法与方法之间用一个空行隔开
        - 使用字典时，键与冒号之间不加空格，写在同一行的冒号和值之间应该加一个空格
        - 给变量赋值时，赋值符号的左边和右边各加一个空格，并且只加一个空格就好
        - ==给变量的类型做注解（annotation）时，不要把变量名和冒号隔开，但在类型信息前应该有一个空格==
#### 与命名有关的建议
        - 函数、变量及属性用小写字母来拼写，各单词之间用下划线相连，例如：lowercase_underscore
        - **受保护的实例属性，用一个下划线开头**，例如：_leading_underscore
        - **私有的实例属性，用两个下划线开头**，例如：__double_leading_underscore
        - 类（包括异常）命名时，每个单词的首字母均大写，例如：CapitalizedWord
        - 模块级别的常量，所有字母都大写，各单词之间用下划线相连，例如：ALL_CAPS
        - **类中的实例方法，应该把第一个参数命名为self，用来表示该对象本身**
        - ==**类方法的第一个参数，应该命名为cls，用来表示这个类本身**==
#### 与表达式和语句有关的建议
        - > 每件事都应该有简单的做法，而且最好只有一种
          The Zen of Python
        - 采用行内否定，即把否定词直接写在要否定的内容前面，而不要放在整个表达式的前面
```python
            if a is not b # ✅
            if not a is b # ❌
```
        - 不要通过长度判断容器或序列是不是空的
```python
            if len(somelist) == 0  # ❌ 判断somelist是否为[]或''等空值
            if not somelist       # ✅ Python会把空值自动评估为False
```
        - 如果要判断容器或序列里面有没有内容，也不应该通过长度来判断
          - 应该采用if somelist语句，因为Python会把非空的值自动判定为True
        - **不要把if语句、for循环、while循环及except复合语句挤在一行**；
          - 应该把这些语句分成多行来写，这样更加清晰；
        - 如果表达式一行写不下，可以用括号将其括起来，而且要适当地添加换行与缩进以便于阅读
          - **多行的表达式，应该用括号括起来，而不要用\符号续行**
#### 与引入有关的建议
        - import语句（含from x import y）总是应该放在文件开头
        - 引入模块时，总是应该使用绝对名称，而不应该根据当前模块路径来使用相对名称
```python
            from bar import foo # ✅
            import foo         # ❌ 即便当前路径为bar包里，也不应该简写
            from . import foo   # ✅ 如果一定要用相对名称来编写import语句
```
        - 文件中的import语句应该按顺序划分成三个部分
          - 标准库里的模块
          - 第三方模块
          - 自己的模块
        - 属于同一个部分的import语句按字母顺序排列
    - [ ] #wait 第3条 了解bytes与str的区别 (都表示字符序列)  
      - `bytes`
        - bytes实例包含的是原始数据，即8位的无符号值（通常按照ASCII编码标准来显示）
```shell
          a = b'h\x65llo'
          print(list(a))
          print(a)
          >>>
          [104, 101, 108, 108, 111]
          b'hello'
```
      - `str`
        - str实例包含的是Unicode码点
        - 码点
          aliases: code point, 代码点
          description: 这些码点与人类语言之中的文本字符相对应
```shell
          a = 'a\u0300 propos'
          print(list(a))
          print(a)
          >>>
          ['a', '`', ' ', 'p', 'r', 'o', 'p', 'o', 's']
          à propos
```
    - 第4条 用支持插值的f-string取代C风格的格式字符串与str.format方法
    - 第5条 用辅助函数取代复杂的表达式
```python
        from urllib.parse import parse_qs
        my_values = parse_qs('red=5&blue=0&green=',
                   keep_blank_values=True)
        red = int(my_values.get('red', [''])[0] or 0)
        green = int(my_values.get('green', [''])[0] or 0)
        opacity = int(my_values.get('opacity', [''])[0] or 0)
```
    - ==第6条 把数据结构直接拆分到多个变量里，不要专门通过下标访问==
    - 第7条 尽量用enumerate取代range
    - 第8条 用zip函数同时遍历两个迭代器
    - ==第9条 不要在for与while循环后面写else块==
    - ==第10条 用赋值表达式（assignment expression）减少重复代码==
      - Since Python 3.8
      - 海象操作符（walrus operator）
  - 第2章 列表与字典
    - 第11条 学会对序列做切片
    - 第12条 不要在切片里同时指定起止下标与步进
    - 第13条 通过带星号的unpacking操作来捕获多个元素，不要用切片
    - 第14条 用sort方法的key参数来表示复杂的排序逻辑
    - 第15条 不要过分依赖给字典添加条目时所用的顺序
    - 第16条 用get处理键不在字典中的情况，不要使用in与KeyError
    - 第17条 用defaultdict处理内部状态中缺失的元素，而不要用setdefault
    - 第18条 学会利用__missing__构造依赖键的默认值
  - 第3章 函数
    - 第19条 不要把函数返回的多个数值拆分到三个以上的变量中
    - 第20条 遇到意外状况时应该抛出异常，不要返回None
    - 第21条 了解如何在闭包里面使用外围作用域中的变量
    - 第22条 用数量可变的位置参数给函数设计清晰的参数列表
    - 第23条 用关键字参数来表示可选的行为
    - 第24条 用None和docstring来描述默认值会变的参数
    - 第25条 用只能以关键字指定和只能按位置传入的参数来设计清晰的参数列表
    - 第26条 用functools.wraps定义函数修饰器
  - 第4章 推导与生成
    - ==第27条 用列表推导取代map与filter==
    - 第28条 控制推导逻辑的子表达式不要超过两个
    - 第29条 用赋值表达式消除推导中的重复代码
    - 第30条 不要让函数直接返回列表，应该让它逐个生成列表里的值
    - 第31条 谨慎地迭代函数所收到的参数
    - 第32条 考虑用生成器表达式改写数据量较大的列表推导
    - 第33条 通过yield from把多个生成器连起来用
    - 第34条 不要用send给生成器注入数据
    - 第35条 不要通过throw变换生成器的状态
    - 第36条 考虑用itertools拼装迭代器与生成器
  - 第5章 类与接口
    - 第37条 用组合起来的类来实现多层结构，不要用嵌套的内置类型
    - 第38条 让简单的接口接受函数，而不是类的实例
    - 第39条 通过@classmethod多态来构造同一体系中的各类对象
    - 第40条 通过super初始化超类
    - 第41条 考虑用mix-in类来表示可组合的功能
    - 第42条 优先考虑用public属性表示应受保护的数据，不要用private属性表示
    - 第43条 自定义的容器类型应该从collections.abc继承
  - 第6章 元类与属性
    - 第44条 用纯属性与修饰器取代旧式的setter与getter方法
    - 第45条 考虑用@property实现新的属性访问逻辑，不要急着重构原有的代码
    - 第46条 用描述符来改写需要复用的@property方法
    - 第47条 针对惰性属性使用__getattr__、__getattribute__及__setattr__
    - 第48条 用__init_subclass__验证子类写得是否正确
    - 第49条 用__init_subclass__记录现有的子类
    - 第50条 用__set_name__给类属性加注解
    - 第51条 优先考虑通过类修饰器来提供可组合的扩充功能，不要使用元类
  - 第7章 并发与并行
    - 第52条 用subprocess管理子进程
    - 第53条 可以用线程执行阻塞式I/O，但不要用它做并行计算
    - 第54条 利用Lock防止多个线程争用同一份数据
    - 第55条 用Queue来协调各线程之间的工作进度
    - 第56条 学会判断什么场合必须做并发
    - 第57条 不要在每次fan-out时都新建一批Thread实例
    - 第58条 学会正确地重构代码，以便用Queue做并发
    - 第59条 如果必须用线程做并发，那就考虑通过ThreadPoolExecutor实现
    - 第60条 用协程实现高并发的I/O
    - 第61条 学会用asyncio改写那些通过线程实现的I/O
    - 第62条 结合线程与协程，将代码顺利迁移到asyncio
    - 第63条 让asyncio的事件循环保持畅通，以便进一步提升程序的响应能力
    - 第64条 考虑用concurrent.futures实现真正的并行计算
  - 第8章 稳定与性能
    - 第65条 合理利用try/except/else/finally结构中的每个代码块
    - 第66条 考虑用contextlib和with语句来改写可复用的try/finally代码
    - ==第67条 用datetime模块处理本地时间，不要用time模块==
    - 第68条 用copyreg实现可靠的pickle操作
    - 第69条 在需要准确计算的场合，用decimal表示相应的数值
    - ==第70条 先分析性能，然后再优化==
    - 第71条 优先考虑用deque实现生产者-消费者队列
    - 第72条 考虑用bisect搜索已排序的序列
    - 第73条 学会使用heapq制作优先级队列
    - 第74条 考虑用memoryview与bytearray来实现无须拷贝的bytes操作
  - 第9章 测试与调试
    - 第75条 通过repr字符串输出调试信息
    - 第76条 在TestCase子类里验证相关的行为
    - 第77条 把测试前、后的准备与清理逻辑写在setUp、tearDown、setUp-Module与tearDownModule中，以防用例之间互相干扰
    - 第78条 用Mock来模拟受测代码所依赖的复杂函数
    - 第79条 把受测代码所依赖的系统封装起来，以便于模拟和测试
    - 第80条 考虑用pdb做交互调试
    - 第81条 用tracemalloc来掌握内存的使用与泄漏情况
  - 第10章 协作开发
    - 第82条 学会寻找由其他Python开发者所构建的模块
    - ==第83条 用虚拟环境隔离项目，并重建依赖关系==
    - 第84条 每一个函数、类与模块都要写docstring
    - 第85条 用包来安排模块，以提供稳固的API
    - 第86条 考虑用模块级别的代码配置不同的部署环境
    - 第87条 为自编的模块定义根异常，让调用者能够专门处理与此API有关的异常
    - 第88条 用适当的方式打破循环依赖关系
    - 第89条 重构时考虑通过warnings提醒开发者API已经发生变化
    - 第90条 考虑通过typing做静态分析，以消除bug
## Comment
  - 最傻逼的地方来了，中文般代码的插入是用图片，而不是文本格式🤣
-