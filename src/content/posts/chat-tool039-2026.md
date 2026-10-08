---
title: "GitHub Typora 项目"
description: "如果你是在找 GitHub 上和 Typora 相关的项目，可以参考下面这些。 官方 GitHub 1. Typora 官方组织（⭐推荐）GitHub：urltypora organizationturn0search0里面主要包含"
pubDatetime: 2026-06-19
category: "建站与技术"
kind: "长文"
tags: ["ChatGPT", "会话归档"]
---

## Q1 · github里typora（第 1 轮对话）

> **提问：** github里typora

如果你是在找**GitHub 上和 Typora 相关的项目**，可以参考下面这些。

#### 官方 GitHub

##### 1. Typora 官方组织（⭐推荐）

**GitHub：**urltypora organizationturn0search0

里面主要包含：

| 仓库 | 用途 |
|---|---|
| urltypora-issuesturn0search2 | Bug 提交、功能建议（不是源码） |
| urltheme.typora.iohttps://github.com/typora/theme.typora.io | 官方主题网站源码 |
| urlTypora-i18nhttps://github.com/typora/Typora-i18n | 多语言翻译 |
| urltypora-default-themeshttps://github.com/typora/typora-default-themes | Typora 默认主题 |
| urltypora-theme-toolkithttps://github.com/typora/typora-theme-toolkit | 主题开发工具 |

---

#### Typora 是否开源？

**答案：不是。**

Typora 是一款**商业闭源软件**，GitHub 上**没有 Typora 的源代码**，官方仓库主要用于：

- Bug 收集

- 用户讨论

- 官方主题

- 国际化

- 一些辅助工具

官方也明确说明**Typora 并非开源软件**。citeturn0search2

---

# 如果你想开发一个 Typora 类应用（推荐）

结合你之前说过想开发**Windows Markdown / MindMap 应用**，下面这些开源项目更值得研究。

| 项目 | 特点 | 推荐指数 |
|---|---|---|
| urlMarkTexthttps://github.com/marktext/marktext | 开源，最像 Typora，Electron | ⭐⭐⭐⭐⭐ |
| urlZettlrhttps://github.com/Zettlr/Zettlr | 学术写作，非常成熟 | ⭐⭐⭐⭐ |
| urlghostwriterhttps://github.com/KDE/ghostwriter | Qt 编写，性能优秀 | ⭐⭐⭐⭐ |
| urlObsidian Sample Pluginhttps://github.com/obsidianmd/obsidian-sample-plugin | 如果要兼容 Obsidian 插件生态 | ⭐⭐⭐⭐ |

其中**MarkText**被广泛认为是最接近 Typora 使用体验的开源替代品。citeturn0search8turn0reddit13

---

# 如果你的目标是做一个「比 Typora 更强」的 Windows Markdown 编辑器

建议直接研究以下几个项目的架构：

1. MarkText （编辑器内核）

1. Obsidian （插件系统、知识库）

1. Logseq （双向链接）

1. Zettlr （文档管理）

1. VS Code （命令系统、扩展架构）

然后融合以下能力：

- ✨ Typora 的实时 WYSIWYG 编辑

- 🧠 Obsidian 的双向链接与知识图谱

- 🧩 VS Code 的插件生态

- 📝 AI 写作（GPT、Claude、Gemini）

- 🎨 Mermaid、PlantUML、思维导图

- 📄 导出 PDF、Word、HTML、EPUB

- ☁️ Git + WebDAV + OneDrive 同步

- 🤖 MCP + Agent 自动写作与排版

这会比单纯复刻 Typora 更有竞争力。

如果你的目标是**自己开发 Windows 版 Typora**，我还可以给你整理一份**GitHub 上 50 个最值得参考的 Markdown 编辑器与相关库**（按编辑器、渲染器、Markdown 引擎、AI、插件系统、导出模块等分类），方便直接作为技术选型参考。

## Q2 · 整理一份 GitHub 上 50 个最值得参考的 Markdown 编辑器与相关…（第 2 轮对话）

> **提问：** 整理一份 GitHub 上 50 个最值得参考的 Markdown 编辑器与相关库

如果你的目标是开发一款**产品级 Windows Markdown 编辑器**（结合我们之前讨论的 Typora + MarkItDown + KillerPDF + SimpleMindMap），那么建议不要只研究 Markdown 编辑器，而是研究整个生态。

下面这**50 个 GitHub 优质项目**，基本覆盖了 Markdown 编辑器开发所需的主要技术。

---

# 一、Markdown 编辑器（⭐⭐⭐⭐⭐ 必看）

| 项目 | 技术 | 推荐 |
|---|---|---|
| entity["company","MarkText","GitHub open-source Markdown editor"] | Electron + Vue | ⭐⭐⭐⭐⭐ |
| entity["company","Zettlr","Markdown editor project"] | Electron | ⭐⭐⭐⭐⭐ |
| entity["company","ghostwriter","KDE Markdown editor"] | Qt | ⭐⭐⭐⭐ |
| entity["company","Apostrophe","GNOME Markdown editor"] | GTK | ⭐⭐⭐ |
| entity["company","Abricotine","Markdown editor"] | Electron | ⭐⭐⭐ |
| entity["company","Remarkable","Markdown editor"] | Electron | ⭐⭐⭐ |
| entity["company","Notable","Note-taking app"] | Electron | ⭐⭐⭐⭐ |
| entity["company","Laverna","Open-source note app"] | Web | ⭐⭐⭐ |
| entity["company","Boost Note","Developer note app"] | Electron | ⭐⭐⭐⭐ |
| entity["company","QOwnNotes","Qt note-taking app"] | Qt | ⭐⭐⭐⭐ |

---

# 二、Markdown 解析器

| 项目 | 用途 |
|---|---|
| entity["company","markdown-it","Markdown parser"] | VuePress、VitePress 使用 |
| entity["company","remark","Markdown processor"] | Unified 生态 |
| entity["company","rehype","HTML processor"] | HTML AST |
| entity["company","CommonMark","Markdown specification"] | Markdown 标准 |
| entity["company","micromark","Markdown parser"] | 新一代解析器 |
| entity["company","marked","Markdown parser"] | 老牌解析器 |
| entity["company","flexmark-java","Java Markdown parser"] | Java 生态 |
| entity["company","goldmark","Go Markdown parser"] | Go 生态 |

---

# 三、编辑器内核（重点）

| 项目 | 用途 |
|---|---|
| entity["company","CodeMirror","Code editor"] | Obsidian 使用 |
| entity["company","Monaco Editor","VS Code editor"] | VS Code 内核 |
| entity["company","Lexical","Meta editor framework"] | Meta 出品 |
| entity["company","ProseMirror","Rich text editor"] | 富文本 |
| entity["company","Slate","Rich text framework"] | React |
| entity["company","Tiptap","Headless editor"] | 基于 ProseMirror |
| entity["company","Milkdown","Markdown editor framework"] | Markdown + ProseMirror |
| entity["company","Toast UI Editor","Markdown/WYSIWYG editor"] | 双模式编辑 |

---

# 四、知识管理（必须研究）

| 项目 | 推荐 |
|---|---|
| entity["company","Logseq","Knowledge management app"] | ⭐⭐⭐⭐⭐ |
| entity["company","SiYuan","Block-based note app"] | ⭐⭐⭐⭐⭐ |
| entity["company","Trilium Notes","Hierarchical notes"] | ⭐⭐⭐⭐ |
| entity["company","Joplin","Open-source note app"] | ⭐⭐⭐⭐⭐ |
| entity["company","AFFiNE","Knowledge workspace"] | ⭐⭐⭐⭐⭐ |
| entity["company","AppFlowy","Collaborative workspace"] | ⭐⭐⭐⭐⭐ |
| entity["company","SilverBullet","Markdown notebook"] | ⭐⭐⭐⭐ |

---

# 五、Mermaid / 图表

| 项目 |
|---|
| entity["company","Mermaid","Diagram library"] |
| entity["company","PlantUML","UML tool"] |
| entity["company","Excalidraw","Whiteboard"] |
| entity["company","draw.io","Diagram editor"] |
| entity["company","Graphviz","Graph visualization"] |

---

# 六、思维导图（与你的项目高度相关）

| 项目 |
|---|
| entity["company","SimpleMindMap","Mind map library"] |
| entity["company","Mind Elixir","Mind map"] |
| entity["company","jsMind","Mind map"] |
| entity["company","KityMinder","Baidu mind map"] |
| entity["company","XMind SDK","Mind map SDK"] |

---

# 七、PDF / Office

| 项目 |
|---|
| entity["company","MarkItDown","Document conversion"] |
| entity["company","PDF.js","PDF renderer"] |
| entity["company","LibreOffice","Office suite"] |
| entity["company","Pandoc","Universal document converter"] |
| entity["company","Mammoth.js","DOCX to HTML"] |

---

# 八、AI 编辑器生态

| 项目 |
|---|
| entity["company","Open WebUI","AI interface"] |
| entity["company","AnythingLLM","Local AI workspace"] |
| entity["company","Continue","AI coding assistant"] |
| entity["company","OpenHands","AI software engineer"] |
| entity["company","LobeChat","AI chat platform"] |

---

# 九、最值得深入研究的 Top 10 ⭐⭐⭐⭐⭐

如果时间有限，建议优先阅读这 10 个项目：

1. MarkText（Typora 开源替代）

1. Joplin（成熟桌面笔记）

1. AFFiNE（无限画布 + 文档）

1. AppFlowy（Notion 替代）

1. SiYuan（块编辑器）

1. Logseq（知识图谱）

1. Milkdown（Markdown 编辑框架）

1. CodeMirror（编辑器内核）

1. MarkItDown（Office/PDF 转 Markdown）

1. SimpleMindMap（思维导图）

---

#### 针对你的应用，我建议的技术组合 🏗️

结合你之前规划的「知识工作台」，我会采用如下架构：

- Markdown 编辑器 ：Milkdown + CodeMirror 6

- Markdown 解析 ：markdown-it + remark

- 文档导入 ：MarkItDown

- PDF 能力 ：PDF.js + KillerPDF

- 思维导图 ：SimpleMindMap

- 知识库 ：SQLite + 文件树索引

- 桌面框架 ：Rust + Tauri（Windows 原生体验）

- AI 能力 ：MCP + 多模型（OpenAI、Claude、Gemini 等）

- 数据存储 ：SQLite + Markdown 文件

这套组合兼顾性能、扩展性和长期维护性，也与你目前规划的产品方向高度契合。

## Q3 · 我会出一个windows端和安卓端 ，请给我提供新的技术组合（第 3 轮对话）

> **提问：** 我会出一个windows端和安卓端 ，请给我提供新的技术组合

如果你的目标已经升级为：

> **一个产品，同时支持 Windows + Android，并且未来还能扩展 macOS、Linux、Web。**

那么我的建议会和之前完全不同。

**不要再围绕 Typora 去设计。**Typora 的架构已经偏传统，并不适合跨平台统一开发。

---

# 推荐方案（2026）

#### 总体架构

```
                AI Service
        GPT / Claude / Gemini / Ollama
                    │
────────────────────┼────────────────────
                Rust Core Engine
────────────────────┼────────────────────
 Markdown │ PDF │ Office │ MindMap │ Search
 Index    │ OCR │ Parser │ Sync    │ Export
────────────────────┼────────────────────
            Flutter Desktop/UI
────────────────────┼────────────────────
 Windows     Android
 （以后直接支持 macOS / Linux / iOS）
```

核心思想：

> **UI 一套，核心引擎一套。**

Flutter 做所有界面。

Rust 做所有业务。

Android、Windows 共用 95% 以上代码。

---

# 推荐技术栈（⭐⭐⭐⭐⭐）

| 模块 | 推荐技术 | 推荐指数 |
|---|---|---|
| UI | Flutter 3.x | ⭐⭐⭐⭐⭐ |
| 状态管理 | Riverpod | ⭐⭐⭐⭐⭐ |
| 路由 | GoRouter | ⭐⭐⭐⭐⭐ |
| 本地数据库 | SQLite (Drift) | ⭐⭐⭐⭐⭐ |
| 全文搜索 | Tantivy（Rust） | ⭐⭐⭐⭐⭐ |
| Markdown Parser | markdown-it-rs 或 pulldown-cmark | ⭐⭐⭐⭐⭐ |
| Markdown 编辑 | Flutter Markdown + 自定义编辑器 | ⭐⭐⭐⭐⭐ |
| PDF | PDFium + PDF.js（按平台） | ⭐⭐⭐⭐⭐ |
| Office 导入 | MarkItDown | ⭐⭐⭐⭐⭐ |
| OCR | PaddleOCR / Tesseract | ⭐⭐⭐⭐ |
| 思维导图 | SimpleMindMap（WebView）或 Rust 原生数据模型 | ⭐⭐⭐⭐⭐ |
| AI | MCP + OpenAI Compatible API | ⭐⭐⭐⭐⭐ |
| 同步 | WebDAV + OneDrive + Git | ⭐⭐⭐⭐⭐ |

---

# 为什么不用 Electron？

| Flutter | Electron |
|---|---|
| Windows⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Android⭐⭐⭐⭐⭐ | ❌ |
| 内存占用低 | 高 |
| GPU渲染 | 是 |
| 动画流畅 | 是 |
| 安装包小 | 大 |
| 手机支持 | 原生 |

如果未来有 Android：

**Flutter 几乎没有对手。**

---

# 编辑器怎么做？

不要直接使用现成编辑器。

建议自己做。

采用

```
Markdown AST
        │
────────┼────────
Source Text
Preview Widget
Outline
MindMap
Knowledge Graph
```

所有功能共享同一棵 AST。

以后：

- Markdown

- 思维导图

- 大纲

- PDF导出

全部同步。

---

# 文档引擎

建议：

```
Rust
```

负责：

```
Markdown解析

Mermaid

PlantUML

PDF解析

Word解析

Excel解析

PPT解析

OCR

全文索引

标签

数据库

AI调用
```

Flutter 永远只负责：

```
界面

动画

交互
```

---

# 思维导图

不要把思维导图当成一个独立模块。

建议：

```
Markdown
      │
 AST
      │
─────────────
Outline
MindMap
Canvas
Knowledge Graph
```

例如：

```
# AI

## GPT

### OpenAI

### Claude
```

自动生成：

```
AI
├── GPT
│   ├── OpenAI
│   └── Claude
```

反过来：

拖动 MindMap

Markdown 自动更新。

这就是双向同步。

---

# 数据结构

建议采用

```
Workspace

├── Documents

├── Assets

├── Database

├── Plugins

├── AI

├── Cache

└── Sync
```

数据库：

```
SQLite

FTS5

Tag

Metadata

Recent

History

AI Chat

MindMap

Graph
```

---

# AI架构

不要把 AI 写死。

建议：

```
AI Provider

├── OpenAI

├── Claude

├── Gemini

├── DeepSeek

├── Qwen

├── Ollama

├── LM Studio

└── MCP
```

统一接口：

```
abstract class AIProvider{
    Future chat();
    Future embedding();
    Future rerank();
}
```

以后增加模型：

不用修改 UI。

---

# 插件系统

建议：

```
Plugin

├── Markdown

├── Export

├── Import

├── AI

├── Theme

├── Toolbar

├── Command

├── OCR

└── PDF
```

全部热加载。

---

# 最终目录结构（推荐）

```
knowledge-workbench/

├── apps/
│   ├── windows/
│   └── android/
│
├── packages/
│   ├── ui/
│   ├── editor/
│   ├── markdown/
│   ├── mindmap/
│   ├── pdf/
│   ├── ai/
│   ├── sync/
│   ├── database/
│   └── plugin/
│
├── rust/
│   ├── parser/
│   ├── search/
│   ├── office/
│   ├── pdf/
│   ├── ocr/
│   ├── ai/
│   └── core/
│
├── docs/
├── assets/
├── themes/
├── plugins/
└── scripts/
```

---

# 针对你的项目，我推荐的「产品级技术路线」

考虑到我们之前讨论的目标——集成**Typora（Markdown 编辑）+ MarkItDown（文档转换）+ KillerPDF（PDF 工具）+ SimpleMindMap（思维导图）+ 知识库**——我建议直接按下面的架构设计：

| 层级 | 技术方案 |
|---|---|
| UI 框架 | **Flutter**（Windows + Android 共用） |
| 核心业务 | **Rust**（解析、索引、转换、AI 能力） |
| 数据库 | SQLite（Drift）+ FTS5 全文检索 |
| Markdown | pulldown-cmark / markdown-it-rs + 自研 AST 编辑器 |
| 文档转换 | MarkItDown + Pandoc（按需） |
| PDF | PDFium + PDF.js |
| 思维导图 | SimpleMindMap（初期）→ 后续自研 Rust 数据模型 |
| AI | MCP + 多模型统一接口 |
| 同步 | WebDAV、OneDrive、Git（插件化扩展） |
| 插件 | Flutter UI 插件 + Rust Core 插件双层架构 |

**这个方案最大的优势**是：一套 UI、一套核心引擎，同时覆盖 Windows 和 Android；未来扩展到 macOS、Linux，甚至 Web 和 iOS，也无需推倒重来，能够作为一个长期演进的产品架构。

## Q4 · 去掉AI功能（第 4 轮对话）

> **提问：** 去掉AI功能

如果**完全去掉 AI 功能**，你的产品定位会更加明确：

> **一款专注于知识管理与文档编辑的跨平台应用**，类似**Typora + Obsidian（非 AI）+ XMind + PDF 工具**，强调**速度、离线、稳定、数据本地化**。

这样架构可以进一步简化，也更容易做到产品级。

---

# 推荐技术架构（Windows + Android）

```
                    UI Layer
              Flutter 3.x（统一界面）
─────────────────────────────────────
           Business Logic Layer
      文档│知识库│思维导图│PDF│搜索│同步
─────────────────────────────────────
             Rust Core Engine
 Markdown │ Office │ PDF │ Index │ Export
─────────────────────────────────────
           SQLite + 本地文件系统
```

---

# 技术选型（2026 推荐）

| 模块 | 推荐技术 | 说明 |
|---|---|---|
| UI | Flutter | Windows、Android 共用界面 |
| 状态管理 | Riverpod | 响应式、易维护 |
| 路由 | GoRouter | 官方推荐方案 |
| 数据库 | SQLite + Drift | 本地数据管理 |
| 文件监听 | Watcher | 自动刷新文档 |
| 全文搜索 | SQLite FTS5 或 Tantivy | 毫秒级搜索 |
| Markdown解析 | pulldown-cmark（Rust） | 高性能 |
| Markdown渲染 | flutter_markdown（可逐步替换） | 初期开发快 |
| PDF阅读 | PDFium | Windows、Android 均可 |
| PDF处理 | lopdf、pdfium-rs | 合并、拆分、提取等 |
| Office导入 | MarkItDown | Word、PPT、Excel 转 Markdown |
| 导出 | Pandoc（可选） | PDF、Word、HTML 等 |
| 思维导图 | SimpleMindMap | 成熟、易集成 |
| 图片处理 | image、image_editor | 裁剪、压缩 |
| 配置管理 | shared_preferences + SQLite | 用户设置 |

---

# 建议采用模块化架构

```
knowledge-workbench
│
├── app_ui              Flutter界面
│
├── editor              Markdown编辑器
│
├── viewer              阅读器
│
├── document            文档管理
│
├── workspace           工作区
│
├── knowledge           知识库
│
├── search              全文搜索
│
├── pdf                 PDF模块
│
├── office              Office导入
│
├── markdown            Markdown解析
│
├── mindmap             思维导图
│
├── export              导出
│
├── sync                同步
│
├── plugin              插件系统
│
└── core                Rust核心
```

---

# 核心功能模块

#### 1. Markdown 编辑器

支持：

- 实时预览（Typora 风格）

- 所见即所得

- 表格编辑

- 数学公式

- Mermaid

- PlantUML

- 代码高亮

- 自动目录

- 大纲导航

- 图片拖拽

- 文件拖拽

- 自动保存

- 多标签页

---

#### 2. 文档管理

支持：

```
工作区

├── 文件夹

├── Markdown

├── PDF

├── Word

├── Excel

├── PPT

├── 图片

└── 附件
```

特点：

- 文件树

- 收藏

- 最近打开

- 回收站

- 标签

- 星标

- 历史版本

---

#### 3. 知识库

建议采用：

```
Workspace

├── Notebook

│   ├── 文档

│   ├── 图片

│   ├── PDF

│   └── 附件
│
├── 标签
│
├── 分类
│
└── 索引
```

数据库保存：

- 标签

- 收藏

- 最近访问

- 文档属性

- 缩略图

- 搜索索引

真正的文件仍保存在本地目录。

---

#### 4. 思维导图

建议不要独立存储。

推荐：

```
Markdown

↓

Heading

↓

Tree

↓

MindMap
```

例如：

```
# Flutter

## Widget

### Stateless

### Stateful
```

自动生成：

```
Flutter
 ├── Widget
      ├── Stateless
      └── Stateful
```

支持：

- Markdown ⇄ 思维导图双向同步

- 折叠节点

- 导出图片

- 导出 PDF

---

#### 5. PDF 模块

支持：

- 阅读

- 搜索

- 批注

- 高亮

- 合并

- 拆分

- 删除页面

- 页面旋转

- 提取图片

- 提取文字

- OCR（可选）

---

#### 6. Office 模块

支持导入：

- Word

- Excel

- PPT

统一转换：

```
Office

↓

Markdown

↓

编辑
```

保持编辑体验一致。

---

#### 7. 导出

支持：

```
Markdown

↓

HTML

↓

PDF

↓

Word

↓

图片

↓

EPUB
```

---

#### 8. 搜索系统

建议：

SQLite FTS5

支持：

- 全文搜索

- 文件名搜索

- 标签搜索

- 文件夹搜索

- 最近搜索

速度快，且无需额外搜索服务。

---

#### 9. 同步

建议插件化。

第一阶段：

- 本地文件

第二阶段：

- WebDAV

第三阶段：

- OneDrive

- Dropbox

- Google Drive

第四阶段：

- Git

---

#### 10. 插件系统

插件类型：

```
Plugin

├── Markdown扩展

├── 导出扩展

├── 导入扩展

├── PDF工具

├── 思维导图

├── 工具栏

├── 快捷命令

├── 主题

└── 同步
```

---

# 推荐最终技术组合（产品级）

| 层级 | 技术 |
|---|---|
| UI | **Flutter** |
| 核心引擎 | **Rust** |
| 数据存储 | **SQLite + Drift + FTS5** |
| Markdown | **pulldown-cmark（Rust）+ 自研编辑器** |
| 文档转换 | **MarkItDown** |
| PDF | **PDFium + lopdf** |
| 思维导图 | **SimpleMindMap（初期）→ 后续自研渲染引擎** |
| 导出 | **Pandoc（可选）** |
| 同步 | **WebDAV / OneDrive / Git（插件化）** |
| 插件 | **Flutter + Rust 双层插件架构** |

---

#### 产品定位建议

这款应用可以定位为一个**离线优先（Offline First）**的知识工作台，而不是单纯的 Markdown 编辑器。核心能力围绕**文档编辑、知识管理、思维导图、PDF 处理、Office 导入导出**五大模块展开，采用**Flutter + Rust**的技术路线，兼顾 Windows 与 Android 的一致体验，同时保留未来扩展到 macOS、Linux 和 iOS 的能力。

相比加入 AI，这种定位更专注、性能更高、依赖更少，也更适合长期打磨成一款稳定、高效的生产力工具。

## Q5 · 给这个应用取一个名字（第 5 轮对话）

> **提问：** 给这个应用取一个名字

结合我们之前讨论的定位，这款产品不是普通的 Markdown 编辑器，而是：

- 📚 本地知识管理

- 📝 Markdown 编辑（Typora 风格）

- 🧠 思维导图

- 📄 PDF 阅读与处理

- 📂 Office 文档导入

- 🗂️ 文件树知识库

- 💻 Windows + Android

- ⚡ 离线优先、速度快、数据属于用户

因此，我建议名字不要局限于「Markdown」，而是打造一个**品牌名**，未来可以承载更多功能。

---

# 第一梯队（⭐⭐⭐⭐⭐ 最推荐）

##### 1. InkFlow（★★★★★）

> Ink（书写）+ Flow（思维流）

寓意：

> 思考与写作自然流动。

优点：

- 国际化

- 简洁

- 好记

- Logo 好设计

---

##### 2. NoteCraft（★★★★★）

> Craft = 匠心打造

寓意：

> 精心打造每一份知识。

非常符合产品定位。

---

##### 3. MindDock（★★★★★）

Dock = 工作台

寓意：

> 思维停靠的地方。

比 Workspace 更有品牌感。

---

##### 4. NodeBook（★★★★★）

Node + Notebook

突出：

- 知识节点

- 思维网络

未来做知识图谱也很契合。

---

##### 5. PaperFlow（★★★★★）

寓意：

所有文档自然流转。

适合：

Markdown

PDF

Office

MindMap

---

# 第二梯队（更有科技感）

#### Lumino

Light + Knowledge

象征知识被点亮。

---

#### NovaNote

Nova（新星）

寓意：

新的知识工具。

---

#### SynNote

Sync

System

Note

寓意：

组织你的知识。

---

#### FlowNote

简单直观。

---

#### NoteOne

一个应用完成所有事情。

---

# 中文品牌（推荐）

#### 墨知（★★★★★）

> 墨 + 知识

很有文化感。

Logo 也容易设计。

---

#### 墨境（★★★★★）

写作

阅读

思维

知识空间

---

#### 知墨

比墨知更偏知识管理。

---

#### 知屿

知识岛屿。

寓意：

建立自己的知识世界。

---

#### 文枢

枢纽。

所有文档中心。

---

#### 墨仓

知识仓库。

---

#### 文境

文档 + 世界。

---

#### 墨云

虽然离线，

但有云同步。

名字很好听。

---

# 偏专业

Knowledge Studio

Document Studio

Workspace

Mind Studio

DocFlow

Paper Studio

---

# 偏极简

Noto

Ink

Flow

Draft

Slate

Atlas

Origin

Leaf

Verse

---

# 如果想做成国际品牌（⭐⭐⭐⭐⭐）

我最推荐：

| 名称 | 推荐 | 品牌感 | 易传播 | 未来扩展 |
|---|---|---|---|---|
| **InkFlow** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **MindDock** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **NoteCraft** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **NodeBook** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **PaperFlow** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

# 如果是面向国内市场（⭐⭐⭐⭐⭐）

我建议优先考虑：

1. 墨知 （最有品牌感）

1. 文枢 （专业、稳重）

1. 墨境 （文艺、高端）

1. 知屿 （年轻、有想象力）

1. 知墨 （简洁易记）

---

#### 结合你的产品定位，我最推荐三个方向 🎯

- InkFlow ：国际化程度最高，适合作为长期品牌，可扩展到更多生产力工具。

- 墨知 ：中文品牌辨识度高，契合知识管理与写作场景，容易形成品牌形象。

- MindDock ：突出“知识工作台”的定位，与你规划的 Markdown、思维导图、PDF、知识库融合产品非常契合。

如果你的目标是打造一款**能够与 Typora、Obsidian、Logseq 等同级竞争的产品**，我建议**品牌名不要包含 Note、Markdown、Editor、Doc 等功能词**，而是选择一个独立品牌名，例如**InkFlow**或**墨知**，这样未来无论扩展到知识库、协作、插件生态还是移动端，都不会受到名称限制。

## Q6 · 知屿 取一个能对应的英文名（第 6 轮对话）

> **提问：** 知屿 取一个能对应的英文名

**「知屿」**这个名字很有气质，给人的感觉是：

- 📚 知识（Knowledge）

- 🏝️ 岛屿（Island）

- 🌊 建立属于自己的知识世界

- 🌱 安静、沉浸、成长

如果对应英文名，我建议不要直译成**Knowledge Island**，那会像地名，而不是产品品牌。更适合的是意境对应或品牌化命名。

#### ⭐ 第一梯队（最推荐）

##### 1. IsleNote ⭐⭐⭐⭐⭐（推荐指数：★★★★★）

> Isle（小岛）+ Note

寓意：属于自己的知识岛。

- 简洁

- 好记

- 与「知屿」意境一致

- 域名和 Logo 设计空间大

---

##### 2. KnowIsle ⭐⭐⭐⭐⭐

> Know + Isle

直译就是：

> Knowledge Island

非常契合「知屿」。

优点：

- 一眼看懂含义

- 国际化

- 品牌感不错

---

##### 3. Isleo ⭐⭐⭐⭐⭐（最有品牌感）

类似：

- Notion

- Obsidian

- Arc

- Linear

Isleo 来源：

> Isle + io

优点：

- 很像成熟软件品牌

- 发音自然（/ˈaɪli.oʊ/）

- 不局限于 Markdown

我个人很喜欢。

---

##### 4. Knowa ⭐⭐⭐⭐⭐

来自：

Knowledge

Nova

Know

一个很现代的软件名字。

例如：

> Knowa Desktop

> Knowa Mobile

---

##### 5. IsleFlow ⭐⭐⭐⭐

知识在岛上流动。

适合你的定位。

---

# 第二梯队

##### Lumisle

Light + Isle

知识之岛。

---

##### Islenote

比 IsleNote 更正式。

---

##### Islet

Islet 本身就是：

> 小岛

非常简洁。

---

##### KnowDock

知识停靠港。

---

##### KnowNest

知识巢穴。

---

##### NoteIsle

很直观。

---

##### MindIsle

思维岛。

---

##### IslandX

科技感。

---

#### 如果采用品牌化命名（推荐）

很多成功的软件其实并不是英文单词。

例如：

- Notion

- Obsidian

- Raycast

- Linear

- Arc

- Figma

因此完全可以创造一个品牌：

##### Zhiyu

直接拼音。

国际用户也能接受。

例如：

> Zhiyu Desktop

> Zhiyu Android

很多中国软件都采用这种方式。

---

##### ZYNote

缩写。

---

##### ZY Studio

适合以后做生态。

---

# 我最推荐的三个

| 中文 | 英文 | 推荐指数 | 说明 |
|---|---|---|---|
| 知屿 | **Isleo** | ⭐⭐⭐⭐⭐ | 最有国际品牌感，不局限功能，适合长期发展 |
| 知屿 | **KnowIsle** | ⭐⭐⭐⭐⭐ | 与中文寓意最贴近，容易理解 |
| 知屿 | **Zhiyu** | ⭐⭐⭐⭐⭐ | 保留中文品牌特色，国际化也没有障碍 |

#### 我的建议

如果你的目标是打造一款**长期运营的产品**，类似 Typora、Obsidian、Notion 这样拥有独立品牌识别度的软件，我会推荐：

- 中文品牌：知屿

- 英文品牌：Isleo

它们并不是逐字翻译，而是保持了“岛屿、知识、沉浸”的核心意境，同时**Isleo**发音简洁、视觉现代、品牌感强，也便于未来扩展到 Windows、Android，甚至更多平台。

## Q7 · | 层级 | 技术（第 7 轮对话）

> **提问：** | 层级 | 技术 | | -------- | -------------------------------- | | UI |**Flutter**| | 核心引擎 |**Rust**| | 数据存储 |**SQLite + Drift + FTS5**| | Markdown |**pulldown-cmark（Rust）+ 自研编辑器**| | 文档转换 |**MarkItDown**| | PDF |**PDFium + lopdf**| | 思维导图 |**SimpleMindMap（初期）→ 后续自研渲染引擎**| | 导出 |**Pandoc（可选）**| | 同步 |**WebDAV / OneDrive / Git（插件化）**| | 插件 |**Flutter + Rust 双层插件架构**| 提供这些技术的github来源

下面是基于你最终确定的技术路线，为每一项技术整理的**GitHub 官方仓库**（优先官方仓库，其次事实上的官方维护仓库）。这些项目基本都是目前业界成熟方案，非常适合作为**「知屿（Isleo）」**的技术基础。

| 模块 | 技术 | GitHub | 推荐指数 | 备注 |
|---|---|---|---|---|
| UI | Flutter | https://github.com/flutter/flutter | ⭐⭐⭐⭐⭐ | 官方 Flutter SDK |
| Dart | Dart SDK | https://github.com/dart-lang/sdk | ⭐⭐⭐⭐⭐ | Flutter 语言 |
| 状态管理 | Riverpod | https://github.com/rrousselGit/riverpod | ⭐⭐⭐⭐⭐ | Flutter 最佳实践 |
| 路由 | GoRouter | https://github.com/flutter/packages/tree/main/packages/go_router | ⭐⭐⭐⭐⭐ | Flutter 官方维护 |

---

# Rust 核心

| 技术 | GitHub | 推荐 |
|---|---|---|
| Rust | https://github.com/rust-lang/rust | ⭐⭐⭐⭐⭐ |
| Cargo | https://github.com/rust-lang/cargo | ⭐⭐⭐⭐⭐ |
| Tokio | https://github.com/tokio-rs/tokio | ⭐⭐⭐⭐⭐ |
| anyhow | https://github.com/dtolnay/anyhow | ⭐⭐⭐⭐⭐ |
| serde | https://github.com/serde-rs/serde | ⭐⭐⭐⭐⭐ |

---

# Flutter ↔ Rust 通信

目前推荐：

| 技术 | GitHub | 推荐 |
|---|---|---|
| flutter_rust_bridge | https://github.com/fzyzcjy/flutter_rust_bridge | ⭐⭐⭐⭐⭐ |

这是 Flutter 官方社区目前最成熟的 Rust 桥接方案。

---

# 数据库

#### SQLite

https://github.com/sqlite/sqlite

⭐⭐⭐⭐⭐

---

#### Drift

https://github.com/simolus3/drift

⭐⭐⭐⭐⭐

Flutter 最好的 SQLite ORM。

---

#### sqlite3_flutter_libs

https://github.com/simolus3/sqlite3.dart

用于 Flutter 内置 SQLite。

---

#### SQLite FTS5

SQLite 官方模块

无需单独仓库。

---

# Markdown

#### pulldown-cmark

https://github.com/pulldown-cmark/pulldown-cmark

⭐⭐⭐⭐⭐

Rust 生态最快 Markdown Parser。

---

#### markdown-it-rs

https://github.com/markdown-it-rust/markdown-it

⭐⭐⭐⭐⭐

如果以后需要插件生态，可以考虑。

---

#### mdBook（参考）

https://github.com/rust-lang/mdBook

Rust Markdown 应用范例。

---

# Markdown 编辑器（参考项目）

#### MarkText

https://github.com/marktext/marktext

⭐⭐⭐⭐⭐

Typora 最大开源参考。

---

#### Zettlr

https://github.com/Zettlr/Zettlr

⭐⭐⭐⭐⭐

大型 Markdown 软件。

---

#### Joplin

https://github.com/laurent22/joplin

⭐⭐⭐⭐⭐

完整笔记软件。

---

# 文档转换

#### MarkItDown

https://github.com/microsoft/markitdown

⭐⭐⭐⭐⭐

微软官方。

支持：

Word

PPT

Excel

PDF

HTML

图片

Markdown

---

#### Pandoc

https://github.com/jgm/pandoc

⭐⭐⭐⭐⭐

文档转换神器。

---

# PDF

#### PDFium

https://github.com/chromium/pdfium

⭐⭐⭐⭐⭐

Chrome 使用。

Windows 首选。

---

#### pdfium-render

https://github.com/ajrcarey/pdfium-render

Rust 封装。

---

#### lopdf

https://github.com/J-F-Liu/lopdf

⭐⭐⭐⭐⭐

Rust PDF 编辑。

---

#### PDF.js（可参考）

https://github.com/mozilla/pdf.js

Mozilla 官方。

---

# 思维导图

#### SimpleMindMap

https://github.com/wanglin2/mind-map

⭐⭐⭐⭐⭐

与你项目最匹配。

---

#### jsMind

https://github.com/hizzgdev/jsmind

---

#### Mind Elixir

https://github.com/ssshooter/mind-elixir-core

---

#### KityMinder

https://github.com/fex-team/kityminder-editor

百度。

---

# 文件监听

notify

https://github.com/notify-rs/notify

Rust 官方常用。

---

# 全文搜索

#### Tantivy

https://github.com/quickwit-oss/tantivy

⭐⭐⭐⭐⭐

Rust 版 Elasticsearch。

如果数据量很大，非常推荐。

---

如果只做几十万文档：

SQLite FTS5 即可。

---

# 同步

#### WebDAV

https://github.com/nerdcave/webdav

参考协议。

---

#### Git

https://github.com/git/git

---

#### libgit2

https://github.com/libgit2/libgit2

如果以后做 Git 同步。

---

# 文件树

walkdir

https://github.com/BurntSushi/walkdir

Rust 最常用。

---

ignore

https://github.com/BurntSushi/ripgrep

用于忽略`.gitignore`。

---

# 导出

Pandoc

https://github.com/jgm/pandoc

---

wkhtmltopdf（可选）

https://github.com/wkhtmltopdf/wkhtmltopdf

---

# 插件系统

#### extism

https://github.com/extism/extism

⭐⭐⭐⭐⭐

目前 Rust 插件化最佳方案。

支持：

Rust

Go

Python

JavaScript

未来插件可以跨语言。

---

# Wasmtime

https://github.com/bytecodealliance/wasmtime

如果以后全部插件 WebAssembly。

---

# 图表

Mermaid

https://github.com/mermaid-js/mermaid

---

PlantUML

https://github.com/plantuml/plantuml

---

# 图片

image

https://github.com/image-rs/image

Rust 图片库。

---

# OCR（可选）

Tesseract

https://github.com/tesseract-ocr/tesseract

---

PaddleOCR

https://github.com/PaddlePaddle/PaddleOCR

---

# UI 图标

Material Symbols

https://github.com/google/material-design-icons

---

Lucide

https://github.com/lucide-icons/lucide

现代风格，非常推荐。

---

# ⭐ 我建议的「知屿（Isleo）v1.0」完整技术栈

| 模块 | 最终方案 |
|---|---|
| UI | Flutter |
| 状态管理 | Riverpod |
| 路由 | GoRouter |
| Rust 桥接 | flutter_rust_bridge |
| 数据库 | SQLite + Drift |
| 全文搜索 | SQLite FTS5（后续可升级 Tantivy） |
| Markdown | pulldown-cmark + 自研编辑器 |
| 文档转换 | Microsoft MarkItDown |
| PDF | PDFium + lopdf |
| 思维导图 | SimpleMindMap |
| 导出 | Pandoc |
| 文件监听 | notify |
| 文件遍历 | walkdir |
| 图表 | Mermaid + PlantUML |
| 图片 | image-rs |
| 同步 | WebDAV + Git（libgit2） |
| 插件 | Extism（WASM） + Flutter + Rust 双层架构 |

---

#### 我的建议：再增加几个“产品级”基础库

如果你的目标是把**知屿（Isleo）**做成一款可长期迭代、媲美 Typora、Obsidian、Logseq 的产品，我建议在上述基础上再重点研究以下几个 GitHub 项目：

1. AppFlowy ：学习 Flutter 桌面应用的整体架构、插件设计和文档编辑实现。

1. AFFiNE ：参考无限画布、文档与知识管理的交互设计。

1. SiYuan（思源笔记） ：学习本地优先、块级编辑、知识库管理。

1. Joplin ：参考成熟的同步机制、资源管理和跨平台经验。

1. MarkText ：重点研究 Typora 风格的 Markdown 编辑体验。

这几个项目与你的产品方向契合度最高，值得作为整体架构和交互设计的重要参考。
