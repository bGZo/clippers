---
created: 2024-06-05T12:00:00
source: https://www.qiyichao.cn/archives/18/
type: archive-web
modified: 2025-01-15T11:38:16
---

在过去，想发布一个 Linux 应用程序会带来很多问题：

  - 程序文件遍布整个系统
  - 需要复杂的代码来管理安装与更新
  - 操作不是事务性的（如果操作失败，对系统的影响仍然会保留）

如今，在 Ubuntu 中已经提供了解决这些问题的方案，这就是 Snap 与 Snapcraft（[https://snapcraft.io/](https://snapcraft.io/)）。它可以提高应用程序的发布频率，支持订阅渠道来控制用户风险级别（例如用户可以订阅测试版），即使发布更新失败也不需要用户参与。

Snap 同时也伴随着一些问题：

  - 理论上支持安装到任何操作系统，但目前还不支持 CentOS
  - 服务端是闭源的，需要通过 Snap 应用商店来发布你的应用，你无法运行一个私有的软件源

而 Ubuntu 自 16.04 版本开始内置了 Snap 应用程序，如果今天想发布一个 Linux 下的应用，Snap 可以算是一个还不错的方案。

Snap 应用程序的概念非常像移动应用程序：它由包含代码的 squashFS 只读文件系统和声明应用程序包信息的 snap.yaml 构成，并额外包括一个数据区域。

在 Snap 应用程序中，所有的依赖都会包含在应用程序包内，其他依赖的更新不会影响到你的应用程序，更新你的应用程序依赖也不会影响其他应用。如果你想使用一个权限，需要像开发 Android 应用程序一样声明所需的权限，与其他应用程序交换数据也需要用户授权，或根据系统默认设置来进行。

### 进一步了解

一般 Snap 在软件管理器中的包名是 snapd，例如在 Ubuntu 16.04 以前的版本中可以使用命令来安装：

```
  sudo apt install snapd
  ```

你也可以在 Snapcraft 的官方文档（[https://docs.snapcraft.io/core/install](https://docs.snapcraft.io/core/install)）中找到对应系统的安装命令。

在系统包含 Snap 后，可以安装 Snap 应用程序：

```
  snap install <snap name>
  ```

默认情况下，Snap 应用会被安装到 `/snap/<snap name>/<revision>/` 目录下。我们可以安装一个 Hello 应用：

```
  snap install hello
  ```

这样我们就可以运行这个应用。

```
  hello
  > Hello, world!
  - hello.universe
  > Hello, universe!
  ```

Snap 也可以支持后台运行的应用。

```
  # 启用一个应用
  snap enable <snap name>
  # 禁用一个应用，应用程序与后台服务将不再可用
  snap disable <snap name>
  ```

Snap 每天将会更新你所有的应用程序，你也可以手动更新。

```
  # 更新所有应用
  snap refresh
  # 更新指定应用程序
  snap refresh <snap name>
  # Snap 支持订阅频道，例如 stable，candidate，beta，edge
  # 可以这样更新一个应用程序，并切换频道
  snap refresh <snap name> --beta
  ```

结论：**Snap 不像 Docker 那样是为了复杂的企业级应用而存在，它解决了普通 Linux 用户安装应用复杂的问题，也解决了应用程序开发者发布应用的难题。**
