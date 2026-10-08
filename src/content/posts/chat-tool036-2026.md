---
title: "Mindmap库推荐"
description: "如果你的目标不是集成一个思维导图库，而是做一个媲美 XMind、ProcessOn、幕布 的 Windows 桌面应用，那我建议不要只找一个库，而是参考成熟项目 + 核心渲染库 + 图形引擎。我按照推荐指数给你排一下。--- ⭐⭐⭐⭐⭐ 第"
pubDatetime: 2026-06-13
category: "建站与技术"
kind: "长文"
tags: ["ChatGPT", "会话归档"]
---

## Q1 · 给我推荐github里关于mindmap的库，我想做一个mindmap应用，wi…（第 1 轮对话）

> **提问：** 给我推荐github里关于mindmap的库，我想做一个mindmap应用，windows端

如果你的目标不是**集成一个思维导图库**，而是**做一个媲美 XMind、ProcessOn、幕布 的 Windows 桌面应用**，那我建议不要只找一个库，而是参考**成熟项目 + 核心渲染库 + 图形引擎**。

我按照推荐指数给你排一下。

---

# ⭐⭐⭐⭐⭐ 第一梯队（最值得研究）

#### 1. BlinkMind ⭐⭐⭐⭐⭐（我最推荐）

> 如果我是从零开始开发，我会首先研究它。

**Github**

- urlBlinkMind Desktophttps://github.com/awehook/blink-mind-desktop

- urlBlinkMind Reacthttps://github.com/awehook/react-mindmap

特点

✅ React

✅ TypeScript

✅ Electron

✅ 完整桌面应用

支持：

- 节点编辑

- 拖拽

- Undo/Redo

- 多Sheet

- 导出图片

- Shortcut

- Theme

- 富文本

- Markdown

基本就是一个开源版 XMind。

里面很多设计值得借鉴。citeturn0search0turn0search1

---

#### 优点

架构非常漂亮：

```
Electron

    │

React

    │

BlinkMind Engine

    │

Renderer

    │

Document
```

Document 与 UI 完全分离。

以后接 AI 很方便。

---

# ⭐⭐⭐⭐⭐ 2. jsMind

Github

> urljsMindhttps://github.com/hizzgdev/jsmind

Star：

约3800+

属于目前最经典的 MindMap Library。

特点：

- Canvas

- SVG

- 无框架依赖

- API 简洁

- 性能不错

支持：

✅ 编辑

✅ 拖拽

✅ 折叠

✅ 导出

✅ 自定义节点

很多国产项目都参考过它。citeturn0search3

---

适合：

如果你自己写 Windows 软件，

jsMind 可以直接作为渲染引擎。

---

# ⭐⭐⭐⭐⭐ 3. Mind Elixir

Github

> urlMind Elixirhttps://github.com/ssshooter/mind-elixir-core

这是近几年评价非常高的一套。

优点：

UI 很现代。

支持：

- 无限缩放

- Drag

- Keyboard

- Rich Text

- SVG

- Theme

代码质量比 jsMind 更现代。

---

它最大的优点：

布局算法比较优秀。

---

# ⭐⭐⭐⭐⭐ 4. Open MindMap

Github

> urlOpen MindMaphttps://github.com/XiangFaGitHub/open-mindmap

这是一个比较新的项目。

特点：

AI Native。

支持：

- Markdown

- 实时生成

- React

- SVG

- Streaming

以后如果要：

> AI 自动生成思维导图

它很值得研究。citeturn0search2

---

# ⭐⭐⭐⭐ 5. Remind

Github

> urlRemindhttps://github.com/luvsic3/remind

React 写的。

特点：

- Undo

- Redo

- Shortcut

- Drag

- 编辑

UI 比 BlinkMind 简洁。

适合学习源码。citeturn0search6turn0reddit23

---

# ⭐⭐⭐⭐ 6. drichard/mindmaps

Github

> urlmindmapshttps://github.com/drichard/mindmaps

老牌项目。

HTML5。

支持离线。

虽然代码偏旧，但架构值得参考。citeturn0search8

---

# 如果你想做商业级 Windows 软件

我建议直接使用下面这一套技术。

```
Electron

        +

React 19

        +

TypeScript

        +

ReactFlow

        +

ELK.js

        +

Y.js

        +

Zustand

        +

Slate / Lexical

        +

Tauri（未来可替换）
```

---

#### 为什么我推荐 ReactFlow？

虽然它不是 MindMap。

但是：

XMind

FlowUs

飞书

很多 AI Diagram

其实都是：

Graph Editor。

ReactFlow：

支持：

- 无限画布

- 节点

- Edge

- MiniMap

- Zoom

- Selection

- Drag

- ContextMenu

这些都是免费的。

然后：

你只需要：

把布局算法改成：

```
Tree Layout
```

就变成 MindMap。

---

#### 再配 ELK.js

```
用户输入

↓

Tree

↓

ELK

↓

计算坐标

↓

ReactFlow

↓

显示
```

布局质量会非常高。

---

# 如果以后接 AI

推荐：

```
LLM

↓

Markdown

↓

AST

↓

MindMap JSON

↓

ReactFlow

↓

MindMap
```

以后：

一句话：

> 帮我生成一个 Windows Agent 的开发架构

直接：

```
LLM

↓

JSON

↓

MindMap
```

无需任何人工拖节点。

---

# 我如果做一个 2026 年的 AI MindMap，会采用的完整技术栈

| 模块 | 推荐方案 | 推荐指数 |
|---|---|---|
| UI | React 19 | ⭐⭐⭐⭐⭐ |
| Desktop | Electron（或后续迁移 Tauri） | ⭐⭐⭐⭐⭐ |
| Canvas | ReactFlow | ⭐⭐⭐⭐⭐ |
| Layout | ELK.js | ⭐⭐⭐⭐⭐ |
| State | Zustand | ⭐⭐⭐⭐⭐ |
| RichText | Lexical | ⭐⭐⭐⭐⭐ |
| History | Immer + Zustand | ⭐⭐⭐⭐⭐ |
| AI | OpenAI / Claude / Gemini | ⭐⭐⭐⭐⭐ |
| Storage | SQLite + IndexedDB | ⭐⭐⭐⭐⭐ |
| Sync | Y.js + CRDT | ⭐⭐⭐⭐⭐ |
| Plugin | Plugin API | ⭐⭐⭐⭐⭐ |

---

# 📌 我的建议（如果你的目标是做「Windows 端 AI 思维导图应用」）

**不要直接基于 BlinkMind 二次开发，而是把它作为参考。**

最佳路线是：

- 🧩 学习 BlinkMind 的数据模型和交互设计

- 🎨 采用 ReactFlow 作为底层画布引擎

- 🌲 使用 ELK.js（或 Dagre）实现自动树布局

- 🤖 从第一天开始 设计 AI Native 架构（JSON ↔ Markdown ↔ MindMap 双向转换）

- 🔌 预留插件系统 、命令系统（Command Pattern）、事件总线和 CRDT 协作能力

这样做出来的产品，扩展性和长期维护性会明显优于基于传统 MindMap 库的方案，也更适合未来加入 AI 自动生成、知识图谱、Agent 协同等能力。🚀
