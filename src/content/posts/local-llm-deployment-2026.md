---
title: "本地大模型部署 · 聊天 · 搜索实现"
description: "普通电脑本地模型推荐、RAG 与微调取舍、搜索实现、两套硬件配置清单与 Ollama 接入。"
pubDatetime: 2026-04-27
category: "AI与Agent"
kind: "手册"
tags: ["本地模型推荐", "RAG/微调", "Ollama", "硬件配置清单", "Hermes 接入"]
---

> **本手册合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00724-2026-03-14 普通电脑本地模型推荐00791-2026-03-24 本地大模型聊天知识提升00793-2026-03-24 本地模型搜索实现方式01030-2026-04-27 本地部署大模型配置建议00955-2026-04-17 Hermes 接入本地 Qwen 模型

## 01 · 普通电脑能跑哪些本地模型（00724 · 2026-03-14）

得益于量化技术，许多大模型压缩后在**8GB–16GB**内存的电脑上就能跑得不错。下表是主流推荐与量化后内存需求（照录）。

| 模型 | 参数 | 内存需求（量化后） | 特点与适用场景 |
|---|---|---|---|
| **Llama 3.1** | 8B | 约 7.2–8 GB | Meta 通用型，对话、写代码、总结文档全面。 |
| **Qwen2.5（通义千问）** | 7B | 约 6–7.5 GB | 阿里出品，中文出色、支持长文本，适合中文内容。 |
| **DeepSeek R1** | 7B/8B | 约 6.7–7.3 GB | 擅长逻辑推理与代码理解，思维过程透明。 |
| **Gemma 2** | 2B/4B/7B | 4B 约 4GB；7B 约 6–8GB | Google 轻量高效，4B 对低配友好，7B 能力更强。 |
| **Mistral 7B** | 7B | 约 6.9–7.6 GB | 速度快、效率高，适合实时聊天机器人。 |
| **Phi-3 Mini** | 3.8B | 约 4–7.5 GB | 微软小参数强逻辑与编程，性价比高。 |
| **Granite** | 3B/4B | 约 3–5 GB | IBM 最小语言模型，速度快、资源有限设备。 |
| **DeepSeek Coder V2** | 6.7B | 约 6 GB | 专为代码生成与理解优化，本地编程辅助。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">常用部署「启动器」</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>Ollama</dt><dd>操作最简单，命令行一键安装运行，对新手友好。</dd><dt>LM Studio</dt><dd>漂亮图形界面，像普通软件一样安装，内置模型搜索下载。</dd><dt>Llama.cpp</dt><dd>性能核心，专注普通硬件（甚至树莓派）高效运行，许多工具基于它。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">8GB 内存的取舍</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>选量化版</dt><dd>文件名带<code>Q4_K_M.gguf</code>即 4-bit 量化，是性能与占用的最佳平衡；建议为模型预留约 1.2 倍内存。</dd><dt>8GB 首选</dt><dd>Gemma 2:4B（首选）、Phi-3 Mini（备选）；写中文可试 Qwen2.5:7B 的 Q3 量化版。</dd><dt>16GB 可选</dt><dd>可流畅跑 Llama 3.1 或 Qwen2.5。</dd></dl></div></div>

| 维度 | 在线版 AI | 本地语言模型 |
|---|---|---|
| **硬件依赖** | 无需配置，有浏览器即可 | 完全依赖本机；8GB 内存只能跑 3B–9B 小模型 |
| **模型能力** | 极强，可用最新最大模型 | 相对较弱，受硬件限制 |
| **隐私安全** | 数据上传服务器，有泄露/被用于训练风险 | 完全离线、数据不出电脑，最适合敏感信息 |
| **成本** | 基础免费、高级付费 | 完全免费、无限次使用 |

笔记建议的混合用法：**日常、隐私、草稿**用本地模型快速记录与初润；**定稿、创意、难题**把草稿交给在线版优化标题、文采与结构。

## 02 · 和本地模型聊天，能让它变聪明吗（00791 · 2026-03-24）

结论先行：**单纯聊天无法永久提升本地大模型的知识或能力。**差别在模型是怎么跑起来的。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">静态模型（Ollama / LM Studio / llama.cpp）</h3><p style="font-size:13.5px;color:inherit">部署后<b>权重是冻结</b>的：每次聊天只基于训练时数据推理，对话历史只活在当前会话的上下文窗口里；关窗即「失忆」，不会因为聊得久就变聪明。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">带「长期记忆」的实验架构</h3><p style="font-size:13.5px;color:inherit">如 MemGPT、LangChain 记忆模块，会把对话总结存进向量数据库，下次聊天能检索到历史作参考——<b>但权重参数依然没变</b>，只是「伪装成记忆」。</p></div></div>

> **真正「提升」知识的两条路**
> - **检索增强生成（RAG）**：把文档喂给它，回答时「查书」——目前本地模型获取新知识的主流方式。
> - **微调（Fine-tuning）**：用新数据训练、修改权重，需要较高显存与技术门槛，已不是「聊天」。

## 03 · 本地模型如何实现「在线搜索」（00793 · 2026-03-24）

**本地模型本身不具备在线搜索能力**——它只是一个静态本地文件、语言生成器。要搜索，得由前端/中间层先调搜索 API，再把结果连同问题喂给模型。

| 实现方式 | 做法 |
|---|---|
| **支持联网的客户端** | Open WebUI、AnythingLLM、ChatGPT-Next-Web 等可配置搜索引擎 API（Google/Bing/SearchAPI）：模型需要搜索时，工具先取搜索结果，再连同问题发给模型作答。主流组合即**Open WebUI + 本地模型（如 Ollama）+ 搜索引擎 API**。 |
| **自己写脚本** | 用 Python 等先调搜索 API，把结果拼接后再调本地模型 API 接口回答。 |
| **云平台「本地部署」模型** | 有些 API 服务虽称「本地」，实际跑在云端，是否内置搜索插件取决于平台。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>附 · LM Studio 与图片</span><h3>LM Studio 能不能装图片生成模型</h3></div><div style="padding:14px 16px"><p>结论：<b>不能直接「安装/运行」图片生成模型（如 Stable Diffusion）</b>，它是专门跑大语言模型（LLM）的工具。但它能做两件和「图」相关的事。</p><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:180px">功能</th><th style="width:120px">能否</th><th>说明</th></tr></thead><tbody><tr><td>直接生成图片</td><td>不能</td><td>本身不是为图像生成设计的。</td></tr><tr><td>运行图像理解模型（VLM）</td><td>能</td><td>支持 VLM 读取并理解图片，官方示例 qwen2-vl-2b-instruct、gemma-3-*、pixtral-* 等，可上传图片提问。</td></tr><tr><td>辅助图片生成</td><td>能</td><td>当「提示词工程师」把想法扩成详细 Prompt 再交给绘图工具；或经 Gemini MCP Server 等插件、或作为节点接入 ComfyUI 工作流。</td></tr></tbody></table></div></div></div>

## 04 · 2万~3万元预算硬件配置清单（01030 · 2026-04-27）

核心思路：优先保障**大显存显卡**。笔记给了两套方案——单卡约 2.2 万跑 7B–14B，双卡约 3.0 万挑战 70B+ 量化模型。CPU 与主板决定你能插几块卡。以下总价均为**不含显示器**的参考估算。

| 方案 | 显卡 GPU | CPU | 内存 RAM | 硬盘 SSD | 参考总价 |
|---|---|---|---|---|---|
| **方案一<br>** | **1 × RTX 4090 24GB**（~¥17,000） | Intel i7-13700K（~¥2,500） | 64GB DDR5（~¥1,500） | 1TB NVMe（~¥500）+ 4TB HDD（~¥600） | **≈ ¥2.2 万** |
| **方案二<br>** | **2 × RTX 3090 24GB**（二手，~¥11,000） | AMD Ryzen 9 7950X（~¥3,500） | 64GB DDR5（~¥1,500） | 1TB NVMe（~¥500）+ 4TB HDD（~¥600） | **≈ ¥3.0 万** |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">方案一 · 单卡旗舰（≈¥2.2 万）</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>主板</dt><dd>Z790 芯片组（~¥2,000），ATX、一线品牌主流型号，重点供电与散热片。</dd><dt>内存</dt><dd>64GB（32GB×2）DDR5 6000MHz，确保加载运行稳定、留余量。</dd><dt>电源</dt><dd>1000W 金牌全模组（~¥1,200）——4090 峰值功耗高。</dd><dt>散热机箱</dt><dd>360mm 一体水冷 + 中塔机箱（~¥1,200），压 i7-13700K。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">方案二 · 双卡探索（≈¥3.0 万）</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>主板</dt><dd>X670E（~¥2,500），双 PCIe 5.0 x16，两张 3090 满速。</dd><dt>关键提醒</dt><dd>二手 3090 务必辨别矿卡/高强度卡；双卡发热大，选全塔机箱并装满风扇。</dd><dt>电源</dt><dd>1500W+ 金牌全模组（~¥2,500）——双卡+旗舰 CPU 满载功耗高。</dd><dt>散热</dt><dd>强烈建议 360 水冷压 7950X。</dd></dl></div></div>

> **为什么旧 3090 可能比新 4090 更有用**：部署大模型，**显存容量**是决定能跑多大模型的第一要素。一个 70B 模型即使压缩也约需**35–40GB**显存；4090 24GB 只能把部分任务甩给 CPU 而速度骤降，两张 3090 组成 48GB 显存池则刚好装下。

#### 这套硬件能跑哪些模型（照录）

| 模型 | 参数规模 | 推荐量化 | 显存需求 | 推荐方案 | 预估速度 |
|---|---|---|---|---|---|
| **Qwen3.5-9B** | 9B | Q4_K_M (4-bit) | ~6 GB | 方案一/二 | 极快（>50 t/s） |
| **DeepSeek-R1-Distill-Qwen-14B** | 14B | Q4_K_M (4-bit) | ~10 GB | 方案一/二 | 快（>30 t/s） |
| **Qwen3.5-35B-A3B** | 35B（MoE，激活 3B） | Q4_K_M (4-bit) | ~20 GB | 方案一/二 | 极快（约 196 t/s） |
| **DeepSeek-V4（量化版）** | 671B（MoE，激活 37B） | 量化版 | ~24 GB+ | 方案一 | 中等（~15 t/s） |
| **Qwen2.5-72B** | 72B | GPTQ-Int4 (4-bit) | ~35–40 GB | 方案二 | 中等（~15–20 t/s） |
| **Llama-4（量化版）** | 1090B（MoE，激活 17B） | 4-bit | ~60 GB | 预算上限 | — |

上手工具：**Ollama + Open WebUI**（新手一条命令下载、浏览器聊天）；**vLLM**（多并发 API 后端）；**llama.cpp**（进阶、CPU/GPU 混合）；**Unsloth**（微调降显存）。系统推荐 Ubuntu 22.04 LTS，装最新 NVIDIA 驱动、CUDA、cuDNN。

> **口径提醒**
> - 推理速度受量化方法、上下文长度、后端框架影响，表中数值为社区公开数据的数量级参考。
> - 硬件价格波动频繁，RTX 4090 近期从 1.2 万左右涨至 1.7 万甚至更高，选购时关注行情。

## 05 · Hermes 接入本地 Qwen 7B（00955 · 2026-04-17）

核心：Hermes 支持**OpenAI 兼容接口**，只要模型提供符合格式的 API 地址就能无缝调用。下面是最省事的 Ollama 路径与配置文件路径。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方法一 · Ollama（新手首选）</span><h3>先跑模型，再配 Hermes</h3></div><div style="padding:14px 16px"><p style="margin-bottom:8px">第一步：确认 Qwen 已在本地经 Ollama 运行——</p><div style="margin:14px 0"><span># 1. 拉取模型</span>ollama pull qwen2:7b<span># 2. 启动服务</span>ollama serve<span># 3. 另开终端验证状态，确认 qwen2:7b 为 loaded</span>ollama list<span># 也可访问 http://localhost:11434 确认服务就绪</span></div><p style="margin-bottom:8px">第二步：终端输入<code>hermes model</code>进入配置向导——Provider 选<code>custom</code>（<b>不要选</b><code>ollama</code>，旧版 Hermes 对原生 Ollama 接口支持不佳），按下表填写：</p><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">字段</th><th>填写值</th></tr></thead><tbody><tr><td>Base URL</td><td><code>http://localhost:11434/v1</code></td></tr><tr><td>Model Name</td><td>Ollama 中的确切模型名，如<code>qwen2:7b</code></td></tr><tr><td>API Key</td><td>任意非空字符，如<code>ollama</code>（Hermes 会校验，Ollama 会忽略其值）</td></tr></tbody></table></div><p style="font-size:13.5px;color:inherit">配置完成后执行<code>hermes</code>即可与本地 Qwen 7B 对话。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方法二 · 配置文件</span><h3>~/.hermes/config.yaml 手动接入</h3></div><div style="padding:14px 16px"><p style="margin-bottom:8px">用<code>hermes config edit</code>打开配置文件，添加如下内容：</p><div style="margin:14px 0"><span># ~/.hermes/config.yaml</span>llm: provider: custom model: &quot;qwen2:7b&quot;<span># 你使用的模型名称</span>base_url: &quot;http://localhost:11434/v1&quot;<span># 本地推理服务地址</span>api_key: &quot;ollama&quot;<span># 任意非空值即可</span><span># 遇 JSON 解析错误可尝试启用兼容模式</span><span># ollama_compatible: true</span><span># 多模型共存示例</span><span># providers:</span><span># qwen_ollama:</span><span># provider: custom</span><span># base_url: &quot;http://localhost:11434/v1&quot;</span><span># api_key: &quot;ollama&quot;</span><span># qwen_vllm:</span><span># provider: custom</span><span># base_url: &quot;http://localhost:8000/v1&quot;</span><span># api_key: &quot;EMPTY&quot;</span></div><p style="margin-bottom:10px">多模型时在<code>providers</code>下定义多个服务，再用<code>provider名/模型名</code>选默认模型。进阶：vLLM 追求高性能生产部署，启动时需加<code>--enable-auto-tool-choice</code>与<code>--tool-call-parser hermes</code>才支持 Qwen 工具调用；用阿里云 DashScope 则在向导选<b>Qwen OAuth</b>。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>排障</span><h3>三个常见问题</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:190px">现象</th><th>原因与解决</th></tr></thead><tbody><tr><td>模型不支持最小上下文报错</td><td>部分低量化 Qwen 上下文窗口小；换上下文更大的模型，如<code>qwen2.5:7b</code>或<code>gemma4:e2b</code>。</td></tr><tr><td>连接失败 / Connection refused</td><td>本地推理服务未启动或 base_url 配错；Ollama 地址通常是<code>http://localhost:11434/v1</code>。</td></tr><tr><td>API Key 无效 / 401 Unauthorized</td><td>Hermes 必须有 API Key 但 Ollama 忽略其值；填任意非空串如<code>ollama</code>或<code>dummy</code>。</td></tr></tbody></table></div><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr));margin-top:14px"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>Ollama</dt><dd>部署最简、配置最快、资源占用低，适合个人/新手/快速原型。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>vLLM</dt><dd>推理性能高、支持高并发，适合生产部署。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>DashScope</dt><dd>无需本地硬件，直接调官方最强模型。</dd></dl></div></div></div></div>
