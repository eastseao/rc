---
title: "立项报告 SKILL 编写"
description: "为 AI Agent 编写「立项报告 SKILL」完整指南：元数据结构、触发条件、输入参数、输出模板与调试方法。"
pubDatetime: 2026-07-14
category: "AI与Agent"
kind: "手册"
tags: ["SKILL", "立项报告", "AI Agent", "提示工程"]
---

## 01 · 什么是 SKILL

SKILL 是 AI Agent 的**可复用能力模块**——它把一类反复出现的任务（比如写立项报告）封装成标准化的提示词+流程+输出模板，让 Agent 在用户提到相关需求时自动调用，而不是每次都从零开始写提示词。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:14.5px;font-weight:700;margin-bottom:8px">为什么需要 SKILL</h3><p style="font-size:13.5px;color:inherit">立项报告有固定的结构和写作规范，每次手动写提示词既重复又容易漏项。SKILL 把这些规范固化下来，输入项目名称就能产出结构完整的初稿。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:14.5px;font-weight:700;margin-bottom:8px">SKILL vs 普通提示词</h3><p style="font-size:13.5px;color:inherit">普通提示词是一次性的；SKILL 有元数据（名称、描述、触发条件），Agent 能自动判断&quot;什么时候该用这个 SKILL&quot;，并按标准流程执行。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:14.5px;font-weight:700;margin-bottom:8px">立项报告 SKILL 的目标</h3><p style="font-size:13.5px;color:inherit">输入项目名称和基本背景，输出一份包含项目概述、市场分析、技术方案、预算、风险、里程碑的完整立项报告初稿。</p></div></div>

## 02 · SKILL 元数据结构

每个 SKILL 以一个 Markdown 文件（SKILL.md）描述，开头用 YAML Front Matter 声明元数据。元数据是 Agent 自动发现和调用这个 SKILL 的依据。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>YAML Front Matter</span><h3>立项报告 SKILL 的元数据声明</h3></div><div style="padding:14px 16px"><pre><code>--- name: proposal-report description: 生成项目立项报告。当用户要求写立项报告、项目建议书、 可行性报告，或提到&quot;立项&quot;&quot;申报项目&quot;&quot;写方案&quot;时使用。 覆盖项目概述、市场分析、技术方案、预算估算、 风险评估和里程碑计划六大章节。 version: 1.0.0 author: gervas tags: [立项报告, 项目管理, 文档生成] ---</code></pre></div></div>

| 元数据字段 | 作用 | 编写要点 |
|---|---|---|
| **name** | SKILL 唯一标识符 | 小写英文+连字符，如 proposal-report |
| **description** | Agent 判断是否调用此 SKILL 的核心依据 | 必须写清楚"什么时候用"+"能做什么"，让 Agent 一眼判断 |
| **version** | 版本号 | 语义化版本，方便追踪迭代 |
| **tags** | 标签索引 | 帮助 Agent 按领域检索 |

## 03 · 触发条件与输入参数

SKILL 正文的第一部分是触发条件说明和输入参数定义。Agent 收到用户请求后，先检查是否满足触发条件，再收集必需的输入参数。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>触发规则</span><h3>什么时候激活这个 SKILL</h3></div><div style="padding:14px 16px"><pre><code>## 何时使用本 SKILL 当用户提出以下任一类型的请求时，激活本 SKILL： 1. 明确要求&quot;写立项报告/项目建议书/可行性报告&quot; 2. 提到&quot;我要申报 XX 项目&quot;&quot;帮我写个方案&quot; 3. 给出项目名称并要求&quot;整理成正式文档&quot; 不要在以下场景使用： - 用户只是询问立项报告怎么写（用对话回答即可） - 用户要求的是结题报告/验收报告（用对应 SKILL）</code></pre></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>输入参数</span><h3>收集哪些信息再动笔</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0;margin-bottom:0"><table><thead><tr><th style="width:130px">参数名</th><th style="width:80px">必填</th><th>说明</th></tr></thead><tbody><tr><td><b>项目名称</b></td><td>必填</td><td>立项报告的核心标题，不知道就先问</td></tr><tr><td><b>项目背景</b></td><td>选填</td><td>为什么要做这个项目，解决什么问题</td></tr><tr><td><b>预算范围</b></td><td>选填</td><td>总预算金额区间，用于估算章节</td></tr><tr><td><b>预计周期</b></td><td>选填</td><td>项目计划起止时间</td></tr><tr><td><b>目标受众</b></td><td>选填</td><td>报告给谁看（领导/评审专家/投资机构），影响行文风格</td></tr></tbody></table></div></div></div>

## 04 · 输出模板：六大章节

SKILL 的核心价值在于**标准化输出结构**。无论输入什么项目，输出都遵循同一个六段式骨架，确保立项报告不会漏项。

| 章 | 章节名称 | 核心内容 |
|---|---|---|
| **一** | 项目概述 | 项目名称、背景、目标、预期成果（一段话讲清楚做什么） |
| **二** | 市场分析 | 行业现状、目标市场规模、竞争格局、机会点 |
| **三** | 技术方案 | 技术路线、核心技术选型、关键创新点、可行性论证 |
| **四** | 实施计划 | 里程碑节点（按季度/月度）、人员分工、交付物清单 |
| **五** | 预算估算 | 人力成本、设备/采购、其他费用、总计与占比 |
| **六** | 风险评估 | 技术风险、市场风险、管理风险及应对措施 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>写作指令</span><h3>SKILL 给 Agent 的写作规则</h3></div><div style="padding:14px 16px"><pre><code>## 写作要求 1. 语气：正式、客观，避免营销话术 2. 数据：不确定的数字用&quot;预计&quot;&quot;约&quot;标注，不要编造精确数字 3. 篇幅：每个章节 300-500 字，总篇幅 2500-3500 字 4. 格式：Markdown 输出，一级标题对应章节，二级标题对应子节 5. 如果用户未提供某项信息，用 [待补充：xxx] 占位，不要跳过该章节 6. 结尾附&quot;附录：关键假设说明&quot;，列出报告中所有推断的前提</code></pre></div></div>

## 05 · 调试与迭代

SKILL 写完不是一次到位的，需要通过真实调用案例迭代优化。

| 迭代阶段 | 做法 |
|---|---|
| **冒烟测试** | 用一个已知项目跑一遍，检查输出是否包含全部六个章节，格式是否符合预期 |
| **边界测试** | 故意只给项目名称不给其他参数，看 Agent 是否会追问必填项、是否会用占位符填充 |
| **真实案例** | 拿 3-5 个真实立项场景测试，收集 Agent 输出与人工期望的差距 |
| **修订提示词** | 把常见遗漏点和错误写法写进 SKILL 的"写作要求"里，版本号 +0.1 |
| **回归测试** | 每次修改后跑一遍冒烟测试，确认没有改坏 |

> **编写 SKILL 的三条原则**
> - **描述比指令重要**：Agent 先看 description 判断要不要调用，描述写不准就会漏触发或误触发。
> - **模板比自由发挥重要**：固定章节结构 + 写作字数要求，比"写一份好的立项报告"这种模糊指令有效得多。
> - **占位符比跳过重要**：信息不全时用 [待补充] 占位并提示用户，而不是直接跳过该章节导致结构残缺。
