---
title: Fusion RSS 阅读器 v0.9.3：全新 UI、快捷键、i18n 等 - V2EX
created: 2025-03-29T22:01:49
modified: 2025-03-29T22:02:10
source: https://www.v2ex.com/t/1121836
tags: 
tags-link:
  - "[[0x2E-fusion]]"
type: archive-web
---

## Origin Content

Hi 朋友们！最近为 Fusion 添加了多个社区呼声很高的功能，分享一下 :D

[Fusion](https://github.com/0x2E/fusion) 是一个轻量、自托管友好的 RSS 阅读器。主要功能和特点有：

- 分组、书签、订阅源自动嗅探、OPML 导入导出
- 响应式、PWA 、暗色模式、快捷键、i18n
- 轻量、易部署
- 只需要一个二进制文件就能部署，也有预构建的 Docker image
- 后端使用 Go + SQLite ，没有其他组件依赖
- 前端使用 SvelteKit 并打包为 SPA 嵌入后端二进制文件中
- 内存占用约 90MB

最近的新变化：

- **新 UI**
- 重新设计为双栏布局，空间利用率更高
- 组件库从 shadcn/ui 换为了 daisyui ，减少 JS 依赖，尽可能利用 HTML 原生能力。打包体积减少了 30%
- 优化了页面加载速度
- **快捷键**。设置了一些类似 Google Reader 和 Feedly 的快捷键。按下 `?` 可以打开快捷键提示
- **i18n**。添加了中、西、德等语言
- \*\* 后端健壮性 ++\*\*。感谢 mtlynch 做了许多代码优化和单测

欢迎大家体验，项目地址： [https://github.com/0x2E/fusion](https://github.com/0x2E/fusion) 。

## Comment



