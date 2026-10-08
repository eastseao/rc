---
title: "Agent 概念·演进·RAG 与生态"
description: "Agent 与语言模型区别、Prompt 到 Skill 四阶段演进、RAG 原理、国内程序全景与 2026 产业数据。"
pubDatetime: 2026-07-08
category: "AI与Agent"
kind: "长文"
tags: ["Agent 概念", "Prompt 到 Skill", "RAG", "OpenClaw", "智能体生态"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00701-2026-03-11 AI 领域 Agent 概念解析（含国内外成熟 Agent 对比、OpenClaw 详解）00985-2026-04-21 AI 从 Prompt 到 Skill 演进及未来趋势01206-2026-05-25 国内 AI Agent 程序列表（含 QClaw / Trae / EasyClaw / Marvis、Molili、DeepSeek Agent 入口）01249-2026-05-31 RAG 技术概念解析01382-2026-07-08 Agent 全景解读（市场规模、大厂动态、应用案例）

## 01 · Agent 是什么：概念与和语言模型的区别（00701）

在人工智能领域，**Agent（智能体）**指能够**感知环境、自主决策并采取行动**以实现特定目标的实体——它不只是能说话的聊天机器人，更是一个能动手干活的数字员工，像一位配备了大脑（大语言模型）又长了双手（调用工具）的数字秘书。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">大脑（大语言模型）</h3><p style="font-size:13.5px;color:inherit">负责理解指令、进行推理、拆解复杂任务并做决策。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">感知（感知模块）</h3><p style="font-size:13.5px;color:inherit">接收多模态信息，包括文本、图像、语音以及环境反馈。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">行动（行动模块）</h3><p style="font-size:13.5px;color:inherit">执行具体动作：调用工具（搜索引擎、API、计算器）或执行命令（控制软件、发送邮件）。</p></div></div>

与传统程序相比，Agent 最显著的区别在于**自主性**和**主动性**：它无需每一步都被人为规定，而是根据目标自行规划路径并执行，遇到错误时还能自我反思并修正。与国内语言模型（DeepSeek、文心一言、通义千问等）的关系是——**语言模型是 Agent 的大脑，Agent 是语言模型的"身体"和"手脚"**。

| 对比维度 | 语言模型（如 DeepSeek） | Agent |
|---|---|---|
| **核心定位** | 大脑：基于海量数据训练的神经网络，主攻文本生成、理解与推理。 | 自主实体或系统：以语言模型为大脑，目标是感知环境、自主决策并采取行动。 |
| **能力范围** | 单次对话与内容生成，局限于对话框内的文本交互。 | 执行多步骤任务，按需调用外部工具（搜索、API）完成任务，如预订机票酒店。 |
| **交互模式** | 被动：用户提问，它回答。 | 主动：按目标自主规划，甚至主动向用户提问以澄清需求。 |
| **记忆能力** | 大多只在单次对话内记忆，新对话如"失忆"。 | 构建更复杂的记忆模块，长期记住用户偏好，并在执行中反思与自我修正。 |

<details open><summary>OpenClaw 详解：引爆&quot;养龙虾&quot;热潮的开源智能体<span>四层架构</span></summary><div><p>OpenClaw 是一款<b>开源、本地优先</b>的 AI 智能体平台，由奥地利开发者 Peter Steinberger（PSPDFKit 创始人）于 2025 年底创建、2026 年初定名 OpenClaw；图标形似龙虾，故把使用和训练它的过程称为<b>&quot;养龙虾&quot;</b>。其革命性在于让 AI 从&quot;只会说&quot;进化为&quot;能够干&quot;。GitHub 星标已突破<b>24.8 万</b>，一度让 Mac Mini 卖到脱销。</p><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">架构层</th><th>对应能力</th><th>说明</th></tr></thead><tbody><tr><td><b>前台 · 多渠道接入层</b></td><td>耳朵</td><td>通过渠道适配器无缝接入 WhatsApp、Telegram、钉钉、飞书、企业微信等，在聊天界面直接 @它下达指令。</td></tr><tr><td><b>大脑 · 多模型决策层</b></td><td>思考中枢</td><td>不绑定单一模型，可切换 Claude、GPT 系列、DeepSeek、智谱 GLM、阿里云百炼（Qwen）等；负责理解意图、拆解任务。</td></tr><tr><td><b>双手 · 技能与执行层</b></td><td>手和脚</td><td>通过模型上下文协议（MCP）与技能插件，获得控制浏览器、调用邮件系统、执行终端命令、操作软件 API 等真实能力。</td></tr><tr><td><b>档案柜 · 本地记忆层</b></td><td>长期记忆</td><td>本地优先双模记忆：短期保证多轮连贯，长期用 SQLite 等把偏好习惯存本地；支持可插拔上下文引擎，让记忆几乎不丢失。</td></tr></tbody></table></div><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>个人效率</dt><dd>7×24 私人秘书：整理文件、批量重命名、提取 PDF 关键信息、自动回复邮件、抓取网页数据填表。</dd><dt>企业自动化</dt><dd>智能客服、自动生成会议纪要与待办、分析产线数据优化工艺、秒级识别异常交易。</dd><dt>开发与科研</dt><dd>辅助代码审查、日志分析、自动跑测试；科研侧调用超算完成分子动力学模拟，效率提升 5-8 倍。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>Token 消耗</dt><dd>执行任务需大量调用模型，Token 消耗是普通对话的<b>30 倍以上</b>，由此催生云厂商算力服务与付费安装、订阅。</dd><dt>生态落地</dt><dd>腾讯云推云上部署方案与 WorkBuddy；阿里云一键部署镜像；国家超算互联网平台接入；硬件厂商推出&quot;OpenClaw 盒子&quot;。</dd></dl><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>安全风险与使用建议</h5><ul><li>工信部 NVDB 平台曾预警：默认配置下存在&quot;信任边界模糊&quot;风险，被恶意利用或误下危险指令可能导致设备被接管、邮件误删、隐私泄露。</li><li>隔离运行：用旧电脑 / 虚拟机 / Docker 部署，不在重要主机上&quot;裸奔&quot;；最小权限；重要操作人工复核（如深圳福田&quot;政务龙虾&quot;配公务员做&quot;监护人&quot;）。</li></ul></div></div></div></div></details>

## 02 · 从 Prompt 到 Skill 的演进四阶段（00985）

AI 的使用方式正发生一场范式转移——核心是**从"指令"思维，向"能力"与"系统"思维跨越**。从 Prompt 到 Skill 只是第一幕，背后是 AI 角色从"对话工具"向"行动主体"的质变。完整路径是：写出单个指令 → 安装可复用技能 → 组建能协同工作的智能体军团 → 构建能自主决策、与物理世界交互的智能生态系统。

| 阶段 | 核心变化 | 关键标志 |
|---|---|---|
| **一 · 装技能包** | 从"写提示词"到"装技能包"：Skill 是把知识、流程、工具封装在一起的可复用模块化能力包（如内置日志格式、错误模式与排查流程的"日志分析 Skill"）。 | 进入"技能工程"阶段；核心价值是专家知识封装与复用、避免上下文过载、降低使用门槛。Anthropic（Claude）、Cursor 已在推动。 |
| **二 · 军团协同** | 从"单兵作战"到"军团协同"：2026 年被普遍视为"智能体爆发年"，单 Agent 成熟后必然走向多智能体系统（MAS），多个分工明确的 Agent 像团队一样协同。 | 软件开发需求自动调配需求拆解、代码生成、测试、协调 Agent；标准化通信协议**MCP（模型上下文协议）**与**A2A（Agent-to-Agent）**成为"通用语言"。 |
| **三 · 智能网络** | 构建自主的智能网络（Agentic Mesh）：AI 从被动任务执行者，转变为主动的、自组织的智能服务网络，自主设计工作流、发现并协同其他 Agent。 | AI 成为深度嵌入企业 IT 架构的"操作系统"；预计到 2026 年底，超过**40%**的企业应用将嵌入专用 AI Agent。 |
| **四 · 人机协作** | 人机关系重塑：人从"写提示词的执行者"升级为**"Agent 指挥官"**，核心能力变为定义目标、架构系统、编排 Agent 军团。 | 认知范式从"预测下一个词"转向"预测世界下一状态"；从单一模型走向推理+端侧混合模型；从数字世界走向具身智能。 |

## 03 · RAG：检索增强生成原理（01249）

RAG 是**Retrieval-Augmented Generation（检索增强生成）**的缩写，结合**信息检索**与**文本生成**两方面能力，让大模型借助外部知识给出更准确、更及时、更可靠的回答。可以想象成一个**允许在考试时查阅指定参考书的学生**。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13px;color:#0f766e;margin-bottom:8px">1 检索 Retrieval</h3><p style="font-size:13.5px;color:inherit">收到问题后，先去知识库（内部文档、最新网页、法律法规）搜索，找与问题最相关的几个信息片段。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13px;color:#0f766e;margin-bottom:8px">2 增强 Augmentation</h3><p style="font-size:13.5px;color:inherit">把检索到的片段与原始问题整合，形成包含上下文的&quot;增强提示&quot;。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13px;color:#0f766e;margin-bottom:8px">3 生成 Generation</h3><p style="font-size:13.5px;color:inherit">把增强后的提示发给大模型，让它基于外部信息而非仅凭&quot;记忆&quot;生成最终答案。</p></div></div>

| 纯大模型的问题 | 为什么是硬伤 | RAG 的解决方案 |
|---|---|---|
| **知识陈旧** | 训练数据截止到某个时间点，之后的信息不知道。 | 检索最新文档或新闻，让模型基于最新信息回答。 |
| **产生幻觉** | 对不了解的问题可能编造看似合理实则错误的内容。 | 答案基于检索到的真实内容，大大降低胡编乱造的可能。 |
| **缺乏私密性** | 无法学习公司或个人的内部数据（出于安全隐私）。 | 检索私有知识库、产品手册，模型本身不存储这些数据。 |
| **成本高昂** | 频繁训练或微调模型更新知识，耗费算力和资金。 | 只需更新外部知识库（加一个新文档），无需重新训练模型。 |

典型应用：智能客服与问答机器人（基于最新产品手册、政策回答）、企业知识库搜索（带出处的精准答案）、AI 辅助编程（查阅最新 API 文档与代码库）、辅助内容创作（先检索事实数据再润色扩写）。一句话——**RAG = 检索系统（找资料）+ 大语言模型（组织语言）**。

## 04 · 国内 AI Agent 程序全景列表（01206）

国内主要科技公司都推出了自己的智能体平台，大致分为三类：**核心智能体 / 大模型平台、编程与特定领域平台、面向开发者的开发框架**。代表性的四款桌面/系统级 Agent 为：**QClaw**（腾讯"养龙虾"AI 助手，最多 3 个并行）、**Trae**（火山引擎 AI 编程开发平台）、**EasyClaw**（猎豹移动 Windows 端任务自动化助手）、**Marvis 马维斯**（腾讯操作系统级 AI 助手，1 主 + 5 专项 Agent）。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>核心智能体 / 大模型平台</span><h3>互联网巨头产品矩阵（一）</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:200px">平台</th><th style="width:120px">出品方</th><th>简介</th></tr></thead><tbody><tr><td><b>文心智能体平台 AgentBuilder</b></td><td>百度</td><td>全流程智能体服务，在知识问答、文档处理场景表现突出。</td></tr><tr><td><b>通义千问</b></td><td>阿里巴巴</td><td>全能型智能体平台，国内调用量第一的大模型，可问答、文本生成。</td></tr><tr><td><b>腾讯元器</b></td><td>腾讯</td><td>零代码 / 少代码快速创建智能体，可发布至公众号、QQ 等生态。</td></tr><tr><td><b>讯飞星火智能体</b></td><td>科大讯飞</td><td>多模态智能体平台，集成文字、语音、图片、视频能力。</td></tr><tr><td><b>智谱清言智能体</b></td><td>智谱 AI</td><td>覆盖学习办公、生活娱乐的 C 端产品，教育领域推出&quot;i福娃&quot;等方案。</td></tr><tr><td><b>通义百炼</b></td><td>阿里云</td><td>大模型服务平台，支持 5-10 分钟低代码快速构建智能体。</td></tr><tr><td><b>智能体开发平台 ADP 3.0</b></td><td>腾讯云</td><td>一站式智能体平台，支持多 Agent 协同、工作流编排，可发布到腾讯生态。</td></tr><tr><td><b>扣子空间</b></td><td>字节跳动</td><td>通用智能体平台，插件生态极强，适合快速构建消费级应用。</td></tr></tbody></table></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>编程与特定领域平台</span><h3>互联网巨头产品矩阵（二）</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:200px">平台</th><th style="width:120px">出品方</th><th>简介</th></tr></thead><tbody><tr><td><b>Trae</b></td><td>火山引擎</td><td>专业 AI 编程开发平台，提供响应快速的编程助手，可创建自定义智能体。</td></tr><tr><td><b>千帆 AppBuilder</b></td><td>百度</td><td>大模型应用开发平台，提供插件、编排等工具快速构建应用。</td></tr><tr><td><b>钉钉 AI</b></td><td>钉钉</td><td>集成在办公协作平台中的 AI 助手。</td></tr><tr><td><b>金蝶苍穹 Agent 平台 2.0</b></td><td>金蝶</td><td>企业级平台，支持 MCP 及 A2A 协议，覆盖财务、人力等核心业务。</td></tr><tr><td><b>用友 BIP 友空间</b></td><td>用友</td><td>集成 100+ 智能体（财务、供应链等），效率提升 300%。</td></tr><tr><td><b>得助智能</b></td><td>中关村科金</td><td>国内集成多模态的 C 端产品，自然语言快速创建智能体。</td></tr></tbody></table></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>开发框架</span><h3>面向开发者的 AI Agent 开发框架</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:200px">框架</th><th style="width:140px">出品方</th><th>简介</th></tr></thead><tbody><tr><td><b>Eino</b></td><td>字节跳动</td><td>主流的 Agent 开发框架之一。</td></tr><tr><td><b>AgentScope</b></td><td>阿里巴巴</td><td>主流的 Agent 开发框架之一。</td></tr><tr><td><b>Youtu-Agent</b></td><td>腾讯</td><td>主流的 Agent 开发框架之一。</td></tr><tr><td><b>MetaGPT</b></td><td>多智能体协作框架</td><td>专注多智能体协作，模仿软件工程标准作业程序。</td></tr></tbody></table></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>更多值得关注</span><h3>垂直与开源生态中的 AI Agent</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:180px">程序</th><th>定位与特色</th></tr></thead><tbody><tr><td><b>DeepSeek Agent</b></td><td>深度求索出品，代码生成与长程任务规划见长，可自主编写 Python 脚本调用外部工具，擅科研数据分析。官方入口：deepseek.com / chat.deepseek.com / platform.deepseek.com。</td></tr><tr><td><b>实在 Agent</b></td><td>实在智能基于自研 TARS 大模型，通过屏幕语义理解&quot;一句话完成工作&quot;，把对话直接转为软件操作。</td></tr><tr><td><b>WebSailor</b></td><td>阿里巴巴，专注检索的通用智能体，可在互联网上完成复杂信息搜集与分析。</td></tr><tr><td><b>阿里云百炼 Model Studio</b></td><td>通用企业服务平台，无缝对接钉钉、阿里云 ERP 等生态工具。</td></tr><tr><td><b>蚂蚁 Agentar</b></td><td>蚂蚁数科全链路开发平台，大模型与行业知识库深度融合，适合金融、零售复杂决策。</td></tr><tr><td><b>DeepAgent</b></td><td>深演智能，专攻营销与销售决策，广告投放、CRM 管理，支持 20+ 智能体协同。</td></tr><tr><td><b>Thingo</b></td><td>多智能体协同平台，支持任务自动拆解，适合中小企业低成本快速部署。</td></tr><tr><td><b>n8n</b></td><td>隐私保护优先的开源自动化平台，支持多步骤工作流编排。</td></tr><tr><td><b>Dify</b></td><td>开源低代码平台，支持 75+ 模型接入，适合中小企业快速构建知识库问答。</td></tr><tr><td><b>Molili</b></td><td>当贝（Dangbei）推出的国内首款中文版 OpenClaw；&quot;三省六部&quot;架构（中书省规划 / 门下省审核 / 尚书省执行），配套 CocoLoop 技能商店 8000+ 现成技能，实测成本比原版降低 50% 以上。</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>快速分类</b>：个人生产力——Marvis、QClaw、EasyClaw、DeepSeek Agent、豆包、元宝、灵光；企业服务与开发——阿里云百炼、腾讯云 ADP、文心智能体、钉钉 AI、扣子空间、Dify、n8n、金蝶苍穹、用友 BIP；垂直行业——WebSailor（检索）、DeepAgent（营销）、智谱 AI（教育）；开发者工具与框架——Trae、Eino、AgentScope、Youtu-Agent、LangGraph、MetaGPT。</div></div></div>

## 05 · 2026 产业全景：市场规模与落地（01382）

截至 2026 年 7 月，AI Agent 正处在从"技术概念"走向"规模落地"的关键转折点。行业重点已从堆叠参数，转向以智能体为核心、追求真实产业增效的"后 Scaling 时代"。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0;text-align:center"><div style="font-size:30px;font-weight:800;color:#0d9488">212 亿 → 449 亿</div><p style="font-size:13px;color:inherit;margin-top:6px">中国企业级 AI 智能体市场规模：2025 年 212 亿元，预计 2026 年猛增至 449 亿元。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0;text-align:center"><div style="font-size:30px;font-weight:800;color:#0d9488">72%</div><p style="font-size:13px;color:inherit;margin-top:6px">全球已有 72% 的企业将 AI Agent 投入生产。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0;text-align:center"><div style="font-size:30px;font-weight:800;color:#0d9488">40%</div><p style="font-size:13px;color:inherit;margin-top:6px">Gartner 预测：到 2026 年底全球 40% 的企业应用将嵌入 AI 智能体。</p></div></div>

| 维度 | 最新动态 |
|---|---|
| **国内大厂** | "下架智能体"实为下架"拟人陪聊 Bot"以符合监管，真正能干的 Agent 是战略重点。阿里云发布多智能体协作平台 AgentTeams 与优化平台 AgentLoop；腾讯发布能力显著提升的混元 Hy3 模型；字节跳动飞书推出"多维表格智能体"。 |
| **海外巨头** | Salesforce 的 Agentforce 平台年收入已近 8 亿美元，并宣布在瑞士投资 10 亿美元加码代理式 AI；微软有 Copilot 体系；ServiceNow 推出面向企业流程管理的 AI Agent 体系。 |
| **关键技术** | 记忆系统被认为是下一代智能体的核心壁垒；开源项目 OpenClaw 的流行标志 AI 原生工作平台加速落地；国家层面已发布首个智能体互联国家标准，解决"信息孤岛"。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">应用案例</h3><ul style="padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:8px">供应链物流：兆企供应链开源框架 WorkMate 将报价响应从 20 分钟缩短至<b>30 秒</b>；但某跨境电商因不同厂商 Agent 接口不统一，导致采购 Agent 误下单造成数百万损失，凸显标准化紧迫性。</li><li style="margin-bottom:8px">酒店服务：华住集团&quot;AI 住中服务&quot;智能体已在上万家门店上线，生成订单仅需<b>5 秒</b>。</li><li>协同办公：Anthropic 的 Claude Tag 让 AI 像同事一样进入工作群，可拆解任务、调用工具；飞书、钉钉、企业微信都在引入类似功能。</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">挑战与展望</h3><ul style="padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:8px">落地不易：许多项目仍停留在试点，真正进入核心业务的比例不高。</li><li style="margin-bottom:8px">安全合规：企业担心 AI 在财务、风控等敏感岗位&quot;做错事&quot;。</li><li>未来方向：多智能体协同、具身智能（与物理世界交互）、记忆原生智能（持续学习与进化）。</li></ul></div></div>
