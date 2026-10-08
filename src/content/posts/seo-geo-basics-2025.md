---
title: "SEO 与 GEO 基础及语料投喂 Skill"
description: "博客 SEO 三步、GEO 四步原理、GEO vs SEO 对比表与 geo-corpus-feeder 四周循环 Skill 设计。"
pubDatetime: 2026-04-12
category: "建站与技术"
kind: "长文"
tags: ["SEO", "GEO", "语料投喂", "博客优化"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00243-2025-10-14 个人博客 SEO 优化指南00298-2025-10-24 生成式引擎优化（GEO）全面解读00906-2026-04-12 GEO 语料投喂 Skill 设计

## 01 · 个人博客 SEO 三步：地基、页面、推广（00243）

核心思想：SEO 不是一次性工作，而是与写博客相伴的习惯。三步依次为技术地基、页面内容优化、站外推广。

| 阶段 | 关键动作 |
|---|---|
| **① 技术地基** | 确认`robots.txt`不误拦；生成 XML 站点地图并在 Google Search Console、Bing Webmaster Tools 提交；装 GSC + GA 看排名与读者行为。关键词先研究再写：新博客主攻**长尾词**（"新手在家如何徒手健身"而非"健身"）。内容专题化 + 写几篇支柱级"终极指南"。 |
| **② 页面优化** | 标题前半放关键词、50–60 字符内；一篇一个 H1，用 H2/H3 结构化；关键词自然分布不堆砌；正文 1500 字以上才有价值地写；URL 简洁含词；图片改描述性文件名 + ALT 文本；新文章链到 2–3 篇相关旧文做内链。 |
| **③ 站外推广** | 外链是权威度最重要信号：先靠卓越内容被自然引用，再礼貌 outreach（禁群发），在知乎/Reddit/专业论坛真诚参与；提速度（PageSpeed Insights）、做响应式、上 HTTPS；社交信号间接带来初始曝光。 |

> **一句话**：内容为王，外链为皇，用户体验为后。建站时配 GSC/GA 与站点地图；写作前花 10 分钟定关键词；写作中优化标题/结构/图片/内链；发布后分享并持续观察 GSC、定期更新旧文。

## 02 · GEO 是什么：AI 怎么"想"和"引用"（00298）

生成式引擎优化（GEO）是为 ChatGPT、Copilot、Gemini、Claude 这类生成式 AI 引擎出现的内容优化策略，目标是让你的内容成为 AI 对话式答案里的"唯一"或"主要"来源。用户不再点十个蓝链，而是直接拿到一段整合答案——几乎 100% 零点击。

| 步 | AI 工作流 | GEO 在哪步赢 |
|---|---|---|
| **1** | 理解用户意图（解析提示词深层需求） | — |
| **2** | 检索相关信息（训练数据或联网搜索找相关片段） | 胜出点：结构化、权威、语义相关的内容更易被检索到 |
| **3** | 综合与生成（理解、整合、重述成连贯答案） | — |
| **4** | 引用来源（Copilot、Perplexity 等标出资料链接） | 胜出点：成为被标注的那一条来源 |

GEO 的目标就是在第 2 步（检索）和第 4 步（引用）中胜出，向 AI 证明你就是该领域最值得信赖的专家。

## 03 · GEO 与 SEO 的五维区别（00298）

| 维度 | 传统 SEO | GEO |
|---|---|---|
| **目标** | 在 SERP 排名靠前，吸引点击 | 成为 AI 答案的**直接信息来源**，可能无需点击 |
| **结果形式** | 10 个蓝链、精选摘要、知识图谱 | 一段整合的自然语言文本 + 引用链接 |
| **优化对象** | 搜索引擎排名算法 | 生成式 AI 的理解、整合与引用偏好 |
| **内容重点** | 关键词密度、外链数量、页面权重 | 权威性、全面性、可信度、结构化 |
| **交互模式** | 人机交互（用户自筛结果） | 人机对话（用户与 AI 直接交互） |

## 04 · GEO 五条实施策略（00298）

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>1</span><h3>成为权威信源</h3></div><div style="padding:14px 16px;font-size:13.5px;color:inherit">展示专家背景、认证、获奖；拿政府/知名媒体/高校的高质量外链；被维基百科、行业白皮书、权威期刊引用——这些都是 AI 的&quot;信任票&quot;。</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>2</span><h3>极致内容深度</h3></div><div style="padding:14px 16px;font-size:13.5px;color:inherit">写&quot;一篇解决所有问题&quot;的终极指南；用 H1/H2/H3、列表、表格、摘要把结构摆清楚；对复杂问题给多角度分析、步骤、利弊对比。</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>3</span><h3>语义与实体</h3></div><div style="padding:14px 16px;font-size:13.5px;color:inherit">写&quot;咖啡&quot;时自然带上&quot;咖啡因/烘焙/手冲/意式&quot;；像跟专家对话一样写，不堆关键词；让内容融入更大的知识网络。</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>4</span><h3>技术与可访问</h3></div><div style="padding:14px 16px;font-size:13.5px;color:inherit">清晰 URL 与内链；用<code>Article / HowTo / FAQPage / Person / Organization</code>等 Schema 结构化数据给 AI 一份&quot;内容说明书&quot;；提速；<code>robots.txt</code>别误封爬虫。</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>5</span><h3>针对提示词优化</h3></div><div style="padding:14px 16px;font-size:13.5px;color:inherit">设 FAQ 用&quot;是什么/为什么/怎么做&quot;句式直接回答；答完主问题后预判后续问题（冲煮咖啡后接着讲选豆与器具清洁）。</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>×</span><h3>挑战与流量悖论</h3></div><div style="padding:14px 16px;font-size:13.5px;color:inherit">AI 引用机制不透明、模型偏好一直在变；被成功引用也可能不带直接点击，需另找品牌曝光与变现。GEO 是持续迭代，不是一次性。</div></div></div>

## 05 · GEO 语料投喂 Skill：按月循环的流水线（00906）

把上面的策略落成一个 OpenClaw Skill：`geo-corpus-feeder`，纯 Markdown、按月跑一轮"收集→结构化→优化→投喂→监测"闭环，目标平台 DeepSeek / Kimi / 豆包。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>目录结构</span><h3>Skill 文件怎么摆</h3></div><div style="padding:14px 16px"><div>geo-corpus-feeder/ ├── SKILL.md # 触发词 + 四周围流程 + 交互命令 ├── corpus/ # 语料库（自行填充） │ ├── brand/ # 品牌故事、定位、价值主张 │ ├── product/ # 产品特性、规格、使用场景 │ ├── faq/ # 常见问答 │ ├── case/ # 客户案例、评价 │ └── knowledge/ # 行业白皮书、研究报告 ├── schedule/ # 调度记录（自动维护） │ ├── current_month.json │ ├── cycle_log.json │ └── history/YYYY-MM/ └── templates/ └── corpus_template.md</div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>四周循环</span><h3>每月四周围跑什么</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:90px">周次</th><th>阶段</th><th>做什么</th></tr></thead><tbody><tr><td><b>第1周</b></td><td>收集与清洗</td><td>扫<code>corpus/</code>找新增/修改；查标题正文元数据是否齐全；标重复、过时、逻辑矛盾的低质语料。</td></tr><tr><td><b>第2周</b></td><td>结构化与 Schema</td><td>每条加 YAML 元数据头；按类型建议 FAQPage / Product / Article / HowTo Schema；做逻辑一致性校验，列&quot;逻辑冲突报告&quot;。</td></tr><tr><td><b>第3周</b></td><td>AI 友好化优化</td><td>长文拆成可独立引用的模块；去掉模糊指代补主体；每条生成 3–5 个问答对；按 1–10 打 GEO 友好度分，低于 6 分人工复审。</td></tr><tr><td><b>第4周</b></td><td>投喂与监测</td><td>按优先级列投喂清单（在各平台手动/API 发布，Skill 只记录）；建<code>corpus_published / ai_citation_rate / exposure_rate / first_recommendation_rate</code>基线；归档历史、生成下月配置。</td></tr></tbody></table></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>元数据头</span><h3>每条语料的标准 YAML 头</h3></div><div style="padding:14px 16px"><div>--- id: brand_001 type: brand | product | faq | case | knowledge priority: high | medium | low keywords: [关键词1, 关键词2, 关键词3] target_platforms: [deepseek, kimi, doubao, chatgpt] created: YYYY-MM-DD updated: YYYY-MM-DD version: 1.0 ---</div><p style="margin:8px 0 0">正文用&quot;核心信息摘要（1–2 句可直接引用）→ 背景/场景 → 关键信息 → 数据/证据 → 3 个问答对 → 10–15 个语义关键词&quot;的模板写。触发词：<code>GEO优化 / 语料投喂 / 开始本月GEO循环 / 查看GEO进度 / GEO月度报告 / 检查语料质量 / 重置本月循环</code>。</p></div></div>

## 06 · 四条被反复引用的 GEO 数字（00906 · 照录）

这些数字在原笔记里被当作 GEO 效果依据反复引用，照录于此——用于说服自己"结构化、持续循环"值得做，不必当作严格可复现的实验结论。

+320%

具备高度逻辑关联的结构化语料，被 AI 引用概率比碎片化文本高。

+40%

结构化数据（Schema）标记可使 AI 检索效率提升。

3%→-80%

品牌信息存在 3% 以上逻辑冲突时，AI 会把其权重调降 80% 以上。

180 天

深度 GEO 优化的语义资产半衰期；热点式灌输内容 3 天内就被新模型权重覆盖。

> **合规底线**：不投虚假内容、不用非法爬取的信源；每月复盘 AI 引用率、跟住主流平台算法更新。原笔记另提到"系统化 GEO 部署后品牌被提及率平均提升 280% 以上"，同样作参考而非承诺。
