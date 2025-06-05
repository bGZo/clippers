---
created: 2024-02-24T12:00:00
source: https://www.zhihu.com/question/443835000/answer/1726902348
type: archive-web
modified: 2025-01-15T11:38:16
---

其实在 WSL 出现之后，Windows 逐步开放了大小写区分的支持

在 RS5 以上的系统里，可以用以下命令对某个目录打开/关闭 Win32 大小写区分支持，保存的是一个扩展属性

```shell
  fsutil.exe file setCaseSensitiveInfo <path> enable
  fsutil.exe file setCaseSensitiveInfo <path> disable
  ```

打开了之后，这个目录下就是大小写区分的了，所有 Win32 程序都会区分路径大小写

在以前的系统里，可以改注册表打开对 Win32 的全局的大小写区分支持
