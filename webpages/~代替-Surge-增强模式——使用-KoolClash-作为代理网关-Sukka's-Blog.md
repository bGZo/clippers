---
title: "代替-Surge-增强模式——使用-KoolClash-作为代理网关-Sukka's-Blog"
created: 2025-03-09T12:58:17
modified: 2025-03-09T12:58:17
description: "KoolClash 从一开始设计就是为了将 Clash 放在路由器或者网关设备上运行。在 Clash 0.14.0 版本推出 fake-ip 模式以后，KoolClash 实现了相对完善的代理网关。"
source: "https://blog.skk.moe/post/alternate-surge-koolclash-as-gateway/"
tags:
tags-link:
type: "archive-web"
---
KoolClash 从一开始设计就是为了将 Clash 放在路由器或者网关设备上运行。在 Clash 0.14.0 版本推出 `fake-ip` 模式以后，KoolClash 实现了相对完善的代理网关。

> 如果要了解 KoolClash 的工作机制，请参考我写的 [这篇文章](https://blog.skk.moe/post/how-koolclash-worked/)。

## TL; DR

在旁路网关上安装 KoolClash `0.17.1-beta` 及其更新版本，在启动 Clash 进程后，将需要连接 Clash 的设备的网关指向安装了 KoolClash 的旁路网关、并将 DNS 修改为 `198.19.0.1` 和 `198.19.0.2`。

## Clash DNS

Clash 支持各种规则组进行分流，包括基于 DOMAIN 的规则。当通过 SOCKS5 和 HTTP 时 Clash 可以直接获取连接域名；但是直接将 TCP 流量重定向到 Clash 的 `redir` 端口时不能直接获取到连接域名，因为根据 TCP/IP 协议的特性，Application 在创建连接时会先发出一个 DNS 请求获取目标 IP，然后直接向 IP 发起连接。Clash 内置了一个 DNS Server 以反查 TCP 连接的域名，用于解析域名规则。

Clash 在 ChinaDNS 思路的基础上设计了国内外 DNS 分流的方法——Clash DNS 的上游分为两组 `nameserver` 和 `fallback`。Clash 首先同时向两组中所有 DNS 发起解析请求，然后从 `nameserver` 中选取解析返回最快的 IP；如果这个 IP 不属于 `CN` 时则采用 `fallback` 组中解析返回最快的 IP。这个 IP 将会用于解析 IP 规则、或者在直连时使用。

对于匹配到规则、而且规则指定了使用代理，连接会被发往远端的代理服务器；代理服务器拿到的是 Host 不是 IP，所以代理服务器会在远端进行 DNS 解析，只有在 DIRECT（直连）中才会使用 Clash DNS 解析的 IP 进行连接。这意味着除非需要 DIRECT，大部分情况下 Clash DNS 不需要得到最正确或是最佳的结果（有时甚至可以是被污染的 IP）——因为 Clash DNS 目的是为了解析规则、得到的 IP（你的 Application 以为连接的 IP）和代理服务器实际连接的 IP 很可能是不一样的。

## `redir-host` 的问题

当 Clash DNS 以 `redir-host` 模式运行时，不仅需要反查域名解析分流规则，还需要把得到的 IP 返回给客户端、不论这个 IP 是否准确。虽然 Application 会认为自己要去连接到 Clash DNS 返回的 IP，但是 KoolClash 会把所有的连接使用 iptables 重定向到 Clash，一旦 Clash 将连接交给代理服务器、代理服务器会进行解析并拿到返回的内容。这不会影响任何正常上网、看视频，但在一些极端情况下会产生问题。比如在 Clash 的 [issues#95](https://github.com/Dreamacro/clash/issues/95) 中讨论的，YouTube 的会被 DNS 污染到 243 开头的 IP，Clash DNS 不能处理保留 IP 并将其返回，而部分应用程序（如 Chrome）拒绝连接这个 IP（`ERR_ADDRESS_UNREACHABLE`）。

抛开 DNS 污染的问题，Chrome 和 Firefox 浏览器有 `preconnect` 特性、在浏览器拿到 IP 以后会试图直接与这个 IP 进行 TCP 握手。虽然建立 TCP 握手的开销很小，但是由于 Clash DNS 返回的这个 IP 和代理服务器在远端解析的 IP 可能不一样、甚至对应 IP 规则和域名规则所使用的代理服务器也不同，最后会产生不必要的开销。

## `fake-ip` 来了

终于，Clash 在 0.14.0 版本推出了 `fake-ip` 模式。当 TCP 连接建立时，Clash DNS 会直接返回一个保留地址的 IP（即 Fake IP；Clash 默认使用 `198.18.0.0/16`，下文以此为例），同时 Clash 继续解析域名规则和 IP 规则。对于 KoolClash 来说，所有流量都被 iptables 转发给 Clash，Clash 会处理 Fake IP 额请求的域名之间的对应关系。  
而且如果 Clash DNS 匹配到了域名规则、则不需要向上游 DNS 请求，Clash 已经可以直接将连接发给代理服务器，节省了 Clash DNS 向上游 DNS 请求解析。Application 拿到的是 Clash DNS 返回的 Fake IP，所以也不会出现某些应用程序拒绝连接一些 IP 的情况；和 `redir-host` 模式一样，在大部分情况下 `fake-ip` 模式下也可以完全无视 DNS 污染。

## `fake-ip` 的问题

- 当 Clash 重启时，Fake IP 会重新从头开始分配；如果设备或软件缓存了 Clash 重启前解析的 Fake IP，可能会出现无法访问等问题。Clash 已经 dev 分支中将 TTL 修改为 1 以解决这个问题。
- 由于所有域名都被返回 Fake IP，意味着所有流量都必须经过 Clash 处理。这意味着使用 iptables 实现端口控制局域网 IP 绕行都会变得毫无意义。Clash 提供 `SRC-IP-CIDR` `SRC-PORT` 和 `DST-PORT`，有访问控制需求的用户需要自己编写 Clash 的配置文件。

## KoolClash 的 Fake DNS

KoolClash 之前将所有 DNS 请求通过 dnsmasq 全部转发给 Clash（Clash DNS 监听在 23453 端口上），结果在测试 `fake-ip` 时导致 Clash 在解析代理服务器的节点域名时都被解析到 Fake IP。  
KoolClash 通过 iptables 将所有 `198.19.0.0/24` 中 53 端口的流量转发到 23453 端口上，并要求用户将需要联网设备的 DNS 修改为 `198.19.0.1` 和 `198.19.0.2`。这样路由器内部直接使用 53 端口通过 dnsmasq 直接进行解析，外部连接的设备的 DNS 请求发往 `198.19.0.0/24` 的 53 端口而被 iptables 拦截转发给 Clash，从而将路由器内部的 DNS 解析和需要使用 Clash DNS 的解析分开。KoolClash 将 `198.19.0.0/24` 称为 Fake DNS。  
需要使用 KoolClash 的设备，除了需要将网关指向 KoolClash 所在的设备的 IP 以外，还需要修改 DNS 到 `198.19.0.1` 和 `198.19.0.2`；如果 DNS 依然指向网关，Clash 将不能解析域名规则，直连解析也可能会导致 DNS 污染；当停止使用 KoolClash 以后，需要还原设备的 DNS 设置。