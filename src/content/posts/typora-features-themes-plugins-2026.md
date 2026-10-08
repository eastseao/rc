---
title: "Typora 功能·主题·插件全面指南"
description: "Typora 所见即所得编辑器功能详述、Mermaid 图表、主题推荐与插件生态全面指南。"
pubDatetime: 2026-05-31
category: "建站与技术"
kind: "长文"
tags: ["Typora", "所见即所得", "Mermaid", "主题", "插件"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00250-2025-10-15 Typora 功能与使用体验介绍（含 Pandoc 介绍）00613-2026-02-28 Typora 功能详述（含 HTML 容器支持、可视化提示词）00671-2026-03-07 全面介绍 Typora 功能（AI 数据可视化培训课件）00709-2026-03-13 推荐好看的 Typora 主题01252-2026-05-31 Typora 插件全面指南

## 01 · Typora 是什么与付费信息（00250 / 00613 / 00671）

Typora 是一款设计简洁、功能强大的 Markdown 编辑器，最与众不同的是真正的**所见即所得（WYSIWYG）**——彻底告别「左边编辑、右边预览」的分屏：你输入`##`建二级标题、用`**`加粗，标记立刻被渲染成最终排版，光标离开即隐藏标记，界面干净无干扰。

| 维度 | 说明 |
|---|---|
| **核心定位** | 轻量级、跨平台的 Markdown 文本编辑器，追求极简设计与无干扰写作体验。 |
| **核心特色** | 实时预览（所见即所得）、简洁界面、强扩展语法（CommonMark + GFM）、专注/打字机等辅助模式、灵活导出。 |
| **操作系统** | Windows、macOS、Linux 三大平台，数据互通无压力。 |
| **适用人群** | 开发者、写作者、学生、科研人员，以及常做会议纪要、报告、数据可视化文档的职场人。 |
| **费用情况** | 已结束公测转**付费软件**。从 1.0 版本起采用**买断制**，价格**14.99 美元或 89 元人民币**，支持在**3 台设备**上激活，并提供**15 天免费试用**。 |

> **正版提醒（照录）**：网络上可能存在所谓「破解版」，但出于安全和支持开发者考虑，强烈建议通过官网 typora.io 购买和下载正版。

## 02 · 语法 · 快捷键 · 视图模式 · HTML 容器（00613 / 00671）

Typora 全面支持标题、列表、引用、链接、图片、表格、代码块等标准语法，并扩展了任务列表、脚注、目录`[TOC]`、Emoji、LaTeX 数学公式与 Mermaid 图表。下表把高频语法与 Typora 快捷键一一对应（照录 00671）。

| 功能 | 语法 | Typora 快捷键 |
|---|---|---|
| 标题 | `# 一级标题` | Ctrl + 1 / 2 / 3 / 4 / 5 / 6 |
| 粗体 | `**粗体**` | Ctrl + B |
| 斜体 | `*斜体*` | Ctrl + I |
| 删除线 | `~~删除线~~` | Alt + Shift + 5 |
| 下划线 | `<u>下划线</u>` | Ctrl + U |
| 高亮 | `==高亮==` | 需在偏好设置中开启 |
| 无序列表 | `- 项目`或`* 项目` | Ctrl + Shift + ] |
| 有序列表 | `1. 项目` | Ctrl + Shift + [ |
| 表格 | 竖线分隔 | Ctrl + T |
| 代码块 | 围栏 + 语言名 | Ctrl + Shift + K |
| 引用块 | `> 一级`/`>> 二级` | Ctrl + Shift + Q |
| 超链接 | `[文字](URL)` | Ctrl + K |
| 图片 | `![描述](路径)` | Ctrl + Shift + I |
| 任务列表 | `- [ ] 待办`/`- [x] 已完成` | 手动输入 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">视图模式（含快捷键）</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>专注模式</dt><dd>F8。当前编辑行高亮、其他行淡出变灰，帮你聚焦当下。</dd><dt>打字机模式</dt><dd>F9。始终保持编辑行在屏幕中央，适合长时间码字。</dd><dt>侧边栏</dt><dd>Ctrl+Shift+1 大纲视图 / Ctrl+Shift+2 文件树；大纲按标题自动生成，长文档一键跳转。</dd><dt>源代码模式</dt><dd>Ctrl + /。需要精细调整时一键切回传统源码编辑。</dd><dt>全屏</dt><dd>F11。沉浸写作。</dd><dt>字数统计</dt><dd>实时统计字数、字符数、行数，甚至预估阅读时长。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">推荐初始偏好设置</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>通用</dt><dd>开启自动保存防丢失；关闭自动检查更新避免弹窗。</dd><dt>外观</dt><dd>主题选 GitHub，经典清晰。</dd><dt>编辑器</dt><dd>关闭拼写检查；开启「显示当前块元素的 Markdown 源码」便于学语法。</dd><dt>图像</dt><dd>复制图片到<code>./${filename}.assets</code>文件夹；优先使用相对路径，保证文档可移植。</dd><dt>Markdown</dt><dd>开启内联公式、下标、上标、高亮、图表等扩展。</dd></dl></div></div>

<details open><summary>Typora 支持哪些 HTML 容器（00613）<span>4 类 + 注意事项</span></summary><div><p>官方把支持的标签分为<b>内联标签</b>与<b>块级标签</b>两类，用于做比标准 Markdown 更丰富的排版。</p><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">类别</th><th>典型标签与用途</th></tr></thead><tbody><tr><td>块级容器 / 布局</td><td><code>&lt;div&gt;</code>通用容器配 CSS；<code>&lt;center&gt;</code>居中；<code>&lt;details&gt;</code>+<code>&lt;summary&gt;</code>可折叠详情块（FAQ）；<code>&lt;table&gt;</code>系列标签做合并单元格（colspan / rowspan）——这是原生表格做不到的。</td></tr><tr><td>文本格式化 / 标记</td><td><code>&lt;span&gt;</code>对一小段文字套独立样式；<code>&lt;ruby&gt;</code>+<code>&lt;rt&gt;</code>注音（如汉字标拼音）；<code>&lt;kbd&gt;</code>键盘按键；<code>&lt;sup&gt;</code>/<code>&lt;sub&gt;</code>上标下标。</td></tr><tr><td>多媒体 / 嵌入</td><td><code>&lt;video&gt;</code>/<code>&lt;audio&gt;</code>嵌入音视频；<code>&lt;iframe&gt;</code>嵌入 YouTube、Bilibili 等网页分享代码。</td></tr><tr><td>交互 / 注释</td><td><code>&lt;details&gt;</code>折叠交互；<code>&lt;!-- ... --&gt;</code>编辑时可见、导出时隐藏的注释。</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>使用注意事项（照录）</h5><ul><li><b>安全限制</b>：出于安全，<code>&lt;script&gt;</code>等标签不会被执行；<code>id</code>、<code>class</code>、<code>data-*</code>在实时预览中被忽略，但导出 HTML/打印时会保留。</li><li><b>导出兼容</b>：HTML 内容在导出 PDF/HTML 时完美保留；导出 Word、LaTeX 时部分复杂结构可能丢失甚至变成纯文本。</li><li><b>编辑技巧</b>：复杂 HTML 块可单击非交互部分，或<code>Ctrl/Cmd + 单击</code>进入代码式编辑，点外部退出。</li><li><b>与 Markdown 混用</b>：块级 HTML 内部标准 Markdown 不解析（CommonMark 设计）；但内联标签（如<code>&lt;span&gt;</code>）内可混用 Markdown。</li></ul></div></div></details>

> **图片管理（00613 / 00671）**
> - 可直接粘贴网络图片或拖拽本地图片；右键图片可缩放。
> - 偏好设置可让插入图片自动复制到`./assets`并用相对路径引用，保证便携。
> - 支持与**PicGo**等图床工具集成，一键上传至 SM.MS、腾讯云 COS、阿里云 OSS，方便发博客。

## 03 · 导出发布与 Pandoc 链路（00250 / 00671）

Typora 原生支持导出 PDF、HTML、图片；安装**Pandoc**后可扩展导出 Word（docx）、LaTeX、ePub，也能从这些格式导入。Pandoc 被称为文档转换领域的「瑞士军刀」，用 Haskell 编写，由 John MacFarlane 开发。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">导出各格式怎么操作</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>PDF</dt><dd>文件 → 导出 → PDF；或 Ctrl+P 打印选「另存为 PDF」。格式完全保留，适合正式交付。</dd><dt>Word (docx)</dt><dd>需先装 Pandoc（pandoc.org/installing.html）并重启 Typora，再 文件 → 导出 → Word。Mermaid 图表会转成图片，表格格式基本保留。</dd><dt>图片</dt><dd>Typora 本身不直接导图片：可用截图工具，或先导出 HTML 用浏览器打开再截（如 GoFullPage 截长图）。</dd><dt>其他格式</dt><dd>装 Pandoc 后可导 LaTeX、ePub，也支持反向导入。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">Pandoc 基础命令（照录）</h3><pre>基本格式：pandoc [输入文件] -o [输出文件] # Markdown 转 HTML pandoc input.md -o output.html # Word 转 Markdown pandoc input.docx -o output.md # 生成 PDF（需 LaTeX 引擎） pandoc input.md --pdf-engine=xelatex -o output.pdf # 中文 PDF 防乱码，指定中文字体 pandoc doc.md -o doc.pdf --pdf-engine=xelatex -V mainfont=&quot;SimSun&quot;</pre><p style="font-size:13px;color:#64748b">原理：Pandoc 先把输入解析成抽象语法树（AST），再从 AST 生成目标格式；可用 Lua/Python 写 Filter 操作 AST。</p></div></div>

> **常见导出故障（00671 照录）**
> - **图片丢失**：多因用了绝对路径，移动文档后找不到 → 设置「复制图片到 ./assets + 相对路径」。
> - **Mermaid 不显示**：检查代码块是否标了`mermaid`语言、偏好设置是否开启「图表」。
> - **导出 Word 图表变代码**：Pandoc 版本过低或未安装 → 更新到最新版，Mermaid 会自动转图片。

## 04 · 七款社区主题与安装避坑（00709）

Typora 允许换主题换心情，有 CSS 基础还能改或自建。00709 整理了七款社区口碑不错、颜值在线的选择。

| 主题 | 风格 | 推荐理由 |
|---|---|---|
| **WhisperEden** | 宁静自然 | 柔和浅绿背景（#C7EDCC），长时间码字护眼，可自由定制，营造沉浸式写作氛围。 |
| **VLOOK** | 功能强大专业 | 不只是主题，更是一个增强插件，提供文档排版、内容导航和演示功能，适合专业技术文档/演示。 |
| **Github** | 经典简约 | 自带主题的代表，清爽、代码友好，「简约而不简单」。 |
| **Aspartate** | 柔和暗色护眼 | 黑色带点灰度而非纯黑，对眼睛更友好，深色模式爱好者心头好。 |
| **happysimple** | 高对比可定制 | 高对比让标题、代码块一目了然；内置多字体，配置文件注释清晰，适合爱折腾的人。 |
| **Gobalt** | 暗色极客 | 专为夜晚工作设计，减轻眼部疲劳，深夜也能专注。 |
| **Vue** | 现代简约 | 灵感来自 Vue.js 官方风格，清爽现代，响应式设计，不同屏幕都有不错显示。 |

<details open><summary>主题安装四步与导出避坑<span>00709</span></summary><div><ol style="margin:0 0 12px 18px;line-height:1.9"><li><b>下载主题</b>：从作者分享页（通常 GitHub 或博客）下载压缩包。</li><li><b>打开主题文件夹</b>：Typora → 文件 → 偏好设置 → 外观 → 打开主题文件夹。</li><li><b>安装</b>：解压后把<code>.css</code>文件和相关资源文件夹一起复制进主题文件夹。</li><li><b>应用</b>：<b>完全重启 Typora</b>，再从菜单「主题」里选择新装的主题。</li></ol><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:4px"><h5>导出避坑</h5><ul><li>高度自定义主题（如 happysimple）导出 PDF 可能排版错乱；常导出的人，用新主题后先测导出，或导出时临时切回官方主题。</li></ul></div></div></details>

## 05 · 插件生态：obgnail 全家桶 vs VLOOK（01252）

Typora 本身**没有官方插件系统**，原生功能刻意保持纯粹。社区用「黑魔法」做出两大主流增强包：全能型**obgnail/typora_plugin**（60+ 功能，最活跃）与排版专精的**VLOOK™**（Typora 首个增强插件）。主流插件要求 Typora 版本**≥ 0.9.98**。

| 取舍维度 | obgnail/typora_plugin | VLOOK™ |
|---|---|---|
| **定位** | 60+ 功能全家桶，全面提升写作效率 | Typora 首个增强插件，专精排版与 PDF 导出 |
| **适合谁** | 要更强的文档编辑、管理、搜索能力的人 | 把 Typora 当排版工具、需精美演示/分享的人 |
| **招牌功能** | 标签页管理、中英文混排、文件模板、思维导图 markmap、自动编号、Markdown 检查、一键上传博客、文件加密 | 一键发布 PDF、表格自动编号与题注、GitHub 风格 [!NOTE]/[!TIP] 警示块美化、图片剪影换色、交叉引用 |

<details open><summary>obgnail/typora_plugin 六大模块速览<span>01252</span></summary><div><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">模块</th><th>代表插件（功能）</th></tr></thead><tbody><tr><td>编辑与效率</td><td>window_tab 标签页（Ctrl+Tab 切换、中键关闭）；md_padding 中英文自动加空格（Ctrl+Shift+B）；templater 文件模板；cursor_history 光标历史跳转。</td></tr><tr><td>搜索与导航</td><td>search_multi 全局文件搜索（AND/OR/NOT、正则、按大小时间筛选）；collapse_paragraph Ctrl+点击折叠章节；toc 右侧大纲；go_top 一键到顶/底。</td></tr><tr><td>内容与图表</td><td>markmap 思维导图（大纲/代码块两种生成）；datatables 表格搜索过滤分页排序；集成 ECharts、PlantUML、DrawIO；fence_enhance 代码块一键复制与折叠；imageReviewer 悬浮看图。</td></tr><tr><td>界面与视觉</td><td>dark 夜间模式；blur 模糊非焦点内容；no_image 隐藏图片加速大文档；editor_width_slider 写作区宽度滑块；scrollBookmarker 书签。</td></tr><tr><td>文档处理协作</td><td>auto_number 自动编号章节/表格/图片/代码块；export_enhance 导出 HTML 把图片转 Base64 内嵌；markdownLint 语法检查；article_uploader 一键发博客；cipher 文件加密；redirectLocalRootUrl 跨笔记软件重定向资源路径。</td></tr></tbody></table></div></div></details>

<details><summary>obgnail 插件快速上手指引<span>01252</span></summary><div><ol style="margin:0 0 12px 18px;line-height:1.9"><li>在 GitHub 仓库下载源码压缩包，找到 Typora 程序目录下<code>window.html</code>所在目录（正式版类似<code>Typora\resources\</code>）。</li><li>把解压得到的<code>plugin</code>文件夹完整复制到该目录。</li><li>进入<code>plugin\bin\</code>：Windows 右键<code>install_windows.ps1</code>「使用 PowerShell 运行」；Linux 以管理员运行<code>install_linux.sh</code>。</li><li>重启 Typora，文档右键出现「常用插件」即成功；右键 → Interactive Plugins → Preferences 管理启用状态。</li></ol></div></details>
