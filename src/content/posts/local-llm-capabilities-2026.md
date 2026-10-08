---
title: "本地开源模型能力介绍"
description: "Qwen2.5-7B、Mistral 7B、Pygmalion 7B、dolphin 等本地开源模型的规格、评测与适用场景。"
pubDatetime: 2026-03-31
category: "AI与Agent"
kind: "长文"
tags: ["Qwen2.5-7B", "Mistral 7B", "Pygmalion 7B", "dolphin", "本地部署"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00796-2026-03-24 Qwen2.5-7B-Instruct 模型能力介绍00797-2026-03-24 Pygmalion 7B 角色扮演模型能力00798-2026-03-24 Mistral7B 模型能力介绍00817 + 00818-2026-03-31 dolphin-2.2.1-mistral-7b 擅长的能力（两份同名笔记内容相同，合并为一条）

## 01 · 四模型总览对照表（00796 / 00797 / 00798 / 00817+00818）

四款都是 7B 量级、可在消费级显卡上跑的开源模型，但定位差异很大：**Qwen2.5-7B**是综合指令模型，**Mistral 7B**是「以小博大」的效率标杆，**Pygmalion 7B**专做角色扮演，**dolphin-2.2.1-mistral-7b**是基于 Mistral 7B 的再微调。

| 模型 | 参数 / 底座 | 上下文 | 定位 | 关键特点 |
|---|---|---|---|---|
| **Qwen2.5-7B-Instruct** | 约 76 亿（7.61B），阿里通义千问 | 131,072（128K） | 指令遵循 / 对话通用 | 知识、编程数学、长文本、结构化数据全面提升；支持 29 种以上语言；Apache-2.0 可商用。 |
| **Mistral 7B** | 73 亿（7.3B），Mistral AI，2023 年 | 理论堆叠可达 131K | 性能/效率平衡 | 几乎所有基准超越 Llama 2 13B；GQA + 滑动窗口注意力；Apache 2.0；v0.3 支持函数调用。 |
| **Pygmalion 7B** | 70 亿（7B），基于 Meta LLaMA-7B 微调 | 约 4096 token | 角色扮演 / 虚构对话 | 保持角色性格语气一致；未做安全对齐、易幻觉，仅供娱乐。 |
| **dolphin-2.2.1-mistral-7b** | 基于 Mistral-7B 的 dolphin 微调版 | —（沿用 Mistral 7B 底座） | 对话/指令向微调 | 原笔记仅记录了查询标题，未留存详细回答，详见第 05 节说明。 |

## 02 · Qwen2.5-7B-Instruct（00796 · 2026-03-24）

阿里云通义千问团队发布的 70 亿参数开源模型，专为**指令遵循和对话场景**优化，在知识掌握、编程与数学、长文本、结构化数据理解上较前代显著提升。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>技术规格</span><h3>架构与参数</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:170px">技术规格</th><th>参数（照录）</th></tr></thead><tbody><tr><td>参数规模</td><td>约<b>76 亿（7.61B）</b></td></tr><tr><td>架构特点</td><td>基于 Transformer，采用 RoPE、SwiGLU、RMSNorm 和 GQA（分组查询注意力）</td></tr><tr><td>上下文长度</td><td>支持长达<b>131,072（128K）tokens</b></td></tr><tr><td>生成能力</td><td>单次最多生成<b>8,192（8K）tokens</b></td></tr><tr><td>训练数据</td><td>预训练数据从 Qwen2 的 7 万亿 tokens 扩展至<b>最高 18 万亿 tokens</b></td></tr><tr><td>开源协议</td><td><b>Apache-2.0</b>，支持免费商用</td></tr></tbody></table></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>基准评测</span><h3>能力维度与评测分数</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">能力维度</th><th style="width:200px">关键特点</th><th>评测表现（照录）</th></tr></thead><tbody><tr><td>综合知识与推理</td><td>知识储备丰富，通用理解出色</td><td>MMLU 85+；MMLU-Pro 56.3</td></tr><tr><td>编程与代码</td><td>编程能力显著增强，多语言代码任务</td><td>HumanEval 85+；MBPP 79.2</td></tr><tr><td>数学与逻辑</td><td>解决更复杂数学问题</td><td>MATH 80+；GSM8K 91.6</td></tr><tr><td>指令遵循与对话</td><td>理解复杂指令、多系统提示，适合角色扮演</td><td>MT-Bench 8.75；Arena-Hard 52.0</td></tr><tr><td>结构化数据处理</td><td>理解和生成表格、JSON</td><td>官方文档强调能力提升</td></tr><tr><td>多语言支持</td><td>支持中文、英文等 29 种以上语言</td><td>官方文档确认</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:14px"><h5>适用场景</h5><ul><li>智能对话助手：客服、虚拟角色扮演等高情商聊天机器人。</li><li>代码生成与辅助：代码编写、解释、调试。</li><li>内容创作与总结：文章/报告生成，长文档摘要。</li><li>结构化输出：从文本提取信息输出为 JSON 的自动化流程。</li><li>多语言应用：跨国业务或多语言环境。</li></ul></div></div></div>

## 03 · Mistral 7B（00798 · 2026-03-24）

Mistral AI 于 2023 年发布的开源模型，以 73 亿参数的「小巧」体积实现超越许多更大模型的性能，因**性能与效率**的平衡而受欢迎。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>核心技术</span><h3>两项架构创新：GQA + SWA</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>分组查询注意力 GQA</dt><dd>显著加速推理、减少解码时内存需求，允许更大批量、提升总吞吐量，对实时应用关键。</dd><dt>滑动窗口注意力 SWA</dt><dd>限制每个 token 只能看到前文固定数量的 token；配合滚动缓冲区缓存，处理 32k 超长序列时缓存内存用量减少<b>8 倍</b>而不影响质量；理论上堆叠注意力层最终上下文跨度可达<b>131K</b>token。</dd></dl><p style="margin:14px 0 10px">技术报告结论：几乎所有基准超越 Llama 2 13B（130 亿），在推理、数学、代码生成上超越 Llama 1 34B（340 亿）；处理推理/理解/STEM 任务时表现相当于其尺寸<b>3 倍大</b>的 Llama 2 模型。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>基准对比</span><h3>与 Llama 2 13B 对比（照录）</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:130px">能力领域</th><th style="width:160px">基准测试</th><th style="width:120px">Mistral 7B</th><th style="width:130px">Llama 2 13B</th><th>小结</th></tr></thead><tbody><tr><td>综合知识</td><td>MMLU</td><td><b>60.1%</b></td><td>55.6%</td><td>全面超越</td></tr><tr><td>常识推理</td><td>HellaSwag</td><td><b>81.3%</b></td><td>80.7%</td><td>领先</td></tr><tr><td>世界知识</td><td>TriviaQA</td><td><b>75.1%</b></td><td>69.6%</td><td>显著领先</td></tr><tr><td>数学能力</td><td>GSM8K (8-shot)</td><td><b>47.5%</b></td><td>34.3%</td><td>大幅领先</td></tr><tr><td>代码生成</td><td>HumanEval (0-shot)</td><td><b>28.1%</b></td><td>18.9%</td><td>大幅领先</td></tr></tbody></table></div><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>获取方式</dt><dd>Apache 2.0 开源，可在 Hugging Face 下载；通过 Ollama 一键本地运行（至少 8GB 内存）。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>版本</dt><dd>有 Instruct（指令）与 Text（文本补全）两版；最新 v0.3 支持函数调用，方便构建 Agent。</dd></dl></div></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:14px"><h5>使用提醒</h5><ul><li>应用：代码生成、机器翻译/摘要/问答/情感分析、创意写作、教育科研。</li><li>完全开源版本可能缺乏内置内容安全过滤，使用时自行注意。</li></ul></div></div></div>

## 04 · Pygmalion 7B（角色扮演）（00797 · 2026-03-24）

专注**角色扮演和虚构对话**的对话式模型，基于 Meta 的 LLaMA-7B 微调，目标是创造沉浸式交互体验，而非通用安全助手。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>核心能力与技术规格</span><h3>角色、对话、创意与提示格式</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">能力维度</th><th>说明</th></tr></thead><tbody><tr><td><b>角色扮演（核心优势）</b></td><td>根据角色描述在对话中完美扮演，保持人物性格、语气一致。</td></tr><tr><td><b>多轮对话</b></td><td>跟踪对话历史、理解上下文，进行连贯自然的连续对话，适合复杂叙事。</td></tr><tr><td><b>创意写作</b></td><td>协助创作虚构故事、生成对话、构思情节、塑造人物，输出偏富有想象力与细节。</td></tr><tr><td><b>上下文理解</b></td><td>通过特定提示格式理解「角色设定」和「对话历史」。</td></tr></tbody></table></div><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0;margin-top:14px"><dt>底座</dt><dd>Meta LLaMA-7B，70 亿（7B）参数。</dd><dt>上下文</dt><dd>约<b>4096 个 token</b>，足以处理中等长度对话或故事片段。</dd><dt>部署</dt><dd>有 GPTQ、GGUF 等量化版本，优化后可在<b>8GB–16GB 显存</b>的消费级硬件流畅运行。</dd></dl><p style="margin:14px 0 8px">标准提示格式（模型需按此格式输入效果最佳）：</p><div style="margin:14px 0">[角色名称]'s Persona: [角色的详细描述] &lt;START&gt; [对话历史] You: [你的输入] [角色名称]:</div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>关键局限性（务必照用）</h5><ul><li>专为娱乐设计：不适合需要高准确性或安全性的严肃场景。</li><li>可能生成不当内容：未经过安全和无害化对齐微调。</li><li>事实准确性差：非常容易「产生幻觉」，重创意轻事实。</li><li>不具备真正的常识、情感或抽象推理，只是按训练数据模式做文本预测。</li></ul></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>LM Studio 调参</span><h3>用 LM Studio 部署时的推荐参数</h3></div><div style="padding:14px 16px"><p>笔记特别说明：LM Studio 通常会自动从模型文件读取正确提示模板，若已能正常工作可不改。需手动调时按下面来。</p><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:180px">参数</th><th>推荐值</th></tr></thead><tbody><tr><td>Temperature（温度）</td><td><b>0.7 – 1.1</b>，稍高更具创造性，适合角色扮演。</td></tr><tr><td>Context Length（上下文长度）</td><td>设为<b>4096</b>，即该模型支持的最大上下文。</td></tr><tr><td>Repeat Penalty（重复惩罚）</td><td><b>1.1</b>左右，防止长对话陷入重复句循环。</td></tr></tbody></table></div><p style="margin-bottom:0">进阶：在 Advanced → Chat Template 选 Custom，用 Jinja 模板把用户输入格式化成<code>You: …</code>、模型回复前加角色名与冒号；注意保留<code>&lt;START&gt;</code>和角色名后冒号这些模型习得的分隔符，也不要加「请遵守道德规范」之类安全指令（对未对齐模型无效且干扰角色扮演）。</p></div></div>

## 05 · dolphin-2.2.1-mistral-7b（合并条目）（00817 + 00818 · 2026-03-31）

原笔记 00817 与 00818 同名、同日、内容完全相同，按要求合并为一条。需要如实说明：**这两份笔记当时只记录了提问标题「dolphin-2.2.1-mistral-7b 擅长的能力」，并未留存 AI 的回答正文**，因此本页不为其编造任何评测分数或参数。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>合并条目</span><h3>dolphin-2.2.1-mistral-7b</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">项目</th><th>可确认信息</th></tr></thead><tbody><tr><td>模型名称</td><td>dolphin-2.2.1-mistral-7b</td></tr><tr><td>底座来源</td><td>名称即表明它是<b>基于 Mistral-7B</b>的 dolphin 系列再微调版——其底座能力可参考本页第 03 节 Mistral 7B（73 亿参数、GQA+SWA、理论 131K 上下文、Apache 2.0）。</td></tr><tr><td>笔记关注点</td><td>原笔记只提了一句「擅长的能力」，未展开；具体擅长领域无原文可引。</td></tr><tr><td>建议</td><td>如需该模型的能力清单，应回到提问当时补一次实测，再按「底座 + 微调方向」补全卡片，不要套用 Mistral 7B 的分数冒充 dolphin 自身成绩。</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>口径声明</b>：本页严格照录源笔记。dolphin 卡片中没有任何数字来自凭空补写——凡原笔记缺失处，均以上表「可确认信息」的边界为准。</div></div></div>
