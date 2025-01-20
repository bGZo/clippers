---
created: 2025-01-10T10:56:47
source: "https://www.ffutop.com/posts/2021-07-23-ssh-proxy/"
type: "archive-web"
modified: 2025-01-15T11:38:15
---

通常，SSH 被用于登录远程服务器，并且可以像使用本地控制台一样，在远程服务器上执行命令。它可以为两台非互信的服务器在公网环境下建立安全加密通信。基于这样的加密连接，以及数据转发能力，SSH 也就顺理成章地能作为代理。

## 正向代理

正向代理一般见于本地无法直接访问目标服务的场景，常见于防火墙或者内网服务等。比如由本地 `HostA` 发起的请求，无法经过公网访问的目标 `HostC` 监听的 `PortC` 端口服务。

![](https://img.ffutop.com/a6f4001a-ecea-4860-852e-a3b969aaa8c2.png)

这种场景下，那就在本地 `HostA` 监听端口 `PortA`，并把端口 `PortA` 监听到的数据全部基于 SSH 构建的隧道转发到目标服务器 `HostC` 的监听端口 `PortC` 上。

基于建立转发隧道的主体，有两种不同的方式。

```shell
# 方法 1
ssh -L 0.0.0.0:PortA:HostC:PortC user@HostC
# 方法 2
ssh -L 0.0.0.0:PortA:HostC:PortC user@HostB
```

![](https://img.ffutop.com/0bed48a4-511c-4c2e-a6cc-8cb142822bd5.png)

## 反向代理

反向代理与正向代理的链路正好相反，常见于内网穿透，将内网的服务暴露的一台绑定有公网 IP 的服务器上以供公开访问。

```bash
ssh -R HostC:PortC:HostA:PortA user@HostC
```

![](https://img.ffutop.com/032a15a1-9016-430b-9db9-4543e6a1aa2c.png)

从图上也可以看出来，建立的 SSH 隧道依然是由 HostA 发起，HostC 响应，但这是数据转发的方向刚好相反。

临时的内网穿透，用 ssh 特别合适，但受限于 sshd 的长时间无操作自动断开机制，建立的隧道总会中断。因此为了稳定的隧道质量，可以使用 `autossh` ，来保证自动重连。

## Socks5 代理

前面做的都是端口服务转发，如果目标服务不定，只是简单的转发流量，并代理服务的发起方，SSH 还能提供 SOCKS 服务。

```shell
ssh -D localhost:1080 HostC
```

让从本地 `HostA` 上面，发给 Socks5 代理 (`localhost:1080` ) 的流量，全部走 SSH 隧道到达服务器 `HostC` ，并“看似”像是从 `HostC` 向真实的目标发起的一样。也就是一种简易版的 SS/SSR 。

## More Advanced

为了更好用一点，还可以加上：`-CqTnN` 参数，比如：

```bash
$ ssh -CfNnqT -L 0.0.0.0:PortA:HostC:PortC user@HostB
# -C compression 压缩数据
# -f Requests ssh to go to background. 后台运行
# -N Do not execute a remote command. 禁止执行远程命令
# -n Redirects stdin from /dev/null. 关闭标准输入
# -q  Quiet mode. 安静模式
# -T Disable pseudo-terminal allocation. 禁止远程服务器分配虚拟终端
```
