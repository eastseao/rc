---
title: "OpenClaw 功能详解与国内变体对比"
description: "OpenClaw 核心能力与执行网关解析，国内十款变体横评、开源平替与 HY3 preview 积分体系。"
pubDatetime: 2026-05-17
category: "AI与Agent"
kind: "长文"
tags: ["OpenClaw", "执行网关", "国内变体", "免费积分", "HY3 preview"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：01162-2026-05-17 HY3 preview属于腾讯混元01165-2026-05-17 OpenClaw功能详解01166-2026-05-17 国内OpenClaw变体对比

## 01 · OpenClaw 是什么与核心能力（01165）

OpenClaw 是一款**开源、本地优先的 AI 智能体执行网关**。它能把大型语言模型（如 GPT-4o、Claude）从只能「动口」聊天，变成能「动手」执行真实任务，成为一个 7×24 小时待命的「数字员工」。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">系统操控能力</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.7"><li><b>文件管理</b>：批量重命名、格式转换、内容提取（如把下载文件夹图片统一转 WebP）。</li><li><b>应用控制</b>：浏览器自动化（数据爬取、表单填写）、操作 Office 软件。</li><li><b>代码与开发</b>：自然语言生成代码、管理部署流程、数据清洗。</li><li><b>系统管理</b>：进程管理、服务控制等。</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">交互渠道与工作流</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.7"><li><b>多渠道沟通</b>：命令行 CLI、Web 界面，或接入 QQ、飞书、企业微信、Slack、Discord 等 IM，「聊天即操作」。</li><li><b>任务编排</b>：把复杂任务拆解成子任务并按序自动执行。</li><li><b>持续运行</b>：7×24 小时自主处理任务，适合全天候监控、定期处理。</li><li><b>数据处理</b>：从邮件、网页、文档提取关键信息并结构化输出，查询数据生成图表报告。</li></ul></div></div>

| 应用场景实例 | 具体用途 |
|---|---|
| **个人效率提升** | 自动处理邮件、管理文件、协调日程；生成代码、调试、协助部署；总结网页、建个人知识库。 |
| **内容创作与社交** | 自动追踪热点，生成文案并分发到多平台。 |
| **法律领域** | 7×24 监控「老赖」公开财产变动，自动汇总线索；协助撰写法律文书、案例检索、案卷整理。 |
| **电商场景** | 自动抓取竞品价格，结合汇率等由 AI 做出调价决策。 |
| **舆情监控** | 自动抓取总结订阅的 RSS；监控社媒与新闻中特定关键词并生成分析报告。 |

##### 安全与可控 · 双刃剑

本地优先、隐私可控，但系统级权限伴随潜在风险

它支持**本地化部署**，数据和操作记录保存在自己设备或私有服务器上；提供沙箱隔离、操作审计、自动更新多重安全机制，并支持全链路可观测，让每次模型调用的成本、链路和性能清晰可见。但正因为拥有强大的系统级权限，若非开发者对代码不熟悉，可能因配置不当带来安全风险。

## 02 · 国内变体横评：百虾大战（01166）

自 OpenClaw 爆红，国内厂商迅速跟进，形成「百虾大战」局面。这些「国产小龙虾」的核心优势在于**上手简单**和**本土化适配**。下表汇总主流产品的出品方、免费额度与体验特点。

| 产品 | 出品方 | 免费额度 | 核心特点与体验 |
|---|---|---|---|
| **QClaw** | 腾讯 | **每日 4000 万 Token**或**每日 800 积分** | 额度最慷慨，主打微信直连，上手极简单，社区超 5000 个技能；但模型能力相对较弱，更适合轻度任务。 |
| **WorkBuddy** | 腾讯 | 新用户**5000 积分**+ 每日签到 | 与 QClaw 并称「腾讯双雄」，侧重办公场景，深度集成企业微信、腾讯文档，积分策略友好，入门首选之一。 |
| **悟空** | 阿里 | 每日**100 算粒**（约 500 万 Token），当日清零 | 深度集成钉钉生态，能直接操作审批、文档；对个人用户场景有限。 |
| **AutoClaw** | 智谱 AI | 注册送**500 积分** | 国内首个一键安装的 OpenClaw 应用，预置 50 多个基础技能；免费额度较少，重度使用需付费。 |
| **JVS Claw** | 阿里云 | **7 天全功能免费**+ 200 积分 | 提供真实 Linux 环境，可操作性极高，能自由接入其他模型，被部分开发者评为体验最好。 |
| **ArkClaw** | 字节跳动 | **7 天试用期**（无积分，按请求计次） | 深度整合飞书生态，基于火山引擎，适合高并发任务；免费额度有限，更偏企业用户。 |
| **KimiClaw** | 月之暗面 | 需查阅官方最新信息 | 支持超长上下文，有 5000+ 社区技能，官方评分很高；免费策略较模糊，建议自行查询。 |
| **EasyClaw** | 猎豹移动 | 每日**200 积分**，当日清零 | 权限开放度高、可玩性强；但积分消耗快，重度使用成本高。 |
| **DuClaw** | 百度 | **30 天试用** | 百度系轻量级产品，内置文心大模型和搜索能力。 |
| **StepClaw** | 阶跃星辰 | 限时**5 万名额**：1 个月免费，含 5000 万 Token | 限时免费活动，额度较大但名额有限。 |

> **请注意**：免费策略变动频繁，以上数据截至于 2026 年 5 月 11 日，请以各产品官网最新信息为准。想尝鲜可从「送得多」的腾讯系 QClaw 或 WorkBuddy 上手。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>其他选择</span><h3>开源或平替方案（适合有技术背景者）</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0;margin-bottom:0"><table><thead><tr><th style="width:160px">产品</th><th style="width:130px">出品方</th><th>特点</th></tr></thead><tbody><tr><td><b>LobsterAI</b></td><td>网易有道</td><td>国内<b>首个 100% 开源</b>的桌面 Agent，代码完全公开，被誉为「中国版 OpenClaw」。</td></tr><tr><td><b>CoPaw</b></td><td>阿里</td><td>无 OpenClaw 内核依赖，<b>完全开源</b>（Apache 2.0 协议），支持本地部署，数据安全可控。</td></tr><tr><td><b>LinClaw</b></td><td>七牛云</td><td><b>渠道覆盖最全</b>，MIT 开源，支持私有化部署，适合希望完全掌控数据的开发者。</td></tr></tbody></table></div></div></div>

## 03 · 模型选型：HY3 preview 与 API 性价比（01162）

HY3 preview 是**腾讯旗下混元团队**推出的新一代大语言模型，2026 年 4 月 23 日发布并开源，是腾讯 AI 基础设施在 2026 年 2 月完成重建后训练的首个模型。它是「快慢思考融合」的混合专家（MoE）模型，总参数达**2950 亿**，激活参数约**210 亿**，最大支持**25.6 万 token**上下文长度，也是前 OpenAI 研究科学家、腾讯首席 AI 科学家姚顺雨加盟后主导的首个重要模型成果。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>计价规则</span><h3>TokenHub 积分倍数的秘密</h3></div><div style="padding:14px 16px"><p>腾讯云大模型服务平台 TokenHub 采用后付费模式，用「积分」计量、账单每日结算。你截图里的积分倍数，是腾讯云根据<b>各模型的标准后付费价格</b>折算出来的：</p><pre>1积分 ≈ 1.2元人民币</pre><p>举例：若某模型后付费定价是<code>0.5元/百万Tokens</code>，则其积分倍数为 0.5 ÷ 1.2 ≈<b>0.41</b>。模型越贵，对应的积分倍数自然越高。</p></div></div>

| 模型 | 积分倍数 | API 后付费价格（元/百万 Tokens） |
|---|---|---|
| **GLM-5.1** | **2.5** | 输入 6.0 / 输出 24.0 |
| DeepSeek-V4-Pro | 2.3 | 输入 12.0 / 输出 24.0（限时 2.5 折后） |
| GLM-5.0-Turbo | 2.3 | 输入 5.0-7.0 / 输出 22.0-26.0 |
| GLM-5.0 | 2.0 | 输入 4.0-6.0 / 输出 18.0-22.0 |
| Kimi-K2.6 | 1.6 | 输入 6.5 / 输出 27.0 |
| Kimi-K2.5 | 1.0 | 输入 4.0 / 输出 21.0 |
| MiniMax-M2.7 | 0.7 | 输入 2.1 / 输出 8.4 |
| **Hy3 preview** | **0.5** | 最低输入 1.2 / 最低输出 4.0 |
| MiniMax-M2.5 | 0.5 | 输入 2.1 / 输出 8.4 |

注：Qwen2.5-7B 和 DeepSeek-deep 的具体积分倍数未在截图中体现；按后付费定价，Qwen2.5-7B（约 0.2 美元/百万 Tokens）的积分倍数估算在 0.1 左右。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">怎么选最划算</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>预算有限</dt><dd>选<b>Hy3 preview（0.5 积分）</b>，官方定价最低，是成本控制的好选择。</dd><dt>极致性价比</dt><dd>选<b>DeepSeek-V4-Pro</b>，官方限时 2.5 折，实际输入低至<b>0.025 元/百万 Tokens</b>，输出仅 6 元/百万 Tokens。</dd><dt>顶尖能力</dt><dd>选<b>GLM-5.1（2.5 积分）</b>，当前性能标杆，但成本最高，适合要求苛刻的专业场景。</dd><dt>找平衡点</dt><dd>选<b>MiniMax-M2.7（0.7 积分）</b>，在能力与成本间取得不错平衡。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">成本排序结论</h3><p style="font-size:13.5px;color:inherit;line-height:1.7;margin-bottom:10px">从成本角度，最经济的模型依次是：</p><pre style="margin-bottom:0">Qwen2.5-7B (≈0.1) &gt; Hy3 preview (0.5) &gt; DeepSeek-V4-Pro (0.1, 限时2.5折)</pre><p style="font-size:13px;color:#94a3b8;margin-top:10px">看常规后付费价格，Hy3 preview 无疑是当前积分倍数最低的选择。</p></div></div>

> **口径说明**：以上价格信息截至 2026 年 5 月，各平台政策可能随时调整，建议使用前以官网最新报价为准。
