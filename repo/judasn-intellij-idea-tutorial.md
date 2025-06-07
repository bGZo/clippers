---
title: judasn/intellij-idea-tutorial
aliases: intellij-idea-tutorial
created: 2023-01-11
modified: 2025-04-03T23:55:47
description: IntelliJ IDEA 简体中文专题教程
source: https://github.com/judasn/intellij-idea-tutorial
tags:
  - github/star
tags-link: 
type: repo
---
## Repo Meta

![](https://img.shields.io/github/stars/judasn/intellij-idea-tutorial?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/judasn/intellij-idea-tutorial?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/judasn/intellij-idea-tutorial?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=judasn&repo=intellij-idea-tutorial&bg_color=00000000)](https://github.com/judasn/intellij-idea-tutorial)

## Notes


## Contents
  - **特别地方**
    - [IntelliJ IDEA 编译方式介绍](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/make-introduce.md)
      - 虽然 IntelliJ IDEA 也支持通过设置开启实时编译，但是不建议，因为太占资源了
      - 多个类之间的关联关系还是要等 Make 或 Rebuild 触发的时候才会做相关检查的
      - 在 IntelliJ IDEA 里，一共有三种编译方式：
        - Compile：对选定的目标（Java 类文件），进行强制性编译，不管目标是否是被修改过。
          - 注：2018版操作为Recompile。
        - Rebuild：对选定的目标（Project），进行强制性编译，不管目标是否是被修改过，由于Rebuild 的目标只有 Project，所以 Rebuild 每次花的时间会比较长。
        - Make：使用最多的编译操作。对选定的目标（Project 或 Module）进行编译，但只编译有修改过的文件，没有修改过的文件不会编译
          - 这样平时开发大型项目才不会浪费时间在编译过程中。
          - 注：2018版操作为Build
      - 在容器运行之前配置上一个编译事件，先编译后运行。默认下 IntelliJ IDEA 也都是这样的设置，所以实际开发中你也不用太注意编译这件事
      - ![编译器的设置和选择](https://github.com/judasn/IntelliJ-IDEA-Tutorial/raw/9801bfb33946e041f8d579df06b22bf839e6fccf/images/xiii-c-compiler-setting-1.jpg)
      - 上图标注 2 所示，设置编译 heap 大小，默认是 700，建议使用 64 位的用户，在内存足够的情况下，建议改为 1500 或以上。如果你在编译的时候出错，报：OutOfMemoryError，一般也是要来改这个地方
      - 图标注 3 所示，还可以设置编译时的 VM 参数，这个你可以根据需求进行设置，一般人是用不上的。
      - ![编译器的设置和选择](https://github.com/judasn/IntelliJ-IDEA-Tutorial/raw/9801bfb33946e041f8d579df06b22bf839e6fccf/images/xiii-c-compiler-setting-2.jpg)
      - 如上图标注 1 所示，可以添加目录 或 文件进行编译排除。
        在项目中，如果有任何一个可编译的文件无法编译通过，则 IntelliJ IDEA 是无法运行起来的，必须等你全部问题解决，编译通过之后才可运行。但是可能开发过程中，某一个包目录的文件编译无法通过，但是我们又不急着改，那我们就可以考虑把该包加入到排除编译列表中，则项目就可以运行起来。
      - ![编译器的设置和选择](https://github.com/judasn/IntelliJ-IDEA-Tutorial/raw/9801bfb33946e041f8d579df06b22bf839e6fccf/images/xiii-c-compiler-setting-3.gif)
      - IntelliJ IDEA 支持常见的几种编译器：Javac(默认)、Eclipse、Ajc 等。
      - Project bytecode version 针对项目字节码编译版本，一般选择的是当前项目主 JDK 的版本
      - Per-module bytecode version 可以针对 Project 下各个 Module 的特殊需求单独设置不同的 bytecode version，前提是电脑上必须有安装对应的 JDK 版本
    - [IntelliJ IDEA 下项目相关特有概念说明](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/project-composition-introduce.md)
  - **必备的快捷键（新用户必看）**
    - [IntelliJ IDEA 项目相关的几个重要概念介绍](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/project-composition-introduce.md)
    - [IntelliJ IDEA 常用快捷键讲解（Win + Linux）](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/keymap-introduce.md)
    - [最特殊的快捷键 Alt + Enter 介绍](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/hotkey-alt-enter-introduce.md)
  - **提高编码效率功能介绍**
    - [Maven 设置](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/maven-project-introduce.md)
    - [IntelliJ IDEA 配合 Maven 的一些要点](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/maven-skill-introduce.md)
    - [前端代码模板：Emmet](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/emmet-introduce.md)
    - [特殊代码模板：Postfix Completion](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/postfix-completion-introduce.md)
    - [Debug 技巧](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/debug-introduce.md)
    - [重构技巧](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/refactor-introduce.md)
    - [数据库管理工具](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/database-introduce.md)
    - [远程调试介绍（Tomcat + Jetty）](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/remote-debugging.md)
  - **高级设置介绍**
    - [IntelliJ IDEA 推荐设置（新人重点）](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/settings-recommend-introduce.md)
    - [IntelliJ IDEA 常用细节-1](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/settings-introduce-1.md)
    - [IntelliJ IDEA 常用细节-2](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/settings-introduce-2.md)
    - [IntelliJ IDEA 常用细节-3](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/settings-introduce-3.md)
    - [IntelliJ IDEA 常用细节-4](https://github.com/judasn/IntelliJ-IDEA-Tutorial/blob/9801bfb33946e041f8d579df06b22bf839e6fccf/settings-introduce-4.md)
  - ...
-