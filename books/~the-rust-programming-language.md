---
cover: t6_YueWen_32435929.jpg
aliases:
  - Rust权威指南
author: Steve Klabnik, Carol Nichols
translator: 毛靖凯 / 唐刚 / 沙渺
isbn: 9787121387067
publisher: 电子工业出版社
published: 20200601
tags:
  - rust
  - "#gtd/todo"
douban: https://book.douban.com/subject/35081743/
weread: https://weread.qq.com/web/bookDetail/d733256071eeeed9d7322fd
created: 2024-01-02T12:00:00
modified: 2024-12-17T09:33:29
---

  
## 第1章 入门指南

```shell
~ > rustc --version
# rustc 1.74.1 (a28077b28 2023-12-04) (Arch Linux rust 1:1.74.1-1)
```

### Install
### Hello, World!

```rust
fn main(){
    println!("Hello, world!");
}
// 1. 标准Rust风格使用4个空格而不是Tab来实现缩进。
// 2. Rust中所有以！结尾的调用都意味着你正在使用一个宏而不是普通函数。普通函数会以去掉！
// 3. 字符串作为参数传入了println!，并最终显示到了终端屏幕上。
// 4. 大部分的Rust代码行都会以分号来结尾。
```

编译完，怎么变大了这么多？

```shell
~/workspace/rust-project/CH01 > rustc --explain E0423
~/workspace/rust-project/CH01 > ll
总计 11M
drwxr-xr-x 2 bgzo bgzo 4.0K Jan 2日 22:40 ./
drwxr-xr-x 4 bgzo bgzo 4.0K Jan 2日 22:36 ../
-rwxr-xr-x 1 bgzo bgzo  11M Jan 2日 22:39 main*
-rw-r--r-- 1 bgzo bgzo   42 Jan 2日 22:40 main.rs
```


- 编译型 (预编译) 语言最好可以生成运行在不同平台的应用，正常无法看到源码；解释型语言需要在每一个运行的机器上都装有解释环境，正常都能看到源码；


> [!tip]
> 为什么是 Ruby、Python或JavaScript 是动态语言?

- **动态类型系统**
    - 在这些语言中，变量的类型是在运行时确定的，而不是在编译时确定。这意味着你可以在运行时更改变量的类型，使得代码更加灵活。例如，你可以在同一个变量中存储不同类型的数据。
- **运行时类型检查**
    - 动态语言通常在运行时执行类型检查，而不是在编译时。这使得更容易进行一些灵活的操作，如动态创建对象或在运行时修改类的结构。
- **动态内存分配**
    - 这些语言允许在运行时分配和释放内存，而不需要在编译时明确指定。这带来了方便，但也需要开发者注意内存管理，以避免潜在的内存泄漏问题。
- **反射和元编程**
    -  动态语言通常支持反射，即在运行时检查和修改程序的结构。这使得编写更加灵活和动态的代码成为可能。
- **解释执行**
    - 这些语言通常使用解释器而不是编译器，允许代码在运行时逐行执行。这使得开发者可以更容易地进行交互式开发和测试。

## 第2章 编写一个猜数游戏
### 创建一个新的项目
### 处理一次猜测
### 生成一个保密数字
### 比较猜测数字与保密数字
### 使用循环来实现多次猜测
### 总结
## 第3章 通用编程概念
### 变量与可变性
### 数据类型
### 函数
### 注释
### 控制流
### 总结
## 第4章 认识所有权
### 什么是所有权
### 引用与借用
### 切片
### 总结
## 第5章 使用结构体来组织相关联的数据
### 定义并实例化结构体
### 一个使用结构体的示例程序
### 方法
### 总结
## 第6章 枚举与模式匹配
### 定义枚举
### 控制流运算符match
### 简单控制流if let
### 总结
## 第7章 使用包、单元包及模块来管理日渐复杂的项目
### 包与单元包
### 通过定义模块来控制作用域及私有性
### 用于在模块树中指明条目的路径
### 用use关键字将路径导入作用域
### 将模块拆分为不同的文件
### 总结
## 第8章 通用集合类型
### 使用动态数组存储多个值
### 使用字符串存储UTF-8编码的文本
### 在哈希映射中存储键值对
### 总结
## 第9章 错误处理
### 不可恢复错误与panic!
### 可恢复错误与Result
### 要不要使用panic!
### 总结
## 第10章 泛型、trait与生命周期
### 通过将代码提取为函数来减少重复工作
### 泛型数据类型
### trait：定义共享行为
### 使用生命周期保证引用的有效性
### 同时使用泛型参数、trait约束与生命周期
### 总结
## 第11章 编写自动化测试
### 如何编写测试
### 控制测试的运行方式
### 测试的组织结构
### 总结
## 第12章 I/O项目：编写一个命令行程序
### 接收命令行参数
### 读取文件
### 重构代码以增强模块化程度和错误处理能力
### 使用测试驱动开发来编写库功能
### 处理环境变量
### 将错误提示信息打印到标准错误而不是标准输出
### 总结
## 第13章 函数式语言特性：迭代器与闭包
### 闭包：能够捕获环境的匿名函数
### 使用迭代器处理元素序列
### 改进I/O项目
### 比较循环和迭代器的性能
### 总结
## 第14章 进一步认识Cargo及crates.io
### 使用发布配置来定制构建
### 将包发布到crates.io上
### Cargo工作空间
### 使用cargo install从crates.io上安装可执行程序
### 使用自定义命令扩展Cargo的功能
### 总结
## 第15章 智能指针
### 使用Box<T\>在堆上分配数据
### 通过Deref trait将智能指针视作常规引用
### 借助Drop trait在清理时运行代码
### 基于引用计数的智能指针Rc<T\>
### RefCell<T\>和内部可变性模式
### 循环引用会造成内存泄漏
### 总结
## 第16章 无畏并发
### 使用线程同时运行代码
### 使用消息传递在线程间转移数据
### 共享状态的并发
### 使用Sync trait和Send trait对并发进行扩展
### 总结
## 第17章 Rust的面向对象编程特性
### 面向对象语言的特性
### 使用trait对象来存储不同类型的值
### 实现一种面向对象的设计模式
### 总结
## 第18章 模式匹配
### 所有可以使用模式的场合
### 可失败性：模式是否会匹配失败
### 模式语法
### 总结
## 第19章 高级特性
### 不安全Rust
### 高级trait
### 高级类型
### 高级函数与闭包
### 宏
### 总结
## 第20章 最后的项目：构建多线程Web服务器
### 构建单线程Web服务器
### 把单线程服务器修改为多线程服务器
### 优雅地停机与清理
### 总结
## 附录A 关键字
### 当前正在使用的关键字
### 将来可能会使用的保留关键字
### 原始标识符
## 附录B 运算符和符号
### 运算符
### 非运算符符号
## 附录C 可派生trait
### 面向程序员格式化输出的Debug
### 用于相等性比较的PartialEq和Eq
### 使用PartialOrd和Ord进行次序比较
### 使用Clone和Copy复制值
### 用于将值映射到另外一个长度固定的值的Hash
### 用于提供默认值的Default
## 附录D 有用的开发工具
### 使用rustfmt自动格式化代码
### 使用rustfix修复代码
### 使用Clippy完成更多的代码分析
### 使用Rust语言服务器来集成IDE
## 附录E 版本