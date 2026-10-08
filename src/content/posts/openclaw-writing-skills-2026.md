---
title: "OpenClaw 技能文件格式与写作规范"
description: "SKILL.md 格式与 frontmatter 字段、微信洗稿技能方案，以及文件写作规范 v1.0 与命名约定。"
pubDatetime: 2026-05-08
category: "AI与Agent"
kind: "手册"
tags: ["SKILL.md", "YAML frontmatter", "技能示例", "文件写作规范", "EastSeaO"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00856-2026-04-07 OpenClaw技能文件格式00934-2026-04-14 OpenClaw洗稿技能方案01120-2026-05-08 OpenClaw文件写作规范设计

## 01 · SKILL.md：YAML + Markdown 混合格式（00856）

OpenClaw 技能文件本质是一个 Markdown 文件（`.md`），但它结合了**YAML**（一种配置语言）和**Markdown**（一种文本格式化语言）的优点。核心结构分两部分：**Frontmatter 元数据区**（YAML 头，夹在两行`---`之间）和**正文内容区**（Markdown 主体）。

| 字段 | 必填/可选 | 作用 |
|---|---|---|
| `name` | **必填** | 技能的名称，用小写字母加连字符（kebab-case），如`my-awesome-skill`。这是技能在 OpenClaw 系统中的唯一标识。 |
| `description` | **必填** | 简短描述这个技能是做什么的。这个描述非常关键，是 OpenClaw 在用户提问时判断是否应调用这个技能的主要依据。 |
| `version` | 可选 | 技能的版本号，使用标准的语义化版本号（Semantic Versioning），如`1.0.0`。 |
| `author` | 可选 | 技能的作者或来源。 |
| `allowed-tools` | 可选 | 一个列表，指定该技能允许使用的工具，如`["bash", "read_file", "write_file"]`，用于增强安全性。 |

正文内容区在 Frontmatter 结束后，用标准 Markdown 编写，由几个关键部分构成：

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">① # 标题</h3><p style="font-size:13px;color:inherit">一个一级标题，明确技能名称。</p><h3 style="font-size:15px;font-weight:700;margin:12px 0 8px">② ## 简介/功能说明</h3><p style="font-size:13px;color:inherit">详细解释技能的用途、适用场景和具体功能，相当于一份「说明书」。</p><h3 style="font-size:15px;font-weight:700;margin:12px 0 8px">③ ## 使用指南</h3><p style="font-size:13px;color:inherit">说明如何触发技能、需要哪些输入、有哪些可选项、预期输出是什么。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">④ ## 示例</h3><p style="font-size:13px;color:inherit">提供输入和输出的例子，帮助 OpenClaw 更好理解如何应用技能。</p><h3 style="font-size:15px;font-weight:700;margin:12px 0 8px">⑤ ## 注意事项/限制</h3><p style="font-size:13px;color:inherit">描述技能的边界、潜在陷阱、或需要用户特别注意的地方。</p></div></div>

复杂技能还可在正文中使用`### Tools`、`### Scripts`、`### Templates`等更高级结构，以及子目录组织。最标准的示例骨架如下：

```
---
name: example-skill
description: A brief description of what this skill does and when to use it.
version: 1.0.0
author: OpenClaw User
allowed-tools: ["bash", "read_file", "write_file"]
---

# Example Skill

## Introduction
This skill provides a detailed explanation of its purpose and functionality.

## Usage
1.  **Trigger**: Describe how to activate this skill.
2.  **Input**: List any required inputs.
3.  **Process**: Explain the steps the OpenClaw agent will take.

## Examples
Provide concrete examples of input and output.

## Notes
Include any important caveats or limitations.
```

## 02 · 实战示例：文档可视化技能（00856 · doc_visualizer）

这是一个完整的技能文件示例：当用户提供结构化数据或请求可视化（如「制作一个月度支出图表」）时，它会生成并执行脚本以创建图表。其 Frontmatter 元数据与正文照录如下。

~~~~json
---
name: doc_visualizer
description: Use this skill whenever a user asks to visualize data, create charts, or generate reports from structured information (like JSON, CSV, or tables). It handles the entire process of generating scripts and executing them to produce visual outputs.
version: 1.1.0
author: DataVizPro
allowed-tools: ["bash", "read_file", "write_file", "python_repl"]
---

# Document Visualizer Skill

## Introduction
The Document Visualizer is an advanced tool designed to transform raw data into clear, insightful, and visually appealing charts and graphs. Whether you need a simple bar chart, a complex line graph, or a comprehensive report, this skill automates the process using Python.

## Features
*   **Multiple Chart Types**: Supports bar charts, line graphs, pie charts, scatter plots, and histograms.
*   **Customizable Styles**: Allows control over colors, labels, titles, and themes.
*   **Report Generation**: Can combine multiple charts into a single HTML report for easy sharing.
*   **Data Parsing**: Automatically detects and parses data from JSON, CSV, or Markdown tables.

## Usage
1.  **Provide Data**: Share your data in a structured format (e.g., a JSON array or a CSV snippet).
2.  **Specify Chart Type**: Tell me what kind of chart you want (e.g., "pie chart showing market share").
3.  **Request Execution**: Say "generate the visualization" or "create the chart".

## Example
**User Input:**
```json
{
  "labels": ["Q1", "Q2", "Q3", "Q4"],
  "values": [150, 230, 180, 290]
}
```
"Create a bar chart of this quarterly revenue data."

**Expected Output:**
The skill will generate a Python script using `matplotlib`, execute it, and save the output as `quarterly_revenue.png` in the current directory.

## Notes
*   The generated chart file path will be reported back to you.
*   Ensure the data format is consistent to avoid parsing errors.
*   This skill requires the `python_repl` tool to be enabled in your OpenClaw configuration.
~~~~

## 03 · 实战示例：微信爆款推文洗稿技能（00934 · wechat-rewriter-skill）

目标是让 OpenClaw 自动读取微信公众号文章，**拆解逻辑、提炼观点、重新撰写**成原创度更高的文章，生成全新的结构、案例和表达方式。目录结构照录如下。

```
wechat-rewriter-skill/
├── SKILL.md              # 技能定义文件（必须放在第一行）
├── scripts/              # 辅助脚本（可选，用于批量处理或工具调用）
│   ├── extract_article.py   # 从 URL 或文件中提取正文
│   └── rewrite_engine.py    # 调用大模型 API 进行改写
└── examples/             # 示例输入输出（可选，用于引导模型）
    ├── sample_input.txt
    └── sample_output.md
```

SKILL.md 的核心定义照录如下（OpenClaw 会优先读取 frontmatter 中的`name`和`description`来决定是否激活）：

~~~~
---
name: wechat-rewriter-skill
description: |
  当用户需要对微信公众号文章进行洗稿、改写、扩写或生成新文章时，激活此技能。
  支持输入文章 URL、文本内容或文件路径，输出符合微信公众号风格的原创文章。
version: 1.0.0
author: OpenClaw User
allowed-tools: ["read_file", "write_file", "bash", "python_repl"]
---

# 微信爆款推文洗稿技能

## 功能说明
本技能帮助用户快速将一篇微信文章改写为原创度更高、结构更清晰、更具传播性的新文章。它会自动完成以下步骤：
1.  **拆解原文**：分析标题逻辑、段落结构、核心观点和情绪节奏。
2.  **重构内容**：基于原文观点，重新组织语言，加入新的案例、比喻或数据。
3.  **优化标题**：生成 3-5 个备选标题，吸引点击。
4.  **排版输出**：生成适合微信公众号编辑器的 Markdown 或 HTML 格式。

## 使用指南
**触发方式**：用户输入以下任意一种：
*   "帮我洗稿这篇文章" + 文章链接/文本
*   "把这段文字改成原创风格"
*   "根据这篇推文写一篇新文章"

**输入要求**：
*   文章链接（需可公开访问）
*   或直接粘贴文章文本
*   或指定本地文件路径（如 `./articles/source.md`）

**输出格式**：
*   默认输出为 Markdown 格式，保存到 `./output/` 目录
*   文件名格式：`rewritten_YYYYMMDD_HHMMSS.md`
*   同时在对话中展示完整文章内容

## 处理流程（Step 1-6）
Step 1: **读取与清洗** - 提取正文，去除公众号特有的装饰性符号、广告和无关片段。
Step 2: **结构分析** - 识别原文的"钩子-展开-高潮-收尾"结构。
Step 3: **观点提取** - 用简洁语言列出原文的 3-5 个核心观点。
Step 4: **重构写作** - 基于核心观点，用全新的表达和案例重写，保持原意但改变句法。
Step 5: **标题生成** - 结合爆款公式生成 3-5 个备选标题。
Step 6: **格式输出** - 按微信公众号排版习惯输出（短句、分段、加小标题）。

## 环境变量配置
如需调用外部 API 进行改写，可在 `~/.openclaw/.env` 中配置：
```bash
OPENAI_API_KEY=sk-...
OPENAI_BASE_URL=https://api.openai.com/v1
REWRITER_MODEL=gpt-4o-mini
```

## 示例输入输出
**输入示例**（片段）：
> 今天分享一个让效率翻倍的小技巧...
**输出示例**（片段）：
> 你是否也曾每天忙到飞起，却感觉什么都没做完？今天这招，可能会彻底改变你的工作节奏...

## 注意事项
*   仅供学习与参考，请勿用于抄袭或侵权内容。
*   改写后的文章需人工审核，确保事实准确。
*   长文章建议分段处理，避免超出模型上下文限制。
~~~~

| 公式类型 | 示例结构 |
|---|---|
| **数字清单式** | 「X 个让你 XXX 的技巧，第 X 个最容易被忽略」 |
| **痛点提问式** | 「为什么你 XXX 却还是 XXX？答案可能和你想的不一样」 |
| **反常识式** | 「别再 XXX 了！真正的高手都在这样做」 |
| **身份代入式** | 「30 岁后才明白：XXX 的人，往往都有这个习惯」 |

##### 合规与风险提示

仅供学习参考，改写内容需人工审核

洗稿存在版权和原创性风险：① 仅供个人学习参考，不要直接用于商业发布；② 大模型改写可能引入事实错误，务必人工核对；③ 对于有明确版权的文章，改写发布可能构成侵权；④ 建议将技能定位为「灵感启发」和「初稿辅助」，而非全自动抄袭工具。

## 04 · 工作文件写作与生成规范 v1.0（01120）

这是一套「工作文件写作与生成规范」，目的是让每一份工作文档结构规范、信息完整、方便追溯——**所有项目中产生的工作文件，都必须遵循此规范进行写作与生成**。核心原则：标题精确、内容分层、格式统一、可追溯。

| 文件类型 | 编码前缀 | 用途 |
|---|---|---|
| **会议纪要** | `MEET` | 记录会议议题、讨论结论、待办事项。 |
| **需求文档** | `REQ` | 描述需求背景、功能点、验收标准。 |
| **设计文档** | `DES` | 记录技术方案、架构设计、接口定义。 |
| **工作计划** | `PLAN` | 拆解任务、分配责任人、设定时间节点。 |
| **项目报告** | `RPT` | 阶段性总结、进度汇报、数据统计。 |
| **复盘文档** | `RETRO` | 分析项目成败原因、沉淀经验教训。 |
| **普通笔记** | `NOTE` | 临时性记录、灵感碎片、调研素材。 |
| **规范说明** | `SPEC` | 本规范类文档自身的说明与修订。 |

标题统一格式为：`[编码前缀] 文档标题 - 项目名 - 日期`，例如`[MEET] 项目周会纪要 - RC智能体 - 2026-05-08`。文件内容按「元数据区 → 正文区 → 附录区」分层，元数据区以 YAML frontmatter 开头，照录如下。

```
---
doc_title: "文档标题"
sub_title: "文档副标题"
file_type: "MEET | REQ | DES | PLAN | RPT | RETRO | NOTE | SPEC"
project: "所属项目名称"
version: "v1.0.0"
author: "EastSeaO"
created_date: "2026-05-08"
last_updated: "2026-05-08"
tags: ["标签1", "标签2"]
---

# 正文标题

## 一、背景与目标
（说明文档产生的背景、要解决的问题、预期目标）

## 二、核心内容
（根据文件类型填充对应章节：会议纪要记结论与待办；需求文档写功能点与验收标准；设计文档画架构与接口……）

## 三、后续行动
（待办事项、责任人、时间节点）

---
## 附录
（链接、参考资料、补充说明）
```

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:14px"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">高频文件模板要点</h3><ul style="margin:0;padding-left:18px;font-size:13px;color:inherit;line-height:1.7"><li><b>MEET</b>：参会人、议题、结论、待办（Action Item 含责任人与截止日）。</li><li><b>REQ</b>：需求背景、功能点列表、验收标准、优先级。</li><li><b>DES</b>：技术选型、架构图、接口定义、数据库设计。</li><li><b>RPT</b>：进度概览、数据指标、风险与下周计划。</li><li><b>RETRO</b>：做得好、待改进、行动计划。</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">格式与追溯原则</h3><ul style="margin:0;padding-left:18px;font-size:13px;color:inherit;line-height:1.7"><li>同一文档可按<code>.md / .pdf / .docx / .xlsx</code>多格式输出，但源稿统一用 Markdown。</li><li>版本号语义化递增（major.minor.patch），每次修订更新<code>last_updated</code>。</li><li>作者统一署名<b>EastSeaO</b>。</li></ul></div></div>

## 05 · 多格式输出与模板文件体系（01120）

为了让规范可自动化执行，规范设计了「6 个核心设定文件 + 1 个生成指令文件」的模板体系，并对 PDF / DOCX / XLSX 三种输出格式分别定义了页面、页眉页脚、样式映射等要求。

| 全局信息字段 | 默认值 / 格式 | 说明 |
|---|---|---|
| `doc_title` | 必填 | 文档主标题。 |
| `sub_title` | 可空 | 文档副标题。 |
| `author` | `EastSeaO` | 作者，统一署名。 |
| `org` | 可空 | 所属组织/团队。 |
| `date` | `YYYY-MM-DD` | 文档日期。 |
| `version` | `v1.0` | 文档版本。 |
| `classification` | 内部 / 公开 / 机密 | 密级。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>PDF 输出</span><h3>页面 / 页眉页脚 / 标题层级</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>页面设置</dt><dd>A4，页边距上下左右统一，中文正文用衬线字体、英文/代码用等宽字体。</dd><dt>页眉</dt><dd>左：文档标题；右：密级；下方一条细分隔线。</dd><dt>页脚</dt><dd>居中：作者 + 日期；右侧：页码<code>第 X 页 / 共 Y 页</code>。</dd><dt>标题层级</dt><dd>一级标题居中加粗，二级标题左对齐加粗，正文首行缩进。</dd><dt>封面</dt><dd>大标题居中，副标题、作者、日期、版本依次排列。</dd></dl></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>DOCX 输出</span><h3>内置属性 / 样式映射</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>文档属性</dt><dd>标题、作者（EastSeaO）、主题、关键词、版本、密级写入 Word 内置属性。</dd><dt>节设置</dt><dd>首页不同、奇偶页不同，正文另起一页。</dd><dt>样式映射</dt><dd>Markdown 标题 → Word「标题 1/2/3」；表格 → Word 网格表。</dd><dt>大词风格</dt><dd>正文采用「大词风格」Word 模板，字距行距宽松、可读性优先。</dd></dl></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0;margin-top:14px"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>XLSX 输出</span><h3>工作表结构 / 打印与封面</h3></div><div style="padding:14px 16px"><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div><p style="margin-bottom:8px">工作表结构（以表格类文件为例）：</p><ul style="margin:0;padding-left:18px;font-size:13px;color:inherit;line-height:1.7"><li>表头行冻结、加粗、带底色。</li><li>数据行交替底色，单元格自动换行。</li><li>列宽按内容自适应，数字列右对齐。</li></ul></div><div><p style="margin-bottom:8px">打印与封面：</p><ul style="margin:0;padding-left:18px;font-size:13px;color:inherit;line-height:1.7"><li>打印页眉：左文档名、右密级。</li><li>打印页脚：作者、日期、页码。</li><li>首页为封面：大标题 + 副标题 + 作者 + 日期 + 版本。</li></ul></div></div></div></div>

整套模板体系由以下文件组成，可通过`build_templates.py`脚本一键生成：

```
# 6 个核心设定文件 + 1 个生成指令文件
metadata.yaml      # 全局元数据（标题/作者/日期/版本/密级）
template.md        # Markdown 源稿模板
pdf-style.css      # PDF 输出样式
template.docx      # Word 模板（大词风格）
template.xlsx      # Excel 模板（封面 + 数据表）
generate.yaml      # 生成流程配置（或 prompt.md 自然语言指令）

# 文件命名规范（源稿）
YYYY-MM-DD_版本号.md
# 示例
2026-05-08_v1.0.md
```

> **自然语言生成入口**：规范同时提供一份可直接喂给大模型的自然语言 prompt（`prompt.md`），让 OpenClaw 按上述设定自动产出符合版式的文档；生成时图片用占位符、避免生成实心黑块。作者统一署名**EastSeaO**，版本号随修订递增。
