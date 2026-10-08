---
title: "SKILL 介绍 · Agent Skills 概念手册"
description: "概念手册 33 节：定义、由来，与 Prompt / Tool 的区别。"
pubDatetime: 2026-09-09
category: "AI与Agent"
kind: "手册"
tags: ["Skill", "Agent", "概念"]
---

GERVAS

SKILL 介绍

概念介绍 › Agent Skills ›**总览**

## SKILLAgent 从「会聊天」走向「能干活」的核心抽象

Skill 不是又一段 Prompt，而是**可被 Agent 动态发现、按需加载并执行的一套「程序化专业能力」**。截至 2026 年，Agent Skills 已从早期 Claude 生态扩展为跨 Agent 的开放标准：Anthropic 将其定义为由 SKILL.md、指令、脚本和资源组成的可组合能力单元；OpenAI 也用 Skills 扩展 Codex 的信息处理与实际计算机工作能力。本手册按原文 33 节结构，从概念、原理、架构讲到生命周期与未来方向。

类型

概念手册

结构

33 节 + 尾声

阅读

约 25 分钟

适用

Agent / Skill / Workflow 体系设计者

PART 01

导论

最重要的结论 · Agent = 人

PART 02

概念本体

是什么 · 为什么出现

PART 03

与相邻概念

Prompt · Tool · MCP · Workflow · Agent

PART 04

核心机制

渐进披露 · 定义 · 七层 · 示例

PART 05

组合与进化

组合 · 技能树 · 依赖

PART 06

边界与蒸馏

边界 · 知识库 · 案例 · 市场

PART 07

系统与架构

架构 · 判断 · 五层 · 治理

PART 08

总结

Agent OS · 未来 · 一句话

PART 01

导论

§01

### §01· 导论先给你一个最重要的结论

如果把一个 Agent 比喻成一个「人」，那么整套 Agent 体系里的每个组件都有清晰的人格对应——而 Skill 对应的是**专业技能 + SOP + 工作方法**：

| Agent 组件 | 类比「人」的 |
|---|---|
| LLM | 大脑 |
| System Prompt | 基本行为准则 |
| Context | 当前工作记忆 |
| Memory | 长期记忆 |
| Tool | 手和工具 |
| MCP | 工具连接协议 |
| Skill | **专业技能 + SOP + 工作方法** |
| Workflow | 工作流程 |
| Agent | 一个能够自主工作的员工 |
| Multi-Agent | 一个组织 |
| Runtime | 工作环境 |
| Evaluation | 绩效考核 |
| Learning | 培训 |
| Policy | 公司制度 |

结论

Skill 不是 Agent。Skill 是 Agent 所拥有的「可调用专业能力」。

例如一个「市场营销经理」Agent，不需要每次重新学习这些方法，它只需要完成一个循环：**发现 → 判断相关性 → 加载 → 执行 → 验证**。

```
Agent：市场营销经理

Skills：
├── 市场调研 Skill
├── 竞品分析 Skill
├── 用户画像 Skill
├── 产品定位 Skill
├── 包装文案 Skill
├── 小红书内容 Skill
├── SEO Skill
└── GEO Skill
```

PART 02

概念本体

§02–03

### §02· 概念本体Skill 到底是什么

目前主流 Agent Skills 的基本形式是一个文件夹，`SKILL.md`是核心入口：

```
skill-name/
│
├── SKILL.md
│
├── scripts/
│   ├── xxx.py
│   └── xxx.sh
│
├── references/
│   ├── guide.md
│   ├── rules.md
│   └── examples.md
│
└── assets/
    ├── template.docx
    ├── template.xlsx
    └── images/
```

官方架构的关键思想是**Progressive Disclosure（渐进式披露）**——不是把整个 Skill 全部塞进上下文，而是分层按需加载：

L1

Metadata

YAML frontmatter

Agent 一开始只知道「我有什么技能」——name 与 description，例如

market-research

及其职责描述。

L2

Instructions

SKILL.md 正文

真正需要使用时才加载：「这个技能怎么做」——目标、流程、规则。

L3

Resources

references/

还需要更深的信息时再读取：研究方法论、来源评估、竞品框架、报告模板等。

L4

Executable

scripts/

需要程序时调用：

scrape.py

、

analyze.py

、

generate_chart.py

、

validate.py

。

```
---
name: market-research
description: >
  Conduct structured market research, competitor analysis,
  trend analysis and evidence-based market reports.
---
```

所以一个 Skill 本质上可以是：

Knowledge + Instructions + Procedures + Tools + Code + Resources + Templates

Anthropic 官方也明确把 Skill 描述为包含 instructions、scripts、resources 的文件夹，并通过渐进式披露减少上下文负担（见文末来源 ①）。

### §03· 概念本体为什么 Skill 会出现

以前的 Agent 通常是`User → Prompt → LLM → Answer`：模型只能凭已有知识、你的 Prompt 和当前 Context 做事。让它「做一次竞品分析」，会立刻暴露三个问题：

问题 1 · 重复

每次都要重新告诉它：第一步做什么、哪些网站可信、如何判断数据、报告怎么写。

问题 2 · 不稳定

今天用方式 A，明天用方式 B，换一个模型又变成方式 C——工作方法没有沉淀。

问题 3 · 上下文浪费

把所有 SOP 塞进 System Prompt：100 个技能 × 每个 5,000 tokens = 巨大 Context，而绝大多数任务根本用不到。

Skill 的解决方式，是把 Agent 与一组可按需加载的能力连接起来：

Agent

──┬──

Skill A

Skill B

Skill C

Skill D

Skill E

→

按需加载

核心判断

Skill 的核心不是「增加 Prompt」，而是

把 Agent 的专业知识和程序化工作方法模块化

。

PART 03

与相邻概念

§04–08

### §04· 与相邻概念Skill 和 Prompt 最大的区别

这是最容易搞混的地方：Prompt 告诉模型**这一次**应该怎么做；Skill 把工作方法**永久封装**成可复用能力。

Prompt

· 一次性指令

Skill

· 能力封装

「你是一名专业市场分析师。请分析以下产品……要求：1. 分析市场规模 2. 分析竞品 3. 分析消费者 4. 给出策略。」

market-research/SKILL.md

规定：任何市场研究任务都走固定方法论。

用完即弃，下次任务要从头再来。

以后只要说「帮我研究虫草市场」，Agent 就自动调用这个 Skill。

质量取决于当次 Prompt 写得多好。

内部规定九步：定义研究问题 → 定义市场边界 → 优先一手资料 → 交叉验证 → 区分事实/推断/观点 → 建立竞争格局 → 建立消费者画像 → 输出结论 → 给出战略建议。

一句话

Prompt 是指令；Skill 是能力封装。

### §05· 与相邻概念Skill 和 Tool 完全不是一个东西

Agent 做市场调研时：Skill 告诉它**怎么研究**，Tool 让它**能够搜索**。一个 Market Research Skill 内部会调用搜索网页、查询数据库、读取 PDF、分析 Excel、生成报告等工具。

直观例子

Excel 是工具，财务分析是技能。

Agent 有 Excel 工具，不代表它会做专业财务分析；反过来，有财务分析 Skill 但没有 Excel / Python / 数据库工具，也无法处理大型数据。

Skill + Tool → 真正可执行能力

### §06· 与相邻概念Skill 和 MCP 又是什么关系

MCP 是「连接工具和外部世界的标准接口」：Agent 通过 MCP 接上 GitHub、Notion、Google Drive、数据库、CRM。而 Skill 决定接上之后**如何使用这些工具完成任务**。

MCP

Skill

解决「

能不能接上

」——提供外部服务和数据访问。

解决「

接上以后怎么干活

」——提供完成任务所需的程序性知识。

官方文档也明确区分：MCP 提供外部服务和数据访问；Skill 提供完成任务所需要的程序性知识，两者可以组合使用（见文末来源 ②）。

### §07· 与相邻概念Skill 和 Workflow 的区别

Skill 解决「**怎么做一类事情**」，Workflow 解决「**这几件事按什么顺序完成**」。

例如一个 SEO Skill 包含关键词研究、搜索意图分析、内容结构设计、内链策略、SERP 分析、E-E-A-T 检查；而一个「产品上市 Workflow」是：

市场调研

→

消费者分析

→

竞品分析

→

产品定位

→

包装策略

→

内容营销

→

渠道投放

→

复盘

Workflow 可以调用多个 Skill：Market Research Skill、Consumer Insight Skill、Product Positioning Skill、Packaging Skill、SEO Skill、Marketing Skill……

一句话

Skill 是能力模块；Workflow 是能力编排。

### §08· 与相邻概念Skill 和 Agent 又是什么关系

Agent = LLM + Instructions + Tools + Memory + Skills + Runtime + Planning + Evaluation

Skill 本身并不是 Agent。「SEO Skill」不能自主决定「我今天要研究一下百度 SEO」；但「SEO Agent」可以——因为它拥有目标、规划、Skill、Tool、Memory 和执行能力。

一句话

Skill = 能力；Agent = 能力的自主使用者。

PART 04

核心机制

§09–13

### §09· 核心机制Skill 最核心的创新：Progressive Disclosure

传统 Agent 是「启动 → 加载所有知识 → 巨大 Context → 开始工作」；Skill 架构把加载变成一条按需推进的链：

1. 启动 —— 只加载 Skill 名称 + 描述 （Metadata）

1. 识别任务 —— Agent 把 Skill Index 与用户任务对上

1. Skill Matching —— 发现相关 Skill

1. Load SKILL.md —— 加载指令层 （Instructions）

1. Load References —— 发现并读取需要的参考 （Resources）

1. Run Scripts —— 发现并执行需要的程序 （Code）

1. Execute Task —— 完成任务

画成结构就是：`Agent`同时连接`Skill Index`与`User Task`，两者汇入`Skill Matching`，再依次经过`Load SKILL.md → Load References → Run Scripts → Execute Task`。Anthropic 把它明确设计成多层加载：Metadata → Instructions → Resources / Code（来源 ①）。

推论

Skill 本质上也是一种 Context Engineering 架构。

### §10· 核心机制Skill 为什么能够「教会」Agent

LLM 本身已经知道「什么是市场调研 / SEO / Excel / 项目管理」；它不一定知道的是**你公司的**市场调研方法、SEO 标准、包装设计流程、品牌语言、审核规则、供应商评估方法。Skill 恰好把这一段补上：

隐性经验

→

显性化

→

结构化

→

程序化

→

机器可执行化

Knowledge → Procedure → Capability

知识 → 方法 → 流程 → 技能 → Agent Capability

### §11· 核心机制所以 Skill 本质上是什么

定义 · Procedural Knowledge Package

Agent Skill 是一种

可发现、可加载、可组合、可执行

的程序性知识封装（Procedural Knowledge Package），用于将特定领域的知识、工作方法、操作规范、资源和工具调用方式，转化为 Agent 可以按需调用的能力模块。

Discoverable

能够被 Agent 发现。

Loadable

需要的时候加载。

Composable

多个 Skill 可以组合。

Executable

可以真正执行。

Reusable

不同任务反复使用。

Portable

跨 Agent / 平台复用。

目前 Agent Skills 已经被明确作为开放标准发展，而不是某一家 Agent 的私有 Prompt 格式（来源 ②）。

### §12· 核心机制一个真正生产级 Skill 应该包含什么

建议把 Skill 分成七层：

1

Identity

身份

name、description——它是什么。

2

Intent

意图

When to use / When NOT to use——什么时候用、什么时候不用。

3

Knowledge

知识

concepts、rules、domain knowledge——领域概念与规则。

4

Procedure

流程

workflow、steps、decision rules——工作流与决策规则。

5

Resources

资源

references、templates、examples——参考资料与模板。

6

Execution

执行

scripts、tools、APIs——可执行部分。

7

Validation

验证

quality checks、constraints、evaluation——质量校验。

官方最基本的规范要求 SKILL.md 至少包含 name 和 description；复杂 Skill 则可以继续向下引用资源和代码（来源 ③）。

### §13· 核心机制一个真实 Skill 示例：consumer-research

```
consumer-research/
│
├── SKILL.md
│
├── references/
│   ├── consumer-analysis.md
│   ├── persona-framework.md
│   ├── interview-method.md
│   └── evidence-rules.md
│
├── scripts/
│   ├── clean_data.py
│   └── analyze_survey.py
│
└── assets/
    └── consumer-report-template.md
```

```
---
name: consumer-research
description: >
  Conduct structured consumer research, consumer segmentation,
  persona construction, demand analysis and insight extraction.
  Use when analyzing customers, consumer needs, surveys,
  interviews, reviews or market demand.
---
```

```
# Consumer Research

## Objective
Transform raw consumer information into evidence-based
consumer insights.

## Workflow
1. Define research question.
2. Identify target consumer.
3. Collect evidence.
4. Separate facts from assumptions.
5. Segment consumers.
6. Identify needs and pain points.
7. Extract behavioral patterns.
8. Build consumer personas.
9. Generate actionable insights.

## Rules
- Do not treat assumptions as facts.
- Distinguish quantitative and qualitative evidence.
- Prioritize primary evidence.
- Explicitly identify uncertainty.
- Do not fabricate consumer data.

## Resources
For segmentation:        read references/persona-framework.md
For evidence evaluation: read references/evidence-rules.md
For survey analysis:     use scripts/analyze_survey.py
```

这已经不是普通 Prompt，而是一个可以复用的「消费者研究能力模块」。

PART 05

组合与进化

§14–16

### §14· 组合与进化Skill 可以组合

这是它真正强大的地方。一个「产品战略 Agent」拥有 Market Research、Consumer Research、Competitor Analysis、Product Positioning、Pricing Strategy、Packaging Strategy 六个 Skill。当用户说「帮我设计一款高端有机黑枸杞产品」，Agent 可能自动形成任务链：

Market Research

→

Consumer Research

→

Competitor Analysis

→

Product Positioning

→

Packaging Strategy

→

Pricing Strategy

多个 Skill 组合起来完成复杂任务——这就是**Composable Skills**。官方也把「可组合」列为 Skills 的核心特征之一（来源 ④）。

### §15· 组合与进化Skill 可以形成「技能树」

```
Business Agent
│
├── Strategy
│   ├── Market Research
│   ├── Competitor Analysis
│   ├── SWOT
│   └── Business Model
│
├── Marketing
│   ├── SEO
│   ├── GEO
│   ├── Content Marketing
│   └── Social Media
│
├── Product
│   ├── Product Research
│   ├── Product Positioning
│   ├── Packaging
│   └── Pricing
│
├── Sales
│   ├── Lead Generation
│   ├── Customer Analysis
│   └── Sales Proposal
│
└── Operations
    ├── Procurement
    ├── Supplier Management
    ├── Inventory
    └── Cost Control
```

这时候 Skill 就不再是几个 Prompt，而开始形成**Agent Skill Graph**。

### §16· 组合与进化Skill 甚至可以形成「技能依赖关系」

技能依赖技能：

SEO Content Skill

requires→

Keyword Research Skill

→

Search Intent Skill

→

Content Structure Skill

→

SEO Validation Skill

再往下延伸：`Skill A → Skill B → Skill C → Tool → External Data`。这已经开始接近**Agent Capability Runtime**。

PART 06

边界与蒸馏

§17–21

### §17· 边界与蒸馏Skill 还有一个非常重要的属性：边界

好的 Skill 一定不是「什么都能做」，而是**定义清晰的能力边界**。以 SEO Skill 为例：

能做

不负责

关键词研究 / 搜索意图 / 内容结构 / SEO 审查 / 内链建议

广告投放 / 品牌战略 / 视觉设计 / 销售管理

为什么？因为 Skill 越大：`Skill 范围 ↑ → 触发边界模糊 → 上下文增加 → 执行不稳定`。

原则

Skill 应该像「一个专业岗位能力」，而不是「万能助手」。

### §18· 边界与蒸馏Skill ≠ 知识库

Knowledge Base

· 回答「知道什么」

Skill

· 回答「知道怎么做什么」

公司产品资料 / 历史销售数据 / 行业报告 / 品牌资料

如何分析销售数据 / 如何研究市场 / 如何写品牌策略 / 如何进行供应商评估

Knowledge = What Skill = How

这也是为什么 Skill 特别适合**把一个人的工作经验「数字化」**。

### §19· 边界与蒸馏这和「蒸馏」高度相关

一个专家身上有：知识、判断、方法、SOP、经验、案例、禁忌、决策逻辑。通过蒸馏，可以把它们转化为 Skill：

Expert

→

Observation

→

Pattern Extraction

→

Procedure Extraction

→

Decision Rules

→

Skill

```
expert-skill/
├── SKILL.md
├── references/
├── examples/
├── scripts/
└── evaluation/
```

战略价值

Skill 可以看作「专家经验的程序化蒸馏结果」。

这是 Skill 最有战略价值的地方。

### §20· 边界与蒸馏再往前一步：Skill ≈「可执行知识」

书、文章、文档、课程属于**Declarative Knowledge**——「知道是什么」；Skill 更接近**Procedural Knowledge**——「知道怎么做」。

一本营销书

一个 Skill

告诉你：消费者需要被细分。

告诉 Agent：Step 1 收集用户数据 → Step 2 按人口属性初分 → Step 3 按行为二次划分 → Step 4 寻找需求差异 → Step 5 建立 Persona → Step 6 验证 Persona。

Knowledge → Procedure → Skill

### §21· 边界与蒸馏Skill 最终可以变成「能力市场」

想象一个 Agent Skill Store，按行业组织：Finance / Legal / Marketing / Research / Programming / Design / Manufacturing / Procurement / Medicine / Education。一个基础 Agent 加上 50 Skills、20 Tools、10 MCP 和 Memory，就可以配置成 Research Agent、Marketing Agent、Finance Agent、Procurement Agent——比「一个 Agent = 一个 Prompt」先进得多。

OpenAI 已经明确展示了这种方向：Codex 通过 Skills 扩展到信息综合、问题解决、写作和计算机实际工作，内部已使用大量 Skills 来标准化复杂工作（来源 ⑤）。

PART 07

系统与架构

§22–31

### §22· 系统与架构从架构角度看，Skill 位于哪里

如果构建一个真正的 Agent Runtime，建议架构如下：

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>USER / GOAL</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>AGENT ORCHESTRATOR</div><div>Goal · Planning · Reasoning · Policy</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL ROUTER</div><div>skill matching &amp; dispatch</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL LAYER</div><div>Strategy · Research · Marketing · Finance · Coding · Design · Procurement · SEO · GEO</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>TOOL LAYER</div><div>Browser · Python · Files · APIs · Database · Git · Search · MCP</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>RUNTIME</div><div>Filesystem · Sandbox · Network</div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Memory / Knowledge / Data</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Evaluation / Observability</div>

### §23· 系统与架构真正高级的 Skill 应该拥有「判断逻辑」

只写「第一步……第二步……第三步……」的 Skill 其实只是 SOP。高级 Skill 应该包含条件判断：

```
IF   data_source == primary      THEN confidence = high
IF   data_source == secondary    THEN confidence = medium
IF   source conflicts            THEN perform cross_validation
IF   evidence < threshold        THEN mark conclusion as uncertain
```

这时候 Skill 才真正开始拥有**Decision Logic**。

### §24· 系统与架构一个成熟 Skill 可以分成 5 层

1

Knowledge

我知道什么。

2

Procedure

我怎么做。

3

Decision

我如何判断。

4

Execution

我用什么执行。

5

Evaluation

我如何判断做对了。

Know → Do → Decide → Execute → Verify

这比简单的「Prompt → Answer」强一个数量级。

### §25· 系统与架构Skill 自己可以被评估

```
evaluation/
├── test_cases.json
├── expected_output.md
└── evaluator.py
```

以 SEO Skill 为例：输入某个产品关键词、要求生成 SEO 策略，然后检查——搜索意图是否正确、关键词是否合理、标题是否符合规则、是否存在关键词堆砌、是否有事实幻觉。

Skill

→

Execute

→

Evaluate

→

Score

这样 Skill 就从 Prompt Engineering 进一步变成**Capability Engineering**。

### §26· 系统与架构Skill 的生命周期

一个成熟的 Skill 不应该是写完就结束：

设计

→

实现

→

测试

→

部署

→

使用

→

观察

→

发现失败

→

优化

→

版本升级

→

重新测试

Skill v1 → Skill v1.1 → Skill v1.2 → Skill v2

Skill Performance → Failure Analysis → Skill Improvement → New Version

这就开始进入 Memory & Learning Layer 的范畴。

### §27· 系统与架构Skill + Memory 是一个非常强的组合

两者千万不要混淆：

Skill

· 「应该怎么做」

Memory

· 「过去发生过什么」

包装采购 Skill：1. 收集供应商报价 2. 对比 MOQ 3. 对比模具费 4. 对比运输成本 5. 进行 TCO 分析。

供应商 A 过去报价 ¥1.85；供应商 B 报价 ¥1.72；供应商 B 曾发生交付延期。

Skill + Memory → 更好的决策

### §28· 系统与架构Skill + Memory + Tool = 真正的工作能力

Skill · 知道怎么做

+

Memory · 知道过去发生什么

+

Tool · 能够真正执行

Agent = Reasoning + Skill + Memory + Tool + Runtime

这已经是现代 Agent 的核心结构。

### §29· 系统与架构Skill 和「Agent Persona」也不一样

「你是一位世界级营销专家」描述的是**是谁**（Persona）；「Marketing Skill」描述的是**怎么工作**（Skill）。这是一个非常漂亮的 Agent 架构分层：

| 维度 | 回答的问题 | 对应对象 |
|---|---|---|
| Persona | 我是谁？ | Who |
| Skill | 我怎么做？ | How |
| Knowledge | 我知道什么？ | What |
| Goal | 我为什么做？ | Why |
| Tool | 我拿什么做？ | With what |
| Memory | 以前发生过什么？ | What happened before |

### §30· 系统与架构如果给 Skill 下一个最简洁的公式

SKILL = DOMAIN KNOWLEDGE + PROCEDURE + DECISION RULES

+ EXECUTION METHOD + VALIDATION

AGENT = GOAL + REASONING + SKILLS + TOOLS + MEMORY

+ RUNTIME + EVALUATION

### §31· 系统与架构对于 Agent 系统：把 Skill Layer 独立出来

在 Prompt Layer / Schema Layer / Workflow Layer / Runtime Layer / Agent Library / Tool Integration / Memory & Learning 之上，建议把 Skill Layer 独立成层：

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>AI ORGANIZATION</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>Organization → Agent Layer</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL LAYER</div><div>Knowledge · Procedure · Decision · Execution · Evaluation</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>Workflow</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>Tool / MCP</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>Runtime</div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Memory / Knowledge / Data</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Evaluation / Learning</div>

这个结构非常适合「OPC → AI 公司 → 自主组织」的演进路线。

PART 08

总结

§32–尾声

### §32· 总结把整个 Agent 世界压缩成一张表

| 层 | 核心问题 | 对应对象 |
|---|---|---|
| Goal | 我要完成什么？ | Goal |
| Persona | 我是谁？ | Agent |
| Knowledge | 我知道什么？ | Knowledge |
| Skill | 我怎么做？ | Skill |
| Decision | 我怎么判断？ | Rules |
| Workflow | 先做什么后做什么？ | Workflow |
| Tool | 我拿什么做？ | Tool |
| MCP | 怎么连接外部世界？ | MCP |
| Memory | 以前发生过什么？ | Memory |
| Runtime | 在哪里执行？ | Runtime |
| Evaluation | 怎么知道做对了？ | Eval |
| Learning | 如何变得更好？ | Learning |
| Organization | 谁和谁协作？ | Multi-Agent |
| Economy | 如何自主竞争/交易？ | AI Economy |

这张表其实就是一个**Agent Operating System 的雏形**。

### §33· 总结Skill 最值得关注的未来方向

未来真正重要的可能不是「谁的模型参数更多」，而是**谁拥有更强的 Skill Ecosystem**。因为模型本身会越来越通用，真正产生差异的东西会逐渐变成：

Model + Skill + Tools + Memory + Data + Workflow + Evaluation

General Intelligence

→

Specialized Capability

→

Professional Agent

→

Autonomous Organization

这也是为什么 OpenAI 已经在 Codex 中把 Skills 当成从「代码生成」走向「计算机实际工作」的重要扩展机制（来源 ⑤）。

### 尾声用一句话理解 Skill

Prompt 告诉 AI 一次应该怎么回答；Skill 把一项专业工作的方法论、流程、判断规则、资源和执行方式封装起来，让 Agent 能够在需要时自动调用并重复完成这类工作。

Skill 很可能就是未来「把专家能力蒸馏成 Agent 可执行能力」的核心载体。

↑ 回到开头

§01 最重要的结论

↓ 参考资料

来源与说明

来源 · Sources

1. Anthropic Engineering — Equipping agents for the real world with Agent Skills

1. Claude Help Center — What are skills?

1. Claude Platform Docs — Agent Skills overview

1. Claude Blog — Skills

1. OpenAI — Introducing the Codex app

内容依据用户提供的《SKILL介绍》原文 33 节整理；结构与编号 1:1 对应。本页为单文件 HTML，双击即可打开。
