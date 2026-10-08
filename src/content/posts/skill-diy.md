---
title: "如何制作适合自己的 Skill"
description: "七步法实操指南 13 节：选高频任务、挖隐性方法、自评闭环。"
pubDatetime: 2026-09-09
category: "AI与Agent"
kind: "手册"
tags: ["Skill", "实操", "七步法"]
---

GERVAS

制作指南

概念介绍 › Agent Skills ›**制作自己的 Skill**· 前篇[SKILL 介绍](../skill/)·[架构规范](../skill-spec/)

## SKILL DIY如何制作一个适合自己的 Skill

「适合自己的 Skill」不是从写 Prompt 开始，而是从**提炼你自己的工作方法**开始：把一个人稳定、可复用、可验证的做事方法，压缩成 AI 可以调用的一套能力。最重要的不是写得多，而是把你的经验变成**规则、流程和判断标准**。本篇按七步法展开，并给出进阶路线。

类型

实操指南

结构

13 节

阅读

约 15 分钟

系列

概念手册

·

架构规范

· 本篇

### §01· 开篇先理解：什么才叫「自己的 Skill」

普通 Prompt

「帮我做一个产品包装方案。」

普通 Skill

当用户需要产品包装方案时，按照产品定位 → 人群 → 卖点 → 信息层级 → 包装结构 → 文案 → 视觉方向 → 验证的流程完成。

适合自己的 Skill

在流程之上，进一步加入「

我通常是怎么判断的？

」

例如做包装工作时，你可能已经形成了很多隐性判断：

- 消费者第一眼应该看到什么？

- 哪些信息不能放正面？

- 什么卖点消费者真正听得懂？

- 高端产品为什么不能堆砌「高科技」？

- 食品包装上的专业术语应该如何转成消费者语言？

- 产品名称、核心卖点、产地、工艺之间如何排序？

- 什么情况下应该突出原料？

- 什么情况下应该突出功效场景？

- 什么情况下应该砍掉 50% 的文字？

核心资产

这些东西才是

你的 Skill 核心资产

。

### §02· 开篇制作自己的 Skill：七步法总览

整个过程可以压缩成一条链：

经验

→

任务

→

方法

→

规则

→

流程

→

案例

→

Skill

下面按 ① → ⑦ 逐步展开。

### §03· 七步法 · ①找一个「高频重复任务」

不要一上来做「我的营销 Skill」——太大。应该从一个具体任务开始，例如：

产品包装文案优化

食品包装卖点提炼

竞品包装分析

采购方案比价

Markdown 文档结构化

把复杂专业资料整理成消费者语言

#### 一个好 Skill 通常满足三个条件

| 条件 | 说明 |
|---|---|
| 高频 | 你经常做 |
| 重复 | 每次都有类似过程 |
| 有经验壁垒 | 你比普通人判断得更好 |

最值得 Skill 化的任务

你已经做过 50 次，但每次还要重新告诉 AI 怎么做。

### §04· 七步法 · ②把「你脑子里的方法」挖出来

这是制作个人 Skill 最关键的一步。不要问「这个 Skill 应该写什么？」，应该问——

如果让我手把手教一个新人，我会怎么教？

以「消费者语言包装文案 Skill」为例，把自己的思维拆开：

1. 输入产品资料

1. 判断产品是什么

1. 判断消费者是谁

1. 找消费者真正关心的问题

1. 提炼产品事实

1. 区分事实 / 卖点 / 利益

1. 把专业语言翻译成消费者语言

1. 建立包装信息层级

1. 生成正面核心文案

1. 生成辅助信息

1. 检查是否夸大

1. 输出方案

质变点

这已经开始从「Prompt」变成「Skill」。

### §05· 七步法 · ③把经验变成「判断规则」

这是 Skill 与普通 Prompt 最大的区别。普通 Prompt 写「请使用消费者语言」——太模糊。你的个人 Skill 可以变成一条条规则：

```
RULE-01
如果一个卖点需要专业知识才能理解，
优先转换成消费者可以直接理解的结果语言。

RULE-02
如果一个技术名词无法回答"对消费者有什么意义"，
则不得作为核心卖点。

RULE-03
包装正面优先表达：
产品是什么 + 核心价值 + 为什么值得购买。

RULE-04
一个包装正面原则上只保留一个第一核心卖点。

RULE-05
不得为了"显得高级"堆砌：
科技、臻选、匠心、赋能、矩阵等空泛词汇。
```

价值公式

Skill 的价值 ≠ 它知道什么，而是它知道「什么时候应该怎么判断」。

### §06· 七步法 · ④把 Skill 分成 5 个核心部分

如果是给自己长期使用，不要把所有东西都塞进`SKILL.md`，可以采用这个结构：

```
my-packaging-skill/
│
├── SKILL.md
│
├── rules/
│   ├── positioning.md
│   ├── consumer-language.md
│   ├── information-hierarchy.md
│   └── compliance.md
│
├── workflow/
│   └── workflow.md
│
├── examples/
│   ├── good.md
│   └── bad.md
│
├── templates/
│   └── packaging-output.md
│
└── evaluation/
    └── evaluation.md
```

核心逻辑：

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL.md</div><div>我是谁 / 做什么 · 什么情况下使用 · 怎么做 · 怎么判断 · 去哪里读取详细知识</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Rules</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Workflow</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Examples</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Templates</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">Evaluation</div>

设计方向

符合 Agent Skills 的重要设计原则：

渐进式加载

，而不是一开始把所有知识塞进上下文。

### §07· 七步法 · ⑤给 Skill 一个明确的「输入 → 输出契约」

这是很多人制作 Skill 时容易忽略的。例如输入：

```
product:
  name: 有机五黑饮
  category: 植物饮品

ingredients:
  - 黑枸杞
  - 黑桑葚
  - 黑加仑
  - 黑莓
  - 黑豆

target_user:
  - 关注健康的人群

positioning:
  - 高花青素
  - 有机
```

Skill 不应该只是「自由发挥」，而应该规定处理流程：

输入

→

产品事实整理

→

消费者需求分析

→

核心价值提炼

→

卖点优先级排序

→

包装信息架构

→

正面文案

→

背面文案

→

风险检查

→

最终方案

最终输出也应该固定：

```
output:
  positioning:
  core_benefit:
  key_selling_points:
  front_panel:
  back_panel:
  visual_direction:
  compliance_risk:
  recommendations:
```

收益

这样以后你的 Agent 才能

稳定调用

它。

### §08· 七步法 · ⑥用你过去做过的「真实案例」训练 Skill

你过去已经做过大量类似工作——产品命名、包装文案、五黑饮、黑枸杞、冬虫夏草、茶油、松茸、食品/健康产品、消费者语言转换——这些实际上就是非常好的**Skill Dataset**。

不要只保存最终答案，最好保存完整链条：

1. 原始需求

1. 原始资料

1. 第一次方案

1. 哪里不好

1. 为什么不好

1. 如何修改

1. 最终方案

1. 为什么最终方案更好

例如一个真实案例的演进：

高活性花青素矩阵

→

5 种天然高花青素黑色果实

→

5 种天然黑色果实，富含花青素

→

根据包装位置决定用哪种表达

案例解读

第一版专业感强，但消费者不知道是什么意思；逐版修改后，最终按包装位置决定表达方式。

关键差别

这时候 AI 学到的不只是「某句话怎么写」，而是

「什么情况下应该这么写」

——这才是个人 Skill。

### §09· 七步法 · ⑦最后一定要加入「自我评价标准」

这是从普通 Skill 走向**生产级 Skill**的关键。例如包装文案 Skill 可以规定，每次输出后必须检查：

1. 消费者是否一眼理解？

1. 是否明确产品是什么？

1. 是否只有一个第一核心卖点？

1. 是否存在专业术语堆砌？

1. 是否存在空泛营销词？

1. 是否存在重复表达？

1. 是否存在夸大宣传？

1. 是否符合产品真实事实？

1. 是否适合包装实际面积？

1. 是否具有购买理由？

然后让 AI 自己评分（示例）：

```
消费者理解度：9/10
卖点聚焦度：  8/10
差异化：      7/10
可信度：      9/10
包装适配度：  8/10

综合：        8.2/10
```

执行

→

检查

→

修正

闭环

这时候 Skill 就开始具有「执行 → 检查 → 修正」的闭环。

### §10· 进阶你可以把自己的 Skill 看成一个「数字化分身」

一本书能不能蒸馏成 Skill？一个人的语言和思维方式能不能蒸馏成 Skill？一个好用的技能能不能蒸馏出来？答案可以统一成：

原始专家

→

经验资料

→

案例

→

决策过程

→

判断规则

→

方法论

→

Skill

→

Agent

知识库

Skill

「我知道什么。」

「

我会怎么做。

」

最值钱的部分

你的个人 Skill 最有价值的其实是：

「我为什么这么做，而不是那么做。」

### §11· 进阶建立自己的「个人 Skill 工厂」

如果准备长期做，不建议一个一个手工写 Skill，可以建立流水线：

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>我的经验</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>任务识别器</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>方法提取器</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">决策规则提取</div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0">工作流程提取</div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL 生成器</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>SKILL 评测器</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>PRODUCTION SKILL</div></div>

↓

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:12px 16px;margin:14px 0"><div>实际使用 / 反馈 → SKILL 进化</div></div>

终局

最终形成：

你的个人 Skill OS

。

### §12· 进阶最适合的制作路线：先做 3 个「母 Skill」

按照 Agent / OPC / Skill 体系，不要从几十个 Skill 开始。先做三个母 Skill，再向下拆：

① 分析 Skill

看资料 → 找事实 → 找问题 → 找规律 → 得出结论。如：资料分析、竞品分析、市场分析、产品分析、文档分析。

② 创作 Skill

信息 → 策略 → 表达 → 成品。如：包装文案、产品命名、营销文案、视觉提示词、方案撰写。

③ 决策 Skill

多个方案 → 判断 → 筛选 → 推荐。如：供应商选择、包装方案选择、产品定位、采购决策、方案评审。

```
Personal Skill OS
│
├── Analysis
│   ├── Document Analysis
│   ├── Competitor Analysis
│   ├── Product Analysis
│   └── Market Analysis
│
├── Creation
│   ├── Packaging Copy
│   ├── Product Naming
│   ├── Marketing Copy
│   └── Visual Prompt
│
└── Decision
    ├── Supplier Selection
    ├── Packaging Evaluation
    ├── Product Positioning
    └── Procurement Decision
```

格局

这样就不是在「做几个 Prompt」，而是在逐渐建立

一个属于你自己的 AI 能力系统

。

### §13· 结语最关键的一句话

个人 Skill = 你的经验 + 你的方法 + 你的判断规则

+ 你的案例 + 你的输出标准 + AI 可执行流程

一个成熟 Skill 最终应该形成完整闭环：

触发

→

理解任务

→

加载必要知识

→

调用方法

→

执行

→

做判断

→

输出

→

自检

→

修正

→

记录经验

→

Skill 升级

这就已经从 Prompt Engineering 开始进入 Personal Agent Engineering 了。

下一步建议

直接拿你

最擅长、最经常做的一项工作

，从实际经验中反向「蒸馏」出来，一步步做成可以放进 OpenClaw / Claude / Codex / 自己 Agent 系统的生产级 Skill。

← 前篇

生产级 Agent Skill 架构规范

↑ 回到开头

SKILL DIY

说明

内容依据用户提供的《如何制作一个适合自己的skill？》原文整理，章节顺序与原文对应（一~十一 + 最关键的一句话）。本页为单文件 HTML，双击即可打开。
