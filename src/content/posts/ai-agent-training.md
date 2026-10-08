---
title: "AI Agent 提效培训 · WorkBuddy 专题"
description: "面向食品生产企业的培训课件：概念科普与七大业务场景实战。"
pubDatetime: 2026-09-08
category: "AI与Agent"
kind: "手册"
tags: ["Agent", "培训", "WorkBuddy"]
---

GERVAS

AI Agent 培训

模块

<svg viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>

01

AI 基础概念

02

技术预备

03

主流 Agent 盘点

04

WorkBuddy 数字员工

05

场景实战（上）

06

场景实战（下）

07

数据可视化与文档

08

Prompt 与 Skill

09

准则 · 安全 · 路线图

←

1 / 22

→

北京同仁堂健康药业（青海）有限公司 · 内部培训 · 2026

## 让 AI Agent 成为你的<br>

从概念到实战：理解 Token、API、Skill、Agent 与大模型的关系，<br>

按→或用顶部按钮翻页 · 支持左右滑动

<img src="../../img/ai-agent-training/assets/eastseao-avatar.jpg" alt="讲师头像" style="width:220px;height:220px;object-fit:cover;border-radius:50%;border:4px solid #2456e6;box-shadow:0 0 40px rgba(36,86,230,.22)">

### 今天讲什么

九个模块：看懂 AI → 备好技术 → 选对工具 → 落地工作 → 沉淀技能

### 五个概念，一个比喻讲清楚

把 AI 想象成一位新入职的"数字员工"，一切都好理解了

<div style="display:grid;gap:14px;margin:14px 0"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>🧠</div><h3>大模型</h3><p><b style="color:#0f172a">大脑</b>。负责思考、理解语言、推理和生成内容。大脑越强，员工越聪明（GPT、Claude、混元、GLM、DeepSeek…）</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>📊</div><h3>Token</h3><p><b style="color:#0f172a">流量</b>。模型按 Token 计费和记忆，1 Token ≈ 0.5~1.5 个汉字。对话越多，流量消耗越大</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>🔌</div><h3>API</h3><p><b style="color:#0f172a">插座</b>。标准接口，让程序能把任务交给大模型、把能力接入业务系统，随插随用</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>🎒</div><h3>Skill</h3><p><b style="color:#0f172a">技能包</b>。教员工掌握的具体本领：读 Excel、查数据库、生成报告、调用系统……技能越多越能干</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>🤖</div><h3>Agent</h3><p><b style="color:#0f172a">员工</b>。大脑+技能+工具+自主规划，能理解目标、拆解步骤、执行任务、汇报结果</p></div></div>

💡 一句话总结：

大模型

是脑子，

Token

是口粮，

API

是插座，

Skill

是技能包，

Agent

= 前四者组装出来能干活的

员工

。

### 为什么是 Agent，而不是"聊天框"？

从"只出主意"到"真干活"的跨越

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>普通对话 AI（Chatbot）</span><ul><li>你问一句，它答一句，被动响应</li><li>只会生成文字，不能操作系统和文件</li><li>需要你复制粘贴到各个工具里自己执行</li><li>适合：查资料、写文案、头脑风暴</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0;border-color:inherit"><span>智能体（Agent）</span><ul><li>理解目标后<b style="color:#0f172a">自主规划</b>：拆步骤 → 调工具 → 检查结果 → 迭代</li><li>能读写文件、查表格、发消息、跑脚本</li><li>交付的是<b style="color:#0f172a">成果物</b>：报告、表格、PPT、待办</li><li>适合：端到端完成一项完整工作</li></ul></div></div>

接收目标

"帮我调研黑果枸杞原料趋势"

→

自主拆解

搜索→筛选→整理→测算

→

调用工具

浏览器 / Excel / 知识库

→

交付成果

报告.md + 数据表 + 结论

### 技术预备 ①：Markdown 与 GitHub

AI 时代的两块基石——写提示词用它，管技能包也用它

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>📝 Markdown：轻量标记语言</span><p style="margin-bottom:8px">2004 年由约翰·格鲁伯（John Gruber）创造，使用易读易写的纯文本格式编写文档，然后转换成结构化的 HTML。</p><ul style="margin-bottom:10px"><li><b style="color:#0f172a">为什么产品部要学？</b>写提示词、写 Skill 文档、写知识库文章，都用 Markdown</li><li>大多数 AI 工具（WorkBuddy、ima 等）原生支持</li><li>比 Word 轻量、比纯文本有结构</li></ul><table><tr><th>语法</th><th>效果</th><th>示例</th></tr><tr><td><code># / ##</code></td><td>一级 / 二级标题</td><td># 产品立项报告</td></tr><tr><td><code>- / 1.</code></td><td>无序 / 有序列表</td><td>- 黑枸杞原浆</td></tr><tr><td><code>**加粗**</code></td><td><b>加粗</b></td><td>**核心卖点**</td></tr><tr><td><code>[文字](URL)</code></td><td>链接</td><td><a href="https://www.tongrentang.com" target="_blank" style="color:#2456e6">同仁堂官网</a></td></tr><tr><td><code>| 列1 | 列2 |</code></td><td>表格</td><td>见本表</td></tr><tr><td><code>![图片名](URL)</code></td><td>插入图片</td><td>用于可视化图表</td></tr></table></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>🐙 GitHub：技能包的仓库</span><p style="margin-bottom:10px">基于 Git 的项目托管与协作平台，全球最大的开源社区。</p><ul><li>可找到大量现成的<b style="color:#0f172a">AI 工具和 Skill 资源</b></li><li>团队共享和管理提示词模板、Skill 文件</li><li>每个 Skill 用 Git 做版本管理：<b style="color:#0f172a">可迭代、可回滚</b></li></ul><div>对我们来说：部门的高频工作流（如&quot;黑枸杞原浆成本测算&quot;）可以沉淀成 Skill 文件，放在 GitHub 统一管理，新同事拿来即用。</div></div></div>

### 技术预备 ②：产品类 Agent 已能"一句话生成"

2026 年，用自然语言"雇"一个数字员工已成为现实

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>阿里 QoderWake 1.0</span><h3>岗位级数字员工</h3><p>2026 年 9 月发布。在控制台描述岗位需求，系统产出角色草稿（职责、协作关系、权限与红线），确认后数字员工即可&quot;入职&quot;。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>蚂蚁百宝箱</span><h3>一键生成企业智能体</h3><p>自然语言一键生成企业级智能体，无需写代码，适合快速搭建业务小助手。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>WorkBuddy Enterprise</span><h3>腾讯云一站式平台</h3><p>面向企业的一站式 AI 智能体平台，可将 Agent 能力深度融入企业的研发、办公与业务全流程。</p></div></div>

🚀 对我们公司来说：不需要写代码，用自然语言描述"我需要一个负责原料行情监控的助手"，AI 就能帮你生成一个专属 Agent。

### 市面主流 Agent 智能体盘点

2026 年视角：通用型、编程型、办公型三大阵营

<table><tr><th>产品</th><th>阵营</th><th>特点</th><th>适合同仁堂青海的用途</th></tr><tr><td>WorkBuddy</td><td>企业办公 Agent</td><td>贴合企业流程，文档/表格/知识库一站式</td><td>⭐ 本次培训主角：日常办公全能助手</td></tr><tr><td>ChatGPT（OpenAI）</td><td>通用型</td><td>生态最成熟，多模态强</td><td>创意生成、方案初稿、翻译</td></tr><tr><td>Claude（Anthropic）</td><td>通用/长文本</td><td>长文档理解出色</td><td>超长报告阅读、合规文档比对</td></tr><tr><td>腾讯混元</td><td>通用型（国产）</td><td>中文理解强，与腾讯生态打通</td><td>国产化要求场景、日常问答</td></tr><tr><td>Coze / 扣子（字节）</td><td>低代码搭建</td><td>拖拽式搭建 Agent，插件丰富</td><td>搭建部门专属小工具</td></tr><tr><td>Manus</td><td>任务执行型</td><td>给目标直接交付成果物</td><td>一次性深度调研任务</td></tr><tr><td>WPS AI</td><td>生产力内嵌</td><td>嵌入 WPS，文档表格提效</td><td>文档表格日常微操</td></tr></table>

选型口诀：

日常办公用 WorkBuddy

，创意用 ChatGPT，长文档用 Claude，国产合规用混元。

### WorkBuddy：你的全能数字员工

为什么本次培训以它为核心——因为它离我们的工作流最近

WorkBuddy Enterprise 是腾讯云面向企业打造的一站式 AI 智能体平台，以腾讯混元大模型为核心并支持多模型混合接入。它支持**一句话下达任务**，可自主规划执行多步骤复杂任务，交付可直接验收的成果。

<div style="display:grid;gap:14px;margin:14px 0"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>📄 文档</span><h3>会写</h3><p>立项书、结题报告、方案、周报，一句话生成初稿</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>📊 数据</span><h3>会算</h3><p>读 Excel、跑公式、核成本、比价格，BOM 梳理自动化</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>🔍 研究</span><h3>会查</h3><p>联网检索市场趋势、原料情报、法规动态</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>🗂️ 整理</span><h3>会管</h3><p>知识库沉淀、文件归类、会议纪要转待办</p></div></div>

📌 使用心法：把 WorkBuddy 当

新来的聪明实习生

——目标讲清楚、资料给到位、过程多确认、结果做把关。

### 场景实战（上）：市场洞察与产品策划

扎根柴达木：黑枸杞、红枸杞、冬虫夏草、藜麦、沙棘等八大系列 70 余种产品

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>① 特色原料市场趋势挖掘</span><p><b style="color:#0f172a">背景：</b>公司位于青海省海西州德令哈市，2017 年落地，致力于青藏高原特色生物资源的全产业链开发与建设。已累计采购枸杞、藜麦等青藏特色资源 3000 余吨，带动省内农副产品销售超 5 亿元；主营黑枸杞、红枸杞、冬虫夏草、藜麦、沙棘等八大系列 70 余种产品。</p><p style="margin:8px 0"><b style="color:#0f172a">痛点：</b>青海特色原料（黑枸杞、沙棘、藜麦、冬虫夏草）市场行情变化快，竞品动态难追踪。<br></p><div>&quot;检索近 90 天'黑果枸杞'在功能性食品和饮品中的应用趋势，重点关注：① 市场规模与增速 ② 主要竞品及定价 ③ 消费者认知与口碑 ④ 潜在机会点与风险提示。输出：趋势摘要 + 数据表格 + 机会/风险清单，附来源链接。&quot;</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>② 产品概念与营销策划</span><p><b style="color:#0f172a">背景：</b>公司已推出黑果枸杞原浆、枸杞原浆、沙棘原浆、西洋参枸杞原浆等药食同源植物原浆经典产品。2025 年，同仁堂植物原浆罐头系列荣登 iSEE 创新品牌百强榜。</p><p style="margin:8px 0"><b style="color:#0f172a">痛点：</b>新产品概念策划耗时长，竞品对标不系统。<br></p><div>&quot;你是一名食品饮料产品经理。针对 25-40 岁都市白领人群，基于'黑果枸杞原浆'开发 5 个新产品概念（口味延伸/功能定位/场景细分），每个含：产品定位 / 核心卖点（3条）/ 一句话文案 / 目标人群洞察 / 对标竞品及差异点。参考同仁堂现有植物原浆产品线风格。&quot;</div></div></div>

⚠️ 提醒：市场数据务必让 Agent 附上

来源链接

，关键数字人工复核。

### 场景实战（下）：研发合规与成本测算

专业判断留给人，重复劳动交给 Agent

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>③ 配方研发与合规筛查</span><p><b style="color:#0f172a">背景：</b>公司产品涵盖黑枸杞原浆、沙棘原浆等食品类别。食品生产涉及 GB 2760（食品添加剂使用标准）、GB 28050（预包装食品营养标签通则）等法规。</p><p style="margin:8px 0"><b style="color:#0f172a">痛点：</b>配方合规筛查依赖人工逐条比对，效率低、易遗漏。<br></p><div>&quot;你是一名食品合规专员。请筛查这份黑枸杞原浆配方（附配方表）是否符合 GB 2760-2024《食品安全国家标准 食品添加剂使用标准》和 GB 28050《预包装食品营养标签通则》。重点检查：① 添加剂是否超范围/超限量 ② 营养标签声称是否合规 ③ 原料是否在药食同源目录中。以表格输出：原料/风险类型/判定/法规依据。&quot;</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>④ 原料成本测算与采购优化</span><p><b style="color:#0f172a">背景：</b>公司主要原料包括黑枸杞、红枸杞、沙棘、藜麦、冬虫夏草等青藏特色资源，已建立从原料收购、精深加工到市场销售的全链条闭环管理。</p><p style="margin:8px 0"><b style="color:#0f172a">痛点：</b>原料价格波动大（受气候、季节影响），成本测算依赖人工 Excel。<br></p><div>&quot;按此黑枸杞原浆配方与当前原料市场价（附表），测算 10 万袋（30ml/袋）的单品原料成本。若目标原料成本 ≤X 元/袋，给出降本替代建议（如改用不同产地枸杞、调整配比等），并附风险提示。&quot;</div></div></div>

### 场景实战（下）：立项撰写与结题报告

最耗时的"文书工作"，恰是 Agent 最强的战场

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>⑤ 立项撰写</span><p><b style="color:#0f172a">背景：</b>公司持续加大生产投入与技术升级，不断优化生产工艺、提升产品品质。新产品开发（如新口味原浆、功能型饮品）需要规范立项。</p><p style="margin:8px 0"><b style="color:#0f172a">痛点：</b>立项报告撰写耗时长，格式不统一。<br></p><div>&quot;按公司新产品立项模板，基于我提供的沙棘+枸杞复合原浆市场调研简报和成本测算，生成立项报告初稿。缺失信息用【待补充】标出，数据自动回填到对应章节。&quot;</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>⑥ 结题报告</span><p><b style="color:#0f172a">痛点：</b>项目结题时需汇总大量过程数据，对照目标分析偏差。</p><p style="margin:8px 0"><b style="color:#0f172a">Agent 做：</b>汇总立项书、过程记录、检测数据，自动生成对照式结题报告：目标 vs 实际、偏差分析、经验沉淀。</p><div>&quot;对照黑果枸杞原浆升级项目立项书指标，用试产数据写结题报告：① 目标 vs 实际对比表 ② 2 项指标偏差原因 ③ 改进措施与经验沉淀。&quot;</div></div></div>

### 场景实战（下）：BOM 梳理与成本匹配

八大系列 70 余种产品的存量管理

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>⑦ BOM 梳理与成本匹配</span><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr));margin-top:6px"><div><p><b style="color:#0f172a">背景</b></p><p>公司产品线涵盖八大系列 70 余种产品，BOM（物料清单）管理复杂。</p></div><div><p><b style="color:#0f172a">痛点</b></p><p>多版本 BOM + 频繁变动的原料价格，人工匹配易出错。</p></div><div><p><b style="color:#0f172a">Agent 做</b></p><p>上传多版本 BOM + 最新价格表，批量匹配、标红缺失与涨价项，输出更新后 BOM 与差异报告。</p></div></div><div style="margin-top:14px">&quot;用附表的最新原料价格更新全量产品 BOM（Excel），输出：① 更新后成本汇总 ② 涨跌幅 TOP10 原料 ③ 未匹配原料清单（需人工确认）。&quot;</div></div>

### AI 赋能数据可视化与结构化文档输出

"从一堆零散数据和素材，到一份可直接交付的精美报告——从 3 小时缩短到 15 分钟"

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr));margin-bottom:6px"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><h3>😫 我们经常面对</h3><ul><li>一堆零散的实验数据、生产记录、检测报告</li><li>群聊里散落的沟通记录和决策要点</li><li>Excel 里密密麻麻的数字，看不出趋势和结论</li><li>最后要整理成<b style="color:#0f172a">结构清晰、图表美观的正式报告</b>给领导汇报或归档</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><h3>🤝 AI + Typora 的分工</h3><ul><li><b style="color:#0f172a">AI 负责&quot;想&quot;和&quot;整理&quot;</b>：清洗数据、提炼要点、生成结构化内容</li><li><b style="color:#0f172a">Typora 负责&quot;排版&quot;和&quot;导出&quot;</b>：所见即所得，一键导出 PDF/图片</li><li>两者结合，实现从原始素材到成品交付的<b style="color:#0f172a">全流程提效</b></li></ul></div></div>

📥 原始素材投放

零散数据/聊天记录<br>

→

🧹 AI 结构化整理

生成 Markdown<br>

→

📊 可视化生成

图表代码/数据看板<br>

→

📤 成品交付

Typora 一键导出<br>

### AI 帮你整理与可视化的四种方式

每种能力都附一条可直接照抄的指令

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>能力一：零散数据 → 结构化表格</span><div>&quot;你是食品行业数据分析师。这是沙棘原浆 2026 年 1-8 月的产量、合格率、原料损耗率原始数据（附 Excel）。请：① 清洗缺失值和异常值 ② 按月汇总成结构化表格 ③ 计算环比增长率 ④ 标注异常月份及可能原因（如设备检修、原料批次波动）。&quot;</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>能力二：数字表格 → 可视化图表</span><div>&quot;基于黑枸杞和沙棘原浆的季度销量对比表（附表），生成数据看板布局建议：① 折线图展示销量趋势 ② 饼图展示渠道占比 ③ 柱状图展示区域对比。描述每个图表的 X/Y 轴含义、数据标签和标题，输出 Markdown 格式，配 mermaid 图表代码或说明文字。&quot;</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>能力三：多份零散文件 → 一份结构报告</span><div>&quot;这是三份文件：① 黑枸杞原浆市场调研简报 ② 成本测算表 ③ 试产报告。请汇总生成《黑枸杞原浆新品上市可行性报告》，按：一、项目概述 / 二、市场分析 / 三、成本与收益测算 / 四、风险与应对 / 五、结论与建议。关键数据从源文件提取并标注来源。&quot;</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>能力四：长文档 → 一页纸摘要 + 图表</span><div>&quot;把这份 80 页《2026 中国枸杞深加工行业白皮书》浓缩成一页纸精华摘要：3 个核心趋势 + 5 组关键数据 + 对我们的 3 点启示。关键数据转成 Markdown 表格，便于后续做成图表。&quot;</div></div></div>

### Typora：结构化文档的"最后一公里"

极简 Markdown 编辑器，所见即所得

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><h3>✨ 为什么选择 Typora</h3><ul><li>界面干净，无干扰，专注写作</li><li>支持 LaTeX 数学公式、表格、代码块、Mermaid 图表</li><li><b style="color:#0f172a">一键导出 PDF</b>（保留目录结构和样式）</li><li><b style="color:#0f172a">一键导出图片</b>，适合插入 PPT 或群聊分享</li><li>支持自定义 CSS 主题，适配企业品牌风格</li></ul><div style="margin-top:14px">💡 小技巧：需要公司 Logo？在&quot;偏好设置 → 导出 → PDF&quot;添加页眉页脚插图片；长图分享可导出 HTML 后浏览器截图；多人协作把 .md 上传 GitHub 或 ima 知识库。</div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><h3>🪜 操作步骤</h3><table><tr><th>步骤</th><th>操作</th><th>说明</th></tr><tr><td>①</td><td>WorkBuddy 执行 AI 指令</td><td>得到 Markdown 格式回复</td></tr><tr><td>②</td><td>复制粘贴到 Typora</td><td>所见即所得，即时渲染</td></tr><tr><td>③</td><td>调整样式（可选）</td><td>&quot;主题&quot;切换风格</td></tr><tr><td>④</td><td>文件 → 导出 → PDF</td><td>带目录、书签的正式报告</td></tr><tr><td>⑤</td><td>文件 → 导出 → 图片</td><td>PNG，适合 PPT/群聊</td></tr></table></div></div>

### 实操案例：沙棘原浆 2026 上半年经营分析报告

四步，15 分钟，交付一份管理层级正式报告

<div style="display:grid;gap:14px;margin:14px 0"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>1</div><h3>投放素材</h3><p>财务部的销量表、生产部的损耗记录、市场部的竞品简报，全部丢给 WorkBuddy</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>2</div><h3>AI 处理</h3><p>汇总素材，按五大章节结构生成 Markdown 报告（见下方指令）</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>3</div><h3>人工微调</h3><p>在 Typora 中核对关键数字，调整措辞</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>4</div><h3>一键交付</h3><p>导出 PDF（带书签），邮件发送给管理层</p></div></div>

"汇总这些素材，生成《沙棘原浆 2026 上半年经营分析报告》，按以下结构：一、总体经营概况 / 二、销量趋势（用折线图描述） / 三、成本与毛利分析（用表格对比各月） / 四、竞品对标（用雷达图描述维度） / 五、下半年重点工作建议。输出为 Markdown 格式。"

### Prompt：给 AI 的"临时指令"

就像你站在新人旁边，当场口头交代任务——只在当前对话生效

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0;margin-bottom:20px"><h3>🎯 CRISPE 框架</h3><table><tr><th>字母</th><th>含义</th><th>说明</th></tr><tr><td><b>C</b></td><td>角色（Character）</td><td>指定 AI 扮演的角色（如&quot;资深食品研发工程师&quot;）</td></tr><tr><td><b>R</b></td><td>背景（Reason/Context）</td><td>提供上下文（如&quot;我们公司主营青藏特色原料深加工&quot;）</td></tr><tr><td><b>I</b></td><td>指令（Instruction）</td><td>明确要做什么（如&quot;筛查配方合规性&quot;）</td></tr><tr><td><b>S</b></td><td>格式（Structure/Format）</td><td>指定输出格式（如&quot;表格输出&quot;）</td></tr><tr><td><b>E</b></td><td>示例（Example）</td><td>提供参考样例</td></tr></table></div>

💡 直觉版万能公式：

角色 + 背景 + 任务 + 要求 + 格式

——指令质量决定产出质量。

### Skill：从"临时指令"到"永久技能"

Prompt 是便签纸，Skill 是员工手册

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><h3>⚖️ Prompt vs Skill</h3><table><tr><th>维度</th><th>Prompt</th><th>Skill</th></tr><tr><td>生命周期</td><td>一次性</td><td>持久化、可复用</td></tr><tr><td>可发现性</td><td>每次手动贴</td><td>Agent 自动匹配</td></tr><tr><td>可移植性</td><td>跟着聊天窗口走</td><td>跨项目、跨平台</td></tr><tr><td>版本管理</td><td>基本没有</td><td>Git 管理，可迭代</td></tr><tr><td>团队协作</td><td>各写各的</td><td>统一分发、统一标准</td></tr></table></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><h3>🛠️ 如何制作一个 Skill（三步）</h3><ul><li><b style="color:#0f172a">第一步 · 梳理 SOP：</b>把任务拆成标准步骤，如&quot;每周原料行情简报&quot; = 搜索 → 筛选 → 整理 → 测算 → 生成报告</li><li><b style="color:#0f172a">第二步 · 写出 SKILL.md：</b>用 Markdown 写清技能名称、触发条件、执行步骤、输出格式、校验规则</li><li><b style="color:#0f172a">第三步 · 打包与测试：</b>SKILL.md + 模板/参考文档放同一文件夹，在 WorkBuddy 中测试迭代</li></ul><div>Skill = 元数据（Metadata）+ 执行指令（SOP）+ 示例模板（Examples）+ 校验规则（Tools）</div></div></div>

### 腾讯 SkillHub：AI 技能的"应用商店"

专为中国用户优化的 AI Skills 社区平台：发现、安装、发布、管理

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>8万+</div><h3>收录 Skills</h3><p>截至 2026 年中，覆盖办公、研发、数据等各类场景</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>3000万</div><h3>累计下载</h3><p>上线 2 个月下载量突破 3000 万次</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div>多平台</div><h3>支持工具</h3><p>WorkBuddy、QClaw、ima 等腾讯产品，及 Claude Code、Cursor 等主流工具</p></div></div>

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr));margin-top:20px"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>📥 下载</span><p>直接获取现成办公 Skill（Excel 处理、报告生成等）</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>📤 上传</span><p>把公司高频工作流（如&quot;黑枸杞原浆成本测算&quot;）封装成专属 Skill</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>🤝 共享</span><p>团队共用一套标准化 Skill，新人上手更快</p></div></div>

💡 行动建议：本周先去 SkillHub（skillhub.cn）浏览，找到 3 个最贴合你日常工作的 Skill 安装试用。

### 用好 Agent 的行为准则

🎯 万能公式示例："你是一名**食品合规专员**（角色）。我们公司位于青海德令哈，主营**黑枸杞原浆和沙棘原浆**（背景）。请筛查这份配方的**添加剂合规性**（任务），依据 GB 2760-2024，重点看**防腐剂和抗氧化剂**（要求），以**表格输出：原料/限量/结论/依据**（格式）。"

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><h3>✅ 要做</h3><ul><li>给足上下文和参考资料（公司背景、产品信息、法规文件）</li><li>复杂任务拆步骤、分多次对话</li><li>要求附来源、标出不确定项</li><li>不满意就追问迭代</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><h3>❌ 别做</h3><ul><li>一句话下模糊指令</li><li>把 AI 输出当最终稿直接提交</li><li>上传涉密数据到未授权工具</li><li>期待 100% 准确却不做复核</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><h3>🔐 安全红线</h3><ul><li>公司机密配方、客户数据不外传</li><li>使用公司批准的工具与账号</li><li>合规结论以法规原文和专业人士为准</li><li>AI 生成内容需人工署名负责</li></ul></div></div>

### 上手路线图：三步走

不要试图一天掌握全部，按周推进

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>第 1 周 · 试用</span><h3>从一个小场景开始</h3><ul><li>每天用 WorkBuddy 完成 1 件文档工作</li><li>如：会议纪要整理、报告摘要</li><li>目标：建立手感，消除陌生感</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>第 2-3 周 · 融入</span><h3>接管 2-3 个高频场景</h3><ul><li>原料行情简报 / 成本测算 / 立项初稿</li><li>常用指令存成个人&quot;指令库&quot;</li><li>目标：单场景节省 50% 以上时间</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><span>第 4 周+ · 沉淀</span><h3>指令升级为 Skill</h3><ul><li>优质指令升级为 Skill</li><li>共享到团队知识库或 SkillHub</li><li>目标：形成部门 AI 工作范式</li></ul></div></div>

📈 衡量标准很简单：同样一件事，

上周花 3 小时，本周花 1 小时

——省下的时间用来做只有人能做的判断和创意。

## AI 不会取代你，<br>

同仁堂青海扎根柴达木盆地，依托青藏高原特色生物资源，已累计采购特色资源 3000 余吨，带动农副产品销售超 5 亿元。在"京青合作、绿色发展"的大背景下，善用 AI 工具将帮助我们在原料管理、产品研发、合规品控等环节实现效率跃升。

**今天回家就做一件事**：挑一项你最烦的文档或数据工作，交给 WorkBuddy 试试，然后打开 Typora，把结果导出成 PDF——感受 15 分钟完成一份正式报告的快感。

Q & A · 谢谢大家 🙌
