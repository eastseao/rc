---
title: "Markdown 语法大全与应用场景"
description: "Markdown 语法（GFM）、引用块、代码块、表格与知识写作应用场景全面总结。"
pubDatetime: 2026-07-06
category: "建站与技术"
kind: "长文"
tags: ["Markdown 语法", "GFM", "引用块", "代码块", "知识写作"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00191-2025-10-09 Markdown 语法大全总结（20 条语法）00541-2026-01-24 Markdown 语法大全总结（含 mermaid、缩写等扩展）00249-2025-10-15 Markdown 特点及应用场景全面分析01372-2026-07-06 Markdown 引用语法（引用块专讲）

## 01 · Markdown 是什么与六大特点（00249）

Markdown 是一种轻量级标记语言，由约翰·格鲁伯于**2004 年**创立。核心理念是：让人们用易于阅读、易于编写的纯文本写作，再转换成有效的 XHTML（或 HTML）。说白了，就是用`#`、`*`、`-`这类简单符号代替复杂 HTML 标签，让作者专注内容本身。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>语法极简</dt><dd>学习成本极低，常用规则约 10 分钟掌握；符号直观，<code>#</code>是标题、<code>*文字*</code>是斜体、<code>**文字**</code>是粗体，贴近书写习惯。</dd><dt>纯文本兼容</dt><dd>任何文本编辑器（记事本、VSCode、Vim）都能打开；不受软件版本、操作系统限制，永远不会因升级打不开旧文件。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>可读性至上</dt><dd>这是设计首要目标。即便不渲染，原始 .md 文档也依然好读，与标签繁多的 HTML、二进制 Word 形成对比。</dd><dt>一次编写到处发布</dt><dd>可轻松转 HTML、PDF、Word、ePub、幻灯片；配合 Pandoc 可实现格式间任意转换。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>专注内容</dt><dd>写作时不用反复调字体、颜色、间距，只需标记结构，最终样式由 CSS 或转换工具统一控制。</dd><dt>灵活可扩展</dt><dd>标准语法有限，但 CommonMark、GitHub Flavored Markdown（GFM）补上了表格、任务列表、代码高亮等实用功能。</dd></dl></div></div>

> **它的三条局限（照录）**
> - **功能有限**：无法精确控制元素位置、复杂多栏布局，不适合宣传册、海报这类高设计要求场景。
> - **标准不统一**：不同平台有自己的「风味」扩展，同一文档在不同环境渲染效果可能不一致。
> - **仍需入门**：虽简单，但对习惯「所见即所得」的用户仍需短暂适应。

## 02 · 基础语法：标题 · 段落 · 强调 · 列表（00191 / 00541）

这是日常写作 90% 时间在用的部分。两份「语法大全」问答在此合并，重复项只列一次。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00191 / 00541</span><h3>标题、段落与换行</h3></div><div style="padding:14px 16px"><p>标题用<code>#</code>到<code>######</code>共六级；段落直接连续书写，段间空行；行尾加两个空格再回车即可换行。</p><pre># 一级标题 ## 二级标题 ### 三级标题 #### 四级标题 ##### 五级标题 ###### 六级标题 这是一个段落。需要换行时在行尾输入两个空格再回车， 或直接空一行另起新段落。</pre></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00191 / 00541</span><h3>文本强调</h3></div><div style="padding:14px 16px"><pre>*斜体文本* 或 _斜体文本_ **粗体文本** 或 __粗体文本__ ***粗斜体*** 或 ___粗斜体___ ~~删除线文本~~<u>下划线</u>（部分编辑器支持） ==高亮文本== （部分编辑器支持）</pre></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00191 / 00541</span><h3>三种列表：无序 / 有序 / 任务</h3></div><div style="padding:14px 16px"><pre>无序列表（缩进 2 空格表示子项）： - 项目1 - 项目2 - 子项目2.1 - 子项目2.2 * 另一种符号 + 又一种符号 有序列表（缩进 3 空格表示子项）： 1. 第一项 2. 第二项 1. 子项1 2. 子项2 任务列表： - [ ] 未完成任务 - [x] 已完成任务</pre></div></div>

## 03 · 链接 · 图片 · 代码 · 引用（00191 / 00541 / 01372）

外链、嵌图、代码块是技术写作主力；引用块由 01372 单独讲透。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>链接</span><h3>行内 / 参考式 / 自动链接</h3></div><div style="padding:14px 16px"><pre>[行内链接](https://example.com) [带标题的链接](https://example.com &quot;标题文本&quot;) [参考式链接][引用id] [引用id]: https://example.com &quot;可选标题&quot;<https: 自动链接.com><email@example.com></email@example.com></https:></pre></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>图片</span><h3>与链接语法几乎一致</h3></div><div style="padding:14px 16px"><pre>![替代文本](图片URL) ![带标题的图片](图片URL &quot;标题文本&quot;) ![参考式图片][图片引用] [图片引用]: 图片URL &quot;可选标题&quot;</pre><p style="font-size:13px;color:#64748b">图片就是链接前面多一个<code>!</code>。</p></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0;margin-top:14px"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>代码</span><h3>行内代码 · 围栏代码块 · 缩进代码块</h3></div><div style="padding:14px 16px"><p>行内用单引号；代码块用三个反引号并指定语言名以获得语法高亮；也可用四个空格（或一个制表符）缩进表示代码块。</p><pre>行内代码：使用 `printf()` 函数 ```javascript function hello() { console.log(&quot;Hello, World!&quot;); } ``` ```python def hello(): print(&quot;Hello, World!&quot;) ```</pre></div></div>

<details open><summary>引用块专讲（01372 · 2026-07-06）：嵌套、换行、分段<span>5 条规则</span></summary><div><p>引用（Blockquotes）用大于号<code>&gt;</code>表示。基本写法是在引用文字前加<code>&gt;</code>和一个空格。</p><pre>&gt; 这是一句引用的名言。 多行引用（建议每行都加 &gt;）： &gt; 这是第一行引用内容。 &gt; 这是第二行引用内容。 &gt; &gt; 这是第三行，中间隔了一个空行（引用内分段）。 嵌套引用（在 &gt; 后再加 &gt;，类似邮件回复缩进）： &gt; 这是第一层引用。 &gt;&gt; 这是第二层嵌套引用。 &gt;&gt;&gt; 这是第三层嵌套引用。 引用内部依然可以放标题、列表、代码： &gt; ## 这是一个标题 &gt; 1. 列表项一 &gt; `console.log('Hello');` 这是行内代码。</pre><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:12px"><h5>换行小技巧（重要，照录）</h5><ul><li>仅仅按回车换行<b>不会</b>在渲染时换行（会被合并成同一段）。</li><li>想在引用内<b>换行但不分段</b>：在行尾加<b>两个空格</b>再回车。</li><li>想<b>分段</b>：在段落之间加一个空行（该行也用<code>&gt;</code>占据或留空）。</li></ul></div><div style="overflow-x:auto;margin:16px 0;margin-top:14px;margin-bottom:0"><table><thead><tr><th style="width:180px">用途</th><th>语法</th></tr></thead><tbody><tr><td>普通引用</td><td><code>&gt; 文字</code></td></tr><tr><td>嵌套引用</td><td><code>&gt;&gt; 文字</code></td></tr><tr><td>引用内分段</td><td>中间加空行（或该行也写<code>&gt;</code>）</td></tr><tr><td>引用内换行</td><td>行尾加两个空格</td></tr></tbody></table></div></div></details>

## 04 · 表格 · 分割线 · 转义 · HTML 嵌入（00191 / 00541）

表格靠竖线与短横线对齐，分割线三种写法等价，转义用反斜杠，需要精细控制时可直接内嵌 HTML。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>表格</span><h3>对齐方式由冒号决定</h3></div><div style="padding:14px 16px"><pre>| 左对齐 | 居中对齐 | 右对齐 | |:-------|:--------:|-------:| | 单元格 | 单元格 | 单元格 | | 单元格 | 单元格 | 单元格 | 简化写法： 左对齐 | 居中对齐 | 右对齐 :--- | :---: | ---: 内容 | 内容 | 内容</pre><p style="font-size:13px;color:#64748b"><code>:---</code>左对齐，<code>:-:</code>居中，<code>---:</code>右对齐。</p></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>分割线 / 转义 / HTML</span><h3>其余常用结构</h3></div><div style="padding:14px 16px"><pre>水平分割线（三者等价）： --- *** ___ 转义字符（让符号不被解析）： \* 这不是斜体 \# 这不是标题 \[ 这不是链接 \] HTML 嵌入（Markdown 原生支持）： 这是<span style="color:red">红色</span>文本。<div align="center">居中内容</div></pre></div></div></div>

## 05 · 扩展语法与六大应用场景（00541 / 00249）

标准语法之外，各家解析器（GFM、CommonMark 等）有自己的扩展；下面这些功能「部分解析器支持」，用前先确认目标平台。

| 扩展语法 | 写法示例 |
|---|---|
| 脚注 | `正文[^1]`，文末`[^1]: 脚注内容` |
| 定义列表 | `术语1`换行`: 定义1` |
| 上标 / 下标 | `H~2~O`（下标）；`X^2^`（上标） |
| 目录（自动生成） | `[TOC]` |
| 数学公式（LaTeX） | 行内`$E = mc^2$`；块级`$$ ... $$` |
| 流程图 / 时序图 | 围栏语言标````mermaid`，如`graph TD; A-->B;` |
| 缩写 | `*[HTML]: HyperText Markup Language` |
| 注释（不渲染） | `<!-- 这是注释，不显示 -->` |

掌握语法之后，更重要的是知道它**该用在哪**。00249 给出的六大应用场景：

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>技术文档与博客</dt><dd>GitHub/GitLab/Gitee 的 README.md 是项目门面；Hexo、Jekyll、Hugo、VuePress、Docusaurus 等静态站原生支持；结合 Swagger、MkDocs 写 API 文档。</dd><dt>日常笔记与知识管理</dt><dd>印象笔记、有道云笔记支持 Markdown；Notion 编辑体验与之高度契合；Obsidian、Logseq、Typora 面向本地知识库，提供双向链接与图谱。</dd><dt>学术写作与报告</dt><dd>结合 Pandoc 把 Markdown 转成严谨的 PDF、Word 或 LaTeX，适合专注内容逻辑的论文与报告。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>沟通与协作</dt><dd>Slack、Discord、Telegram、Stack Overflow、知乎支持部分 Markdown；Markdown Here 插件可把 Markdown 一键渲染成 HTML 邮件。</dd><dt>书籍创作与电子出版</dt><dd>用 Markdown 写书，工具链生成 ePub、Mobi（Kindle）、PDF，流程清晰。</dd><dt>演示文稿</dt><dd>Marp、Reveal.js 允许用 Markdown 写幻灯片，再生成带动画的网页版幻灯片。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">未来趋势（照录）</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.8"><li><b>标准化</b>：CommonMark 等项目致力于消除语法歧义。</li><li><b>深度集成</b>：更深度融入各类软件与在线服务，成为底层内容编辑标准。</li><li><b>增强交互</b>：在 Observable HQ 这类平台，Markdown 开始与可执行代码（JS/Python）结合出动态文档。</li></ul></div></div>

> **兼容性提醒**：不同 Markdown 解析器（GitHub Flavored Markdown、CommonMark 等）支持的扩展语法不同——脚注、定义列表、数学公式、高亮、上下标、mermaid、缩写等，在某些平台或编辑器中可能不可用，发布前请查看目标平台文档。新手可从 Typora 或 StackEdit 这类「所见即所得」编辑器开始体验。
