---
title: "Lessica/TrollFools"
aliases: "TrollFools"
created: 2025-05-03T10:48:46
modified: 2025-05-03T15:36:49
description: "In-place tweak injection with insert_dylib and ChOma."
source: "https://github.com/Lessica/TrollFools"
tags:
  - "star"
tags-link:
type: "repo"
---

## Repo Meta

![](https://img.shields.io/github/stars/Lessica/TrollFools?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/Lessica/TrollFools?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/Lessica/TrollFools?style=for-the-badge&label=since)

[![](https://github-readme-stats.vercel.app/api/pin/?username=Lessica&repo=TrollFools&bg_color=00000000)](https://github.com/Lessica/TrollFools)

## Notes

### tipa 和 ipa 的区别是什么？ #deepseek

| 特性       | `.ipa`                        | `.tipa`       |
| -------- | ----------------------------- | ------------- |
| **签名要求** | 必须有效签名                        | 通常未签名或签名无效    |
| **分发场景** | App Store、合法侧载                | TrollStore 专用 |
| **兼容工具** | SideStore、AltStore、Sideloadly | 仅限 TrollStore |
| **文件内容** | 标准应用包                         | 可能包含脱壳/修改内容   |

### **1. `.ipa` 和 `.tipa` 的区别**
- **`.ipa` (iOS App Store Package)**
  这是 iOS 应用的标准分发格式，包含应用的二进制文件、资源、元数据和签名信息。所有通过 App Store 或合法渠道分发的应用均使用此格式。侧载工具（如 AltStore、Sideloadly、SideStore）依赖此格式，并要求文件包含有效的签名（开发者证书或企业证书）。

- **`.tipa` (TrollStore IPA)**
  这是为 **TrollStore**（巨魔商店）设计的特殊格式，通常用于绕过签名验证。`.tipa` 文件可能是以下两种形式之一：
  1. **未签名的 IPA**：移除了官方签名，依赖 TrollStore 的系统级漏洞（如 CoreTrust）直接安装。
  2. **脱壳或修改后的 IPA**：可能包含脱壳的二进制文件或其他破解内容，无需签名即可运行。

  **关键特性**：
  - 依赖 TrollStore 的漏洞绕过签名验证。
  - 通常无法通过传统侧载工具安装（如 SideStore），因为缺乏有效签名。

### **2. 为什么 TrollStore 支持 `.tipa` 而 SideStore 不支持？**
- **TrollStore 的工作原理**
  TrollStore 利用 iOS 系统的漏洞（如 CoreTrust），允许直接安装未签名或修改后的应用。它对 `.tipa` 的支持是通过绕过签名验证实现的，因此可以处理未签名或脱壳的 IPA 文件。

- **SideStore 的限制**
  SideStore 基于 AltStore 的机制，依赖以下两种合法方式安装应用：
  1. **个人开发者证书**：通过 Apple 开发者账号签名，每个应用需每 7 天续签。
  2. **企业证书或 WebClip 漏洞**（部分情况）。
  因此，SideStore 只能安装包含有效签名的 `.ipa` 文件。未签名或签名被破坏的 `.tipa` 文件无法通过验证，导致无法选中或安装。

### **3. 如何转换 `.tipa` 为 SideStore 可用的 `.ipa`？**

若需在 SideStore 中安装 `.tipa` 文件，需确保其包含有效签名。以下是可能的步骤：

1. **重新签名工具**：使用工具（如 `iOS App Signer`、`Sideloadly`）对 `.tipa` 文件重新签名。
   - 若原 `.tipa` 已脱壳或修改，需确保二进制文件未加密且兼容签名。
   - 使用个人开发者证书或企业证书签名后，保存为 `.ipa` 格式。
   - 
2. **直接获取已签名的 IPA**：
   从可信来源获取已签名且未修改的 `.ipa` 文件（如官方应用或未破解版本）。
