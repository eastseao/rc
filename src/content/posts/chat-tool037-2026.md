---
title: "Codex Windows 中文设置"
description: "如果你说的是 OpenAI Codex Windows 桌面应用（Codex Desktop App），目前中文支持情况比较特殊。 方法一：在软件内设置（如果你的版本支持）1. 打开 Codex2. 点击 File → Settings3."
pubDatetime: 2026-06-14
category: "建站与技术"
kind: "长文"
tags: ["ChatGPT", "会话归档"]
---

## Q1 · codex windows 桌面应用怎么设置中文显示（第 1 轮对话）

> **提问：** codex windows 桌面应用怎么设置中文显示

如果你说的是**OpenAI Codex Windows 桌面应用（Codex Desktop App）**，目前中文支持情况比较特殊。

##### 方法一：在软件内设置（如果你的版本支持）

1. 打开 Codex

1. 点击 File → Settings

1. 进入 General

1. 找到 Language

1. 选择 中文（中国） / zh-CN

1. 完全退出 Codex （不是关闭窗口，而是退出后台进程）

1. 重新启动应用。citeturn0search6turn0search5

---

#### 如果设置了还是英文

这是目前 Windows 版比较常见的问题。

很多用户反馈：

- Language 已经改成 中文

- 配置文件也保存为 zh-CN

- 重启之后界面仍然是英文

这是官方已经确认的 Bug，目前还没有完全修复。citeturn0search3turn0search4turn0search2

---

#### 方法二：检查配置文件

可以看看

```
C:\Users\你的用户名\.codex\config.toml
```

是否有

```
[desktop]
localeOverride = "zh-CN"
```

或者

```
C:\Users\你的用户名\.codex\
```

里面的全局配置是否已经写入

```
"localeOverride": "zh-CN"
```

如果已经是`zh-CN`，但 UI 还是英文，那么基本就是当前版本的国际化没有生效。citeturn0search3turn0search2

---

#### 方法三：更新到最新版

官方一直在完善中文支持。

目前已经有不少版本修复了部分中文界面，但仍存在：

- 一级菜单中文

- 二级菜单英文

- 设置页部分英文

- Sidebar 部分英文

也就是说，目前**可能只能做到中英混合界面**。citeturn0search0turn0search4

---

#### 方法四：使用社区汉化（非官方）

GitHub 上已经有人做了完整汉化补丁。

不过：

- ✅ 中文最完整

- ❌ 属于第三方修改版本

- ❌ 更新官方版本后可能失效

- ❌ 存在一定安全和维护风险，需要自行评估。citeturn0search0

---

#### 我建议你先确认一下

请告诉我：

1. 你的 Codex 是哪个版本？ （Help → About）

1. 安装来源是哪里？

- Microsoft Store - OpenAI 官网 - GitHub Release

1. 现在是什么情况？

- 完全英文 - 部分中文、部分英文 - 没有 Language 选项

我可以根据你的版本告诉你是否支持中文，以及是否有对应的解决办法。
