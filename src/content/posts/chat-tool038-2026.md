---
title: "GitHub开源思维导图软件"
description: "如果你的目标是开发一款 Windows 思维导图软件，我建议不要只看 Star 数，而是看以下几个维度：- ✅ 是否还在持续维护- ✅ 是否支持大规模节点- ✅ 是否支持插件- ✅ 是否容易二次开发- ✅ 是否支持 Markdown- ✅"
pubDatetime: 2026-06-18
category: "建站与技术"
kind: "长文"
tags: ["ChatGPT", "会话归档"]
---

## Q1 · github上开源的思维导图软件（第 1 轮对话）

> **提问：** github上开源的思维导图软件

如果你的目标是**开发一款 Windows 思维导图软件**，我建议不要只看 Star 数，而是看以下几个维度：

- ✅ 是否还在持续维护

- ✅ 是否支持大规模节点

- ✅ 是否支持插件

- ✅ 是否容易二次开发

- ✅ 是否支持 Markdown

- ✅ License 是否允许商业使用

下面按照不同技术路线推荐。

---

# 一、目前 GitHub 最优秀的 MindMap 开源项目（推荐指数★★★★★）

#### 1. entity["software","SimpleMindMap","GitHub project"] ⭐⭐⭐⭐⭐（国内最火）

**Github**

https://github.com/wanglin2/mind-map

image_group{"query":["SimpleMindMap GitHub screenshot","SimpleMindMap editor interface","SimpleMindMap node styles","SimpleMindMap markdown import"]}

##### Star

约8k+

##### 技术

- TypeScript

- SVG

- Canvas

- Vue3

特点

✅ 非常漂亮

✅ 插件化

✅ 节点样式丰富

✅ 导出 PDF

✅ 导出 PNG

✅ 导出 SVG

✅ Markdown

✅ 大纲模式

✅ 协同基础

支持：

- Fishbone

- Timeline

- Logic Chart

- Organization Chart

- MindMap

这是目前国内做得最完整的一套。

适合：

⭐⭐⭐⭐⭐

如果你准备开发自己的产品，我最推荐直接 Fork。

---

# 2. entity["software","Mind Elixir","GitHub project"] ⭐⭐⭐⭐⭐

Github

https://github.com/ssshooter/mind-elixir-core

image_group{"query":["Mind Elixir GitHub demo","Mind Elixir editor UI","Mind Elixir draggable nodes","Mind Elixir example mind map"]}

特点：

非常轻量

纯 TS

API 非常简单

几十 KB

支持：

- Undo

- Drag

- Zoom

- History

- Keyboard

适合：

作为自己软件的核心引擎。

---

# 3. entity["software","jsMind","GitHub project"] ⭐⭐⭐⭐⭐

Github

https://github.com/hizzgdev/jsmind

image_group{"query":["jsMind demo screenshot","jsMind example mind map","jsMind node editing","jsMind GitHub"]}

这是经典中的经典。

十几年历史。

很多国产软件都是参考它。

优点：

API 非常成熟

稳定

学习资料多

---

# 4. entity["software","Markmap","GitHub project"] ⭐⭐⭐⭐⭐

Github

https://github.com/markmap/markmap

image_group{"query":["Markmap markdown mind map","Markmap demo","Markmap live editor","Markmap GitHub"]}

最大的特点：

Markdown 自动生成思维导图。

例如：

```
# AI

## ChatGPT

### GPT5

### Agent

## Claude

## Gemini
```

直接生成：

```
AI
 ├──ChatGPT
 │      ├──GPT5
 │      └──Agent
 ├──Claude
 └──Gemini
```

很多知识库都在用。

---

# 5. entity["software","Minder","GitHub project"] ⭐⭐⭐⭐

Github

https://github.com/fex-team/kityminder

image_group{"query":["KityMinder editor screenshot","KityMinder demo","Baidu KityMinder","KityMinder GitHub"]}

百度出品。

特点：

功能非常完整。

支持：

- 富文本

- 大纲

- Markdown

- 导图

---

# 二、桌面软件（Electron）

#### 6. entity["software","Freeplane","Mind mapping software"]

image_group{"query":["Freeplane screenshot","Freeplane UI","Freeplane mind map example","Freeplane desktop"]}

Java

历史悠久。

非常成熟。

插件很多。

---

#### 7. entity["software","FreeMind","Mind mapping software"]

经典鼻祖。

很多软件都是它演变来的。

---

# 三、真正可以参考源码的大型项目

#### 8. entity["software","Xmind","Open-source legacy edition"]（旧版本）

以前 XMind 开源过：

GitHub：

https://github.com/xmindltd/xmind

可以学习：

- 文件格式

- UI

- 导出

- 导图布局

不过最新版已经闭源。

---

# 四、支持 Markdown 的

| 项目 | Markdown | 双向编辑 |
|---|---|---|
| entity["software","Markmap","GitHub project"] | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| entity["software","SimpleMindMap","GitHub project"] | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| entity["software","Minder","GitHub project"] | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

# 五、支持无限画布（Infinite Canvas）

目前比较先进的是：

- entity["software","tldraw","Open-source whiteboard"]

- entity["software","Excalidraw","Open-source whiteboard"]

- entity["software","Affine","Knowledge workspace"]

- entity["software","AppFlowy","Open-source workspace"]

它们不是纯 MindMap。

但是：

无限画布 + 思维导图

已经成为未来趋势。

---

# 六、如果你想做 Windows AI 思维导图软件，我推荐的技术栈

```
UI
│
├── React
├── TypeScript
├── Tailwind
├── Electron
│
Canvas
│
├── SimpleMindMap
│
AI
│
├── OpenAI
├── Claude
├── Gemini
│
Storage
│
├── SQLite
├── IndexedDB
│
Document
│
├── Markdown
├── PDF
├── DOCX
│
Plugin
│
├── MCP
├── Plugin API
│
Sync
│
├── Git
├── WebDAV
├── OneDrive
```

这是目前比较适合打造生产级桌面思维导图应用的一套组合。

---

# 七、如果目标是打造「媲美 XMind / GitMind / ProcessOn」的产品，我最推荐研究这几个项目

| 排名 | 项目 | 推荐指数 | 适合作为内核 |
|---|---|---|---|
| 🥇 | entity["software","SimpleMindMap","GitHub project"] | ⭐⭐⭐⭐⭐ | ✅ 最推荐 |
| 🥈 | entity["software","Mind Elixir","GitHub project"] | ⭐⭐⭐⭐⭐ | ✅ 轻量高性能 |
| 🥉 | entity["software","jsMind","GitHub project"] | ⭐⭐⭐⭐☆ | ✅ 稳定成熟 |
| 4 | entity["software","Markmap","GitHub project"] | ⭐⭐⭐⭐☆ | ✅ Markdown 导图 |
| 5 | entity["software","Minder","GitHub project"] | ⭐⭐⭐⭐☆ | ✅ 富文本编辑 |
| 6 | entity["software","tldraw","Open-source whiteboard"] | ⭐⭐⭐⭐⭐ | ✅ 无限画布能力 |
| 7 | entity["software","Excalidraw","Open-source whiteboard"] | ⭐⭐⭐⭐☆ | ✅ 白板融合 |
| 8 | entity["software","Affine","Knowledge workspace"] | ⭐⭐⭐⭐⭐ | ✅ 知识管理与导图结合 |

**结合你之前提到的目标（开发一款 Windows 桌面 AI 思维导图应用）**，我会建议采用：

- 导图引擎 ：entity["software","SimpleMindMap","GitHub project"]

- 无限画布 ：参考 entity["software","tldraw","Open-source whiteboard"] 的架构设计

- 桌面框架 ：Electron + React + TypeScript

- AI 能力 ：接入多模型（OpenAI、Claude、Gemini），实现 AI 一键生成导图、导图总结、知识拆解、文档转导图等功能。

这条路线既能快速构建 MVP，也为后续扩展插件、协作、知识库等高级功能预留了足够空间。
