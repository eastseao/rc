---
title: "生产级 Agent Skill 架构规范"
description: "工程层规范 35 节：14 模块标准模型、Contract / Schema 与生命周期。"
pubDatetime: 2026-09-09
category: "AI与Agent"
kind: "手册"
tags: ["Skill", "架构", "规范"]
---

GERVAS

架构规范

概念介绍 › Agent Skills ›**生产级架构规范**· 前篇[SKILL 介绍](../skill/)

## SKILL SPEC生产级 Agent Skill 架构规范

上一篇[SKILL 介绍](../skill/)讲清了 Skill 是什么；本篇进入工程层——一个 Skill 到底应该有哪些组件、目录、Schema、路由、依赖、版本与评估机制，如何从「Prompt 文件」升级成真正的 Agent Capability。全文 35 节 + 2 篇结语，编号与原文一一对应。

类型

架构规范

结构

35 节 + 2 篇结语

阅读

约 30 分钟

适用

Agent 能力平台设计者

PART 01

总纲

结论 · 标准模型 · 目录

PART 02

能力基座

Identity → Decision

PART 03

判断与执行

判断 · 执行 · 资源 · 状态

PART 04

评估与治理

评估 · 基准 · 安全 · 可观测

PART 05

系统组件

Registry · Router · 依赖 · 组合

PART 06

经验与进化

Memory · Learning · 生命周期

PART 07

工程落地

示例 · Manifest · 成熟度 · OS

PART 08

结语

一句话 · v1.0 路线

PART 01

总纲

§01–03

### §01· 总纲先给结论：生产级 Skill ≠ SKILL.md

很多人理解的 Skill 只有一个`SKILL.md`——那只能算**Level 1 Skill**。真正生产级的 Skill 是一条完整的链路：

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL REGISTRY</div><div>技能注册 / 索引</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL ROUTER</div><div>技能发现 / 路由</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL</div><div>Identity · Intent · Knowledge · Procedure · Decision Rules · Tools · Resources · State · Validation · Evaluation</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Memory</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Workflow</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Tools</div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL RUNTIME</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>RESULT / ARTIFACT</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>EVALUATION</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>LEARNING / VERSION</div></div>

Skill = Metadata + Knowledge + Procedure + Decision + Execution + State + Validation + Evaluation

结论

这八个部分构成一个完整的能力单元。

### §02· 总纲先建立一个 Skill 的「标准模型」

建议系统统一采用以下 14 个模块，每个模块回答一个问题：

| 模块 | 解决的问题 |
|---|---|
| Identity | 我是谁？ |
| Intent | 什么时候应该使用我？ |
| Contract | 我的输入输出是什么？ |
| Knowledge | 我知道什么？ |
| Procedure | 我怎么做？ |
| Decision | 我怎么判断？ |
| Execution | 我如何真正执行？ |
| Resources | 我可以参考什么？ |
| State | 我执行过程中记住什么？ |
| Validation | 我如何检查结果？ |
| Evaluation | 我的能力到底好不好？ |
| Security | 我允许做什么？ |
| Observability | 我执行过程中发生了什么？ |
| Versioning | 我现在是哪一版？ |

对照

这已经和普通 Prompt 有本质区别。

### §03· 总纲生产级 Skill 的目录结构

```
skills/
│
├── skill-name/
│   │
│   ├── SKILL.md
│   ├── manifest.yaml
│   ├── schema/
│   │   ├── input.schema.json
│   │   └── output.schema.json
│   │
│   ├── instructions/
│   │   ├── procedure.md
│   │   ├── decision-rules.md
│   │   └── quality-rules.md
│   │
│   ├── references/
│   │   ├── knowledge.md
│   │   ├── methodology.md
│   │   ├── standards.md
│   │   └── examples.md
│   │
│   ├── scripts/
│   │   ├── execute.py
│   │   ├── validate.py
│   │   └── transform.py
│   │
│   ├── templates/
│   │   ├── report.md
│   │   └── output.json
│   │
│   ├── tests/
│   │   ├── cases/
│   │   ├── expected/
│   │   └── evaluator.py
│   │
│   └── policies/
│       ├── permissions.yaml
│       └── safety.yaml
```

重要原则

不要为了「完整」而把所有文件都创建出来。

Skill 应该遵循 Progressive Disclosure（渐进式披露）。

简单 Skill

SKILL.md

复杂 Skill

SKILL.md + references/ + scripts/

生产级 Skill

SKILL.md + manifest + schema + evaluation + policy + observability

PART 02

能力基座

§04–09

### §04· 能力基座第一层：Identity

Skill 首先必须有自己的身份：

```
name: competitor-analysis
version: 1.4.0
description: >
  Analyze competitors, competitive positioning,
  product differences, pricing and strategic advantages.
```

其中最重要的是`name`、`description`、`version`三项。Skill Router 不是读取全部 Skill 后再决定，而是：

User Task

→

Skill Metadata

→

Candidate Skills

关键判断

Description 实际上是 Skill 的「路由接口」。

### §05· 能力基座第二层：Intent

生产级 Skill 必须明确边界——什么时候用、什么时候不能用：

```
when_to_use:
  - 用户要求分析竞争对手
  - 用户要求比较产品
  - 用户要求竞争格局分析
  - 用户要求竞品价格比较

when_not_to_use:
  - 纯市场规模预测
  - 财务审计
  - 用户画像
  - 产品视觉设计
```

为什么非常重要？因为`Skill 数量 ↑ → Router 选择难度 ↑`。如果没有边界，SEO Skill、Marketing Skill、Content Skill、GEO Skill、Brand Skill 很容易全部被激活，最后：

Skill 数量 ↑

→

触发边界模糊

→

Context 爆炸

### §06· 能力基座第三层：Skill Contract

这是很多现有 Skill 最缺失的一层。Skill 不应该只是「请按照以下方法做」，而应该有明确的`Input → Processing → Output`契约：

```
input:
  type: object
  required:
    - product
    - market

output:
  type: object
  required:
    - competitors
    - positioning
    - opportunities
```

例如输入：

```json
{
  "product": "有机黑枸杞饮料",
  "market": "中国",
  "objective": "寻找高端市场机会"
}
```

输出：

```json
{
  "competitors": [],
  "market_structure": {},
  "positioning": {},
  "opportunities": []
}
```

分水岭

没有 Schema 的 Skill，本质上还是自然语言 Prompt。

有了 Schema，Skill 开始成为机器可组合的 Capability。

### §07· 能力基座第四层：Knowledge

这里存放 Skill 的专业知识：

```
references/
├── methodology.md
├── terminology.md
├── industry-rules.md
├── standards.md
└── examples.md
```

原则

不要把所有知识塞进 SKILL.md。

应该由 SKILL.md 告诉 Agent：「如果需要 X，请读取 references/X」：

```
## Knowledge

For consumer segmentation:
read references/segmentation.md

For evidence evaluation:
read references/evidence-rules.md
```

这样才能做到「需要什么 → 加载什么」，而不是「所有知识 → 全部加载」。

### §08· 能力基座第五层：Procedure

Procedure 回答「这个技能到底怎么干活」：

```
## Procedure

### Step 1
Define the research question.

### Step 2
Define market boundaries.

### Step 3
Collect evidence.

### Step 4
Cross-check sources.

### Step 5
Analyze competitors.

### Step 6
Identify strategic opportunities.

### Step 7
Generate recommendations.

### Step 8
Validate output.
```

但生产级 Skill 不应该只有线性 SOP——真实工作经常是条件分支：`如果 A → 做 B；如果 C → 做 D；如果没有数据 → 改变策略；如果数据冲突 → 重新验证`。所以还需要下一层。

### §09· 能力基座第六层：Decision Engine

这是 Skill 从「教程」升级成「专家能力」的关键：

```
rules:
  - condition:
      source_type: primary
    action:
      confidence: high

  - condition:
      source_type: secondary
    action:
      confidence: medium

  - condition:
      sources_conflict: true
    action:
      require_cross_validation: true

  - condition:
      evidence_count: 0
    action:
      mark_as_unknown: true
```

Knowledge + Procedure + Decision Rules → 接近专家能力

PART 03

判断与执行

§10–14

### §10· 判断与执行为什么 Decision Rules 特别重要

专家真正值钱的地方往往不是「知道什么」，而是**「在什么情况下做什么决定」**。以一个优秀采购人员为例：

普通知识

· 知道什么

真正的能力

· 怎么决定

知道供应商报价

知道 MOQ

知道模具费

知道运输费

如果 A 价格低 10% 但交期风险高 → 不一定选择 A

如果 B 价格高 5% 但稳定性高 → B 可能更优

如果采购量达到 100 万 → 可以重新议价

推论

这就是

Decision Skill

。「采购 Agent」这类场景非常适合 Skill 化。

### §11· 判断与执行第七层：Execution

Knowledge + Procedure + Decision 仍然不够，Agent 必须真正执行。执行资产包括`scripts/`（scrape.py、calculate.py、transform.py、generate_report.py、validate.py）以及 Tools、MCP、API、Browser、Python、Filesystem、Database 等通道：

Skill

→

Decision

→

Tool

→

Action

以 Competitor Analysis Skill 为例：

搜索竞品

→

Browser / Search Tool

→

获取数据

→

Python

→

价格分析

→

生成报告

### §12· 判断与执行第八层：Resources

Resources 是 Skill 的「外挂大脑」：

```
resources/
├── industry/
├── standards/
├── examples/
├── templates/
└── datasets/
```

Knowledge

Resources

Skill 自己需要

理解

的知识。

Skill 工作时可以

查询

的资料。

例如一个 Packaging Skill：references/ 放 packaging-methodology.md、material-selection.md、packaging-design-rules.md；resources/ 放 supplier-database.xlsx、packaging-specifications.pdf、cost-reference.xlsx。

### §13· 判断与执行第九层：State

高级 Skill 很容易被忽略的一层。Skill 执行不是永远一次完成：

Task

→

Step 1

→

Step 2

→

等待外部信息

→

Step 3

→

Step 4

所以需要 Skill State：

```json
{
  "status": "running",
  "step": 4,
  "completed_steps": [
    "research",
    "competitor_analysis"
  ],
  "pending_steps": [
    "pricing_analysis"
  ]
}
```

能力

这让 Skill 支持

Long-running Tasks

。

### §14· 判断与执行第十层：Validation

一个真正的 Skill 必须知道「什么叫做完成」。以 SEO Skill 为例：

- ✓ 标题存在

- ✓ 主关键词存在

- ✓ 搜索意图匹配

- ✓ 内容结构完整

- ✓ 无虚假数据

- ✓ 引用存在

- ✓ 没有关键词堆砌

Execute

→

Validate

→

Pass / Fail

·

Fail → Retry → Repair → Validate

闭环

这就形成

Self-Correction Loop

（自我修正回路）。

PART 04

评估与治理

§15–18

### §15· 评估与治理第十一层：Evaluation

Validation 和 Evaluation 不一样：

Validation

Evaluation

检查：

这一次

是否符合规则？

检查：

这个 Skill 本身

到底好不好？

例如 Skill v1.2 的能力画像（示例指标）：

| 指标 | 数值 |
|---|---|
| Task Success Rate | 82% |
| Accuracy | 91% |
| Tool Efficiency | 76% |
| Hallucination Rate | 3% |
| User Satisfaction | 88% |
| Average Cost | $0.17 |
| Average Time | 42 sec |

定义

这才是真正的

Skill Performance

。

### §16· 评估与治理Skill Evaluation 应该建立 Benchmark

```
tests/
│
├── cases/
│   ├── case001.json
│   ├── case002.json
│   ├── case003.json
│   └── case004.json
│
├── expected/
│
└── evaluator.py
```

100 个测试任务

→

Skill v1

→

Score 82%

·

修改后 v1.1

→

Score 89%

价值

这样你就可以知道：

Skill 的修改到底有没有变好。

### §17· 评估与治理第十二层：Security / Permission

生产环境必须考虑「Skill 可以做什么」：

```
permissions:
  filesystem:
    read: true
    write: true
  network:
    access: true
  shell:
    execute: false
  database:
    read: true
    write: false
  external_api:
    allowed:
      - github
      - google
```

Skill + Tool = Action

安全边界

Skill 可能具有真实世界的执行能力——这时候

Skill 本身就必须是一个安全边界

。

### §18· 评估与治理第十三层：Observability

生产级 Skill 必须可以被观察。一次执行应记录：

```
execution_id
├── selected skill
├── skill version
├── input
├── context loaded
├── tools called
├── decisions
├── output
├── validation
├── errors
├── latency
└── token / cost
```

例如一次执行：

```
execution_id: exec_8f3a92
skill:      competitor-analysis
version:    1.4.2
duration:   38.2s
tools:      search × 12, python × 2
context:    18,420 tokens
validation: PASS
score:      91
```

运营

这样你才能真正运营 Skill。

PART 05

系统组件

§19–24

### §19· 系统组件Skill Registry

当 Skill 数量达到 10、50、100、1000 个，就不能靠文件夹管理了，需要 Skill Registry：

```json
{
  "id": "skill.competitor-analysis",
  "name": "Competitor Analysis",
  "version": "1.4.2",
  "domain": "marketing",
  "tags": [
    "competitor",
    "market",
    "strategy"
  ],
  "status": "active",
  "quality_score": 0.91
}
```

Registry 负责：

发现

搜索

版本

依赖

权限

状态

评分

### §20· 系统组件Skill Router

这是整个 Skill 系统的「大脑」。用户说：「帮我分析有机黑枸杞饮料的竞品。」Router 的工作流：

User Intent

—— 理解用户意图

Task Classification

—— 任务分类

Skill Retrieval

—— 技能检索

Candidate Skills

—— 得到候选集

Competitor Analysis

0.94

Market Research

0.83

Consumer Research

0.61

Product Positioning

0.52

于是**Competitor Analysis**成为主 Skill，**Market Research**可能作为辅助 Skill。

### §21· 系统组件Skill Router 最好不是简单关键词匹配

初级

高级

keyword matching（关键词匹配）

semantic retrieval 语义检索

+ metadata filtering 元数据过滤

+ capability matching 能力匹配

+ dependency resolution 依赖解析

+ cost optimization 成本优化

+ policy filtering 策略过滤

Task

→

Intent

→

Candidate Skills

→

Capability Matching

→

Policy Check

→

Dependency Resolution

→

Skill Selection

### §22· 系统组件Skill Dependency

复杂 Skill 往往依赖其他 Skill：

```
Product Launch Skill
│
├── Market Research Skill
├── Consumer Research Skill
├── Competitor Analysis Skill
├── Product Positioning Skill
├── Pricing Skill
└── Marketing Skill
```

Registry 应该记录依赖：

```
dependencies:
  - skill: market-research
    version: ">=1.2"

  - skill: competitor-analysis
    version: ">=2.0"

  - skill: pricing-analysis
    version: "^1.5"
```

Skill

→

Dependency Graph

→

自动加载依赖

### §23· 系统组件Skill Composition

再进一步：多个 Skill 可以临时组合成 Composite Skill。

Organic Beverage Launch = Market Research + Consumer Research + Competitor Analysis + Product Positioning + Packaging + Pricing

系统可以动态生成**Skill Composition Plan**，而不是人为提前写死。这就是**Dynamic Capability Composition**。

### §24· 系统组件Skill 和 Workflow 最终应该这样结合

不要把 Skill 和 Workflow 混为一谈：

Skill

Workflow

Agent

能力

编排

自主决策者

执行关系：

Agent · 判断目标

→

选择 Workflow

→

Workflow 调用 Skills

→

Skills 调用 Tools

→

Runtime 执行

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>AGENT</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>PLANNER</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>WORKFLOW</div><div>Skill A · Skill B · Skill C · Skill D</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>TOOL / MCP</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>RUNTIME</div></div>

PART 06

经验与进化

§25–29

### §25· 经验与进化Skill Memory

Skill 不应该只有 Static Knowledge，还可以拥有 Skill Memory。例如采购 Skill 的历史经验：

供应商 A

供应商 B

交付稳定 · 价格中等

价格最低 · 曾出现延期

另有供应商 C：小批量能力强。于是 Skill + Memory 开始具备**经验型能力**。

### §26· 经验与进化Skill Learning

Skill

→

Execution

→

Failure

→

Evaluation

→

Learning

→

Skill Update

例如：Skill v1.3 成功率 81%，分析发现定价错误主要来自「未考虑渠道成本」；Learning 的动作是**增加 Channel Cost Rule**；结果 Skill v1.4 成功率升到 89%。

定义

这就是

Self-Improving Skill

（自改进技能）。

### §27· 经验与进化Skill 的「蒸馏」架构

这与「能不能把专家能力蒸馏成 Skill」直接连接。可以设计：

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>EXPERT</div><div>Documents · Conversations · Decisions · Work Logs · Examples · Corrections · Outcomes</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL DISTILLATION</div><div>Knowledge / Procedure / Decision / Rule / Evaluation Extraction</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL v1</div></div>

Skill v1

→

真实执行

→

专家纠正

→

Learning

→

Skill v2

一个专家不是被复制成一个 Persona，而是被蒸馏成一套 Skill System。

### §28· 经验与进化生产级 Skill 的完整生命周期

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL SOURCE</div><div>专家 / 书籍 / SOP</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>DISTILLATION → DESIGN → BUILD → TEST</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>REGISTRY → ROUTER → RUNTIME</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>EXECUTE → VALIDATE → EVALUATE</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Success → Memory</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Failure → Analysis</div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>LEARNING → SKILL UPDATE → NEW VERSION</div></div>

定义

这才是一套真正完整的

Skill Lifecycle

。

### §29· 经验与进化Skill Runtime 的执行模型

1 DISCOVER

→

2 SELECT

→

3 LOAD

→

4 PLAN

→

5 EXECUTE

6 OBSERVE

→

7 VALIDATE

→

8 EVALUATE

→

9 STORE

→

10 LEARN

| 阶段 | 作用 |
|---|---|
| Discover | 找技能 |
| Select | 选技能 |
| Load | 加载上下文 |
| Plan | 制定执行计划 |
| Execute | 执行 |
| Observe | 记录过程 |
| Validate | 检查结果 |
| Evaluate | 评价能力 |
| Store | 保存经验 |
| Learn | 改进 Skill |

PART 07

工程落地

§30–35

### §30· 工程落地一个生产级 SKILL.md 可以长什么样

一个更接近生产环境的版本：

```
---
name: competitor-analysis
version: 1.4.0
description: >
  Analyze competitors, products, pricing, positioning,
  strengths, weaknesses and strategic opportunities.
  Use when a task requires competitive intelligence
  or competitor comparison.

domain: marketing
tags:
  - competitor
  - strategy
  - market

inputs:
  required:
    - product
    - market

outputs:
  required:
    - competitors
    - positioning
    - opportunities

dependencies:
  - market-research >=1.2.0

permissions:
  network: true
  filesystem: read
  shell: false
---

# Competitor Analysis Skill

## Purpose

Transform competitor information into
evidence-based competitive insights.

## When to Use

Use when:
- analyzing competitors
- comparing products
- analyzing pricing
- identifying competitive gaps

## Do Not Use

Do not use for:
- financial auditing
- legal analysis
- product visual design

## Procedure

1. Define competitive scope.
2. Identify competitors.
3. Collect primary evidence.
4. Collect secondary evidence.
5. Normalize competitor data.
6. Compare products.
7. Compare pricing.
8. Analyze positioning.
9. Identify competitive gaps.
10. Generate strategic opportunities.

## Decision Rules

- Prefer primary sources.
- Cross-check conflicting information.
- Never fabricate missing data.
- Mark uncertain conclusions explicitly.
- Separate facts from inference.

## Resources

For evidence evaluation:
read references/evidence-rules.md

For positioning:
read references/positioning-framework.md

For pricing:
read references/pricing-analysis.md

## Tools

Use:
- web search
- browser
- python

## Validation

Before completion:

- [ ] competitor list complete
- [ ] sources included
- [ ] pricing normalized
- [ ] facts separated from inference
- [ ] uncertainty identified
- [ ] strategic conclusions supported by evidence
```

这个结构已经不是传统 Prompt，它具备：

Identity

Intent

Contract

Procedure

Decision

Resources

Tools

Validation

### §31· 工程落地再往上：Skill Manifest

如果做真正的 Agent Runtime，建议把机器读取的信息从 SKILL.md 中进一步分离：

```
id: skill.competitor-analysis

name: Competitor Analysis

version: 1.4.0

runtime:
  type: agentic
  max_steps: 40

capabilities:
  - competitor-research
  - pricing-analysis
  - positioning-analysis

inputs:
  schema: schema/input.json

outputs:
  schema: schema/output.json

dependencies:
  - skill.market-research@^1.2

tools:
  - web.search
  - browser
  - python

permissions:
  network: true
  filesystem: read

evaluation:
  benchmark: competitor-analysis-v2

status: production
```

manifest

SKILL.md

负责机器。

负责 Agent。

原则

二者职责分离。

### §32· 工程落地Skill 的四种成熟度

评价一个 Skill，不要只看「Prompt 写得好不好」，可以分成五级：

L0

Prompt Skill

一段 Prompt

一次性指令，无法复用。

L1

Instruction Skill

SKILL.md + References

已经可以复用。

L2

Executable Skill

+ Tools / Scripts / Schema / Validation

可以真正执行任务。

L3

Production Skill

+ Registry / Router / Dependency / Version / Permission / Observability / Evaluation / Memory

企业级 Skill。

L4

Self-Evolving Skill

+ Feedback / Learning / Distillation / Automatic Evaluation / Version Generation

自进化 Agent Capability。

### §33· 工程落地最终形成你的「Skill OS」

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>AGENT</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL ROUTER</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL REGISTRY</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Skill A</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Skill B</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Skill C</div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL RUNTIME</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Tools</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Memory</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Data</div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>EXECUTE → VALIDATE → EVALUATE → LEARN</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL vNEXT</div></div>

定义

这已经不是单纯的 Skill Framework，而是

Skill Operating System

。

### §34· 工程落地和你之前的 Agent OS 设计结合起来

原有体系：Prompt Layer → Schema Layer → Workflow Layer → Runtime Layer → Agent Library → Tool Integration → Memory & Learning → Self-Evolving Organization → AI Autonomous Economy。如果重新架构，建议升级为：

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>AI ORGANIZATION</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>ORGANIZATION LAYER → AGENT LAYER</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>CAPABILITY OS</div><div>Skill Registry · Skill Router · Skill Runtime · Skill Evaluation</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL LAYER</div><div>Knowledge · Procedure · Decision</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>TOOLS → RUNTIME</div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Memory / Learning</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Evaluation / Governance</div>

这里出现一个非常重要的概念：**Capability OS**。Agent 不再是「Prompt + LLM」，而是——

Agent = 一个能够自主组合 Capability 的智能执行主体。

### §35· 工程落地最终建议采用的 Skill 元模型

以后设计任何 Skill，都可以套这个模型：

01

Identity

name / version / description

02

Intent

when / when-not

03

Contract

input / output / schema

04

Knowledge

concepts / references

05

Procedure

workflow / SOP

06

Decision

rules / heuristics

07

Execution

tools / scripts / APIs

08

Resources

templates / datasets

09

State

runtime state / checkpoint

10

Validation

constraints / quality

11

Evaluation

benchmark / score

12

Security

permission / policy

13

Observability

trace / log / metrics

14

Memory

experience / feedback

15

Learning

improvement / distillation

PART 08

结语

§36–37

### §36· 结语最关键的一句话

如果把 Agent 比作一个公司员工：

| 组件 | 类比 |
|---|---|
| Prompt | 老板临时交代的话 |
| Knowledge | 员工掌握的知识 |
| Skill | **员工真正会做的工作** |
| Workflow | 公司的办事流程 |
| Tool | 员工手里的工具 |
| Memory | 员工过去积累的经验 |
| Evaluation | 绩效考核 |
| Learning | 培训 |
| Skill Registry | 公司的人才技能库 |
| Skill Router | HR / 调度系统——判断「这件事应该调用谁的能力」 |
| Skill Runtime | 实际的工作环境 |

### §37· 结语下一步：Production Agent Skill Specification v1.0

真正值得下一步做的，不是继续研究「SKILL.md 怎么写」，而是直接建立一套**《Production Agent Skill Specification v1.0》**，把它工程化成 10 个核心 Schema / 文件：

```
01 skill-spec.md           ← Skill 总规范
02 SKILL.md                ← Agent 指令规范
03 manifest.schema.json    ← Skill 元数据 Schema
04 input.schema.json       ← 输入 Schema
05 output.schema.json      ← 输出 Schema
06 dependency.schema.json  ← Skill 依赖
07 policy.schema.json      ← 权限 / 安全
08 evaluation.schema.json  ← Skill 评估
09 registry.schema.json    ← Skill 注册中心
10 runtime.spec.md         ← Skill Runtime
```

然后进一步实现完整链路：

Registry

→

Router

→

Loader

→

Dependency Resolver

→

Runtime

→

Validator

→

Evaluator

→

Memory

→

Learning

这样我们就不是在「写几个 Agent Prompt」，而是在真正设计一个**可扩展的 Agent Capability Platform（智能体能力平台）**。这套架构非常适合 OPC / AI 公司方向：最终可以做到——

一个人 + 一个 Agent OS + 数百个专业 Skills，把采购、市场、SEO/GEO、产品、包装、研究、运营等工作能力全部模块化。

← 前篇

SKILL 介绍 · 概念手册

↑ 回到开头

SKILL SPEC

说明

内容依据用户提供的《生产级 Agent Skill 架构规范》原文 35 节整理，结构与编号 1:1 对应；文中指标与评分为原文示例。本页为单文件 HTML，双击即可打开。
