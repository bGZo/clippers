---
title: "pypa/pipx"
aliases: "pipx"
created: 2025-02-22T13:53:52
modified: 2025-02-22T13:59:37
description: "Install and Run Python Applications in Isolated Environments"
source: "https://github.com/pypa/pipx"
tags:
  - "github/star"
tags-link:
type: "repo"
---

## Meta

![](https://img.shields.io/github/stars/pypa/pipx?style=for-the-badge&label=stars) ![](https://img.shields.io/github/repo-size/pypa/pipx?style=for-the-badge&label=size) ![](https://img.shields.io/github/created-at/pypa/pipx?style=for-the-badge&label=since)

## Notes

### 环境隔离原理 #chatGPT

1. **每个应用独立的虚拟环境**：pipx 在 ~/.local/pipx/venvs/ 目录下为每个安装的应用创建一个独立的 **virtualenv**（Python 虚拟环境）。这样，每个工具的依赖不会相互影响，避免了 Python 依赖冲突。
2. **使用 python -m venv**：pipx 依赖 venv 模块创建独立的 Python 虚拟环境，而不是全局安装工具。这类似于 virtualenv，但 venv 是 Python 自带的模块。
3. **只暴露 CLI 命令**：pipx 只会将虚拟环境中的可执行文件（通常在 venv/bin/ 目录下）链接到 ~/.local/bin/，而不会污染全局 site-packages。这样，工具的 Python 运行环境是隔离的，但用户可以像全局安装一样直接运行 CLI 命令。
4. **自动管理 Python 版本**：pipx 允许使用不同的 Python 版本运行工具，比如 pipx install --python python3.9 some-tool，这样可以确保工具使用指定的 Python 版本，不受系统 Python 版本变化的影响。
5. **支持临时运行 (run 命令)**：pipx run some-tool 会在临时目录中创建一个虚拟环境，并在执行后自动删除，确保不污染已有环境。

### 运行 ` pipx install ` 会自动创建 Venv 环境 #chatGPT 

1. **检查是否已有 venv**（默认在 ~/.local/pipx/venvs/some-tool/）：
    1. 如果 venv 已存在，则直接使用。
    2. 如果 venv 不存在，pipx 会 **自动创建一个独立的虚拟环境**。
2. **在 venv 里安装 some-tool**（使用 pip install）。
3. **将 some-tool 的可执行文件**（venv/bin/some-tool）**链接到 ~/.local/bin/**，方便你在终端直接运行 some-tool。
### Run under [[proxy]]

https://github.com/pypa/pipx/issues/669