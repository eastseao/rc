---
title: "Markdown 生成模板与文章转换"
description: "生成 Markdown 推文模板、整篇文章用 Markdown 形式展现、方案内容转换与框架展示方法。"
pubDatetime: 2025-11-09
category: "建站与技术"
kind: "长文"
tags: ["YAML 头", "推文模板", "整篇转换", "代码块", "AI 写作"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00168-2025-10-04 生成 Markdown 推文模板（YAML front-matter）00174-2025-10-05 整篇文章用 Markdown 形式展现（GitHub 用途）00200-2025-10-10 用 Markdown 格式生成方案内容（降本增效方案）00400-2025-11-06 Markdown 框架内 40 条人性观察（可复制代码块）00409-2025-11-09 Markdown 框架内展示七情六欲00370-2025-10-31 Markdown 框架展示（敏感内容请求被拒）

## 01 · 文章头部模板：YAML front-matter（00168）

静态博客（Jekyll/Hexo 等）的文章头用两段`---`包裹 YAML 元数据。00168 的任务是「按这个格式生成标题 test、日期为今天的推文」，生成结果照录如下。

```
---
layout: post
title: "test"
date: 2024-01-15 14:30:00 +0800
categories: [示例分类, 测试分类]
tags: [测试, 示例, 模板]
---
```

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>字段含义</dt><dd><code>layout</code>指定页面布局；<code>title</code>文章标题；<code>date</code>发布时间；<code>categories</code>分类数组；<code>tags</code>标签数组。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>使用要点</dt><dd><code>+0800</code>表示东八区（中国标准时间）；categories、tags 替换为实际内容；发布前把日期时间改成实际发布时间。</dd></dl></div></div>

## 02 · 整篇文章转 Markdown：GitHub 用途与降本方案（00174 / 00200）

「把一大段口语化长文整理成 Markdown」的关键动作：**提炼层级标题、把并列内容抽成列表、把对照类内容抽成表格**。两个实例如下。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00174</span><h3>实例一：GitHub 用途长文 → 结构化 Markdown</h3></div><div style="padding:14px 16px"><p>原文把 GitHub 用途分成个人、建站、学习、工作、创意五类。转换后用<code>##</code>/<code>###</code>分层，并把「建站类型」「创意玩法」「小结」做成表格。抽取的表格范式如下。</p><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:120px">类型</th><th style="width:220px">举例</th><th>使用方式</th></tr></thead><tbody><tr><td>静态网页</td><td>公司官网、产品展示页、活动页</td><td>直接上传 HTML/CSS/JS 到仓库，启用 GitHub Pages</td></tr><tr><td>文档系统</td><td>产品说明书、API 文档</td><td>用 Docsify / Docusaurus / VuePress</td></tr><tr><td>知识库</td><td>笔记、学习档案、wiki</td><td>用 Obsidian、MkDocs</td></tr><tr><td>简历页面</td><td>交互式个人简历</td><td>用 HTML 模板或 React 页面</td></tr></tbody></table></div><p style="margin-bottom:0">同名账户下可挂多个站点：<code>blog.hdbuyer.github.io</code>（博客）、<code>cv.hdbuyer.github.io</code>（简历）、<code>design.hdbuyer.github.io</code>（作品集）。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00200</span><h3>实例二：降本增效方案 → 带预期成果表的方案</h3></div><div style="padding:14px 16px"><p>「用 Markdown 格式生成方案内容」的范式：用<code># 一、总体目标</code>→<code>### （一）</code>→<code>#### 1.</code>三级标题搭骨架，措施用有序/无序列表，最后用一张表收预期成果。核心数字照录：</p><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th>项目</th><th style="width:170px">措施要点</th><th style="width:100px">预期降幅</th><th>预计节省（万元）</th></tr></thead><tbody><tr><td>燕窝及主要原料</td><td>—</td><td>3%–5%</td><td>60</td></tr><tr><td>黑枸杞等原料</td><td>替代与框架协议</td><td>10%–15%</td><td>120</td></tr><tr><td>包材（传统+电商）</td><td>优化批量 + 消化库存</td><td>10%</td><td>200</td></tr><tr><td>研发物料</td><td>锁价采购 + 替代原料</td><td>8%</td><td>40</td></tr><tr><td>运输成本</td><td>路线优化 + 运费下调</td><td>10%</td><td>25</td></tr><tr><td><b>合计</b></td><td colspan="3"><b>约 445 万元节省 + 出厂价优化收益（出厂价优化 3%–5%，保持利润率稳定）</b></td></tr></tbody></table></div><p style="font-size:13px;color:#64748b">目标：整体采购成本降 10%–15%、包材资金占用降 20%、运输费降 10%。物流侧照录：顺丰特快享 0.75 折优惠、整车货物整体降 10% 运费。</p></div></div>

## 03 · 零散条目转「可复制」代码块（00400）

当内容是一长串并列条目、用户又想保留语法符号便于粘贴时，做法是把它包进````markdown`代码块里输出。00400 的任务是「40 条人性观察，Markdown 格式化、带语法符号、可复制」，AI 最终用有序列表代码块交付。节选照录：

~~~~
```markdown
1. 贫穷时，穿着体面一点，更容易翻身。
2. 99%的男人都好色，99%的女人都爱钱。
3. 80%的生意，都是人情生意。
...
40. 不要高估了你和任何人的关系，更不要低估了人性的逐利规则，
    做好自己，亲疏随缘。
```
~~~~

> **为什么包代码块**（照录原说明）：把三个反引号及其中内容整体复制，粘贴到 GitHub、Notion、Typora 等支持 Markdown 的编辑器即可看到格式化效果；代码块里的语法符号（数字、点号、空格）原样保留。若需再调整（如改无序列表、加标题或强调）可继续提。

## 04 · 知识主题框架化：以「七情六欲」为例（00409）

00409 演示了两种交付：一种是直接渲染的 Markdown 文章，另一种是放进````markdown`代码框里、结构清晰可再复制的版本。两种都照录要点。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>七情</span><h3>两种分类体系</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>儒家分类</dt><dd>喜、怒、哀、惧、爱、恶、欲（最早见于《礼记·礼运》，人生而具有）。</dd><dt>中医分类</dt><dd>喜、怒、忧、思、悲、恐、惊。</dd></dl></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>六欲</span><h3>传统与现代理解</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>传统分类</dt><dd>眼（见欲）、耳（听欲）、鼻（香欲）、舌（味欲）、身（触欲）、意（意欲）。</dd><dt>现代延伸</dt><dd>求生欲、求知欲、表达欲、表现欲、舒适欲、情欲。</dd></dl></div></div></div>

```
关系：七情是情绪体验，六欲是需求动机，相互影响。
作用：适度的情欲是人性完整表现，过度则需节制。
```

> **交付范式**：知识主题用「概述 → 分主题（列表/表格）→ 关系与作用说明」组织；若用户要二次使用，再整段包进 markdown 代码框，保持结构清晰、易于复制扩展。

## 05 · 转换不是万能：敏感内容请求被拒（00370）

00370 的请求是「把一段露骨的成人内容用 Markdown 框架系统整理」。与前面几篇的差别只在主题：当内容本身涉及露骨性描写时，**「整理成 Markdown」这个排版动作也不会被执行**——AI 回复「这个问题我暂时无法回答，换个话题再聊聊」，并未产出任何整理后的正文。

> **可记的一条边界**
> - 排版、格式化、结构化整理这类工具性能力，会随**内容主题**一起被拒绝；不会因为「只是帮你排版」就放行敏感内容。
> - 正常的职场方案、知识科普、列表整理（前几篇）都可正常转换；露骨、违法、高危主题即使包上「Markdown 框架」也不会输出。
