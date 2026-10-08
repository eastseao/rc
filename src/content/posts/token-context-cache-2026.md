---
title: "Token 估算 · 上下文长度 · 缓存命中"
description: "汉字与 token 换算、百万 tokens 定价、168K/1M 上下文对照、KV 缓存命中与 TTFT 解析。"
pubDatetime: 2026-06-07
category: "AI与Agent"
kind: "长文"
tags: ["token 换算", "百万 tokens 定价", "168K/1M 上下文", "KV 缓存", "TTFT"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00629-2026-03-02 一千汉字 token 数量估算00640-2026-03-03 模型上下文长度介绍00660-2026-03-07 Token 成本构成解析01052-2026-04-27 AI 缓存命中未命中解释01117-2026-05-08 模型参数上下文解答01278-2026-06-07 AI 上下文 168K 含义解释

## 01 · 一个汉字折多少 token（00629）

token 是文本处理的基本单位，中文按字、词或子词（如 BPE）切分。一篇一千个汉字的文章折多少 token，取决于分词算法——三种情况照录如下。

| 分词方式 | 一千个汉字对应的 token 数 |
|---|---|
| **基于字的模型** | 每个汉字约对应 1 个 token，1000 字 ≈**1000 个 token**。 |
| **基于词的模型** | 词语由多个字组成，token 数可能**少于 1000**。 |
| **子词分词（GPT 系列常用）** | 每个汉字通常对应 1–2 个 token，1000 汉字约**1200–1800 个 token**，常见估计为**1500 个左右**。 |

笔记结论：实际数值需通过具体 tokenizer 计算，上述范围可作参考。日常可按**平均约 1.5 token / 汉字**估算。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">百万 tokens 相当于多少中文书</h3><div>1,000,000 tokens ÷ 1.5 ≈ 666,667 汉字（约 66.7 万字）</div><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>参照</dt><dd>一部普通长篇小说约 20 万–30 万字，百万 tokens 相当于<b>2–3 本</b>这样的书；《平凡的世界》约 100 万字，百万 tokens 接近其体量。</dd><dt>极端情况</dt><dd>字级模型（1 汉字=1 token）：百万 tokens = 100 万字。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">计费直觉</h3><p style="font-size:13.5px;color:inherit;margin-bottom:10px">钱不是按提问次数算，而是按「让模型思考了多少字」算。tokens 像加油站的「升」——用多少油付多少钱。</p><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>百万 tokens 有多大</dt><dd>一篇 1000 字文章约 1500 tokens，一百万 tokens 约等于<b>670 篇文章</b>的体量。</dd></dl></div></div>

## 02 · Token 成本构成与三档定价（00629 / 00660）

笔记 00629 贴出一张价格表并逐档解释；笔记 00660 则从费用、系统资源、工程与机会四个角度拆解「token 的成本」。价格表与计算公式照录。

| 计费项 | 价格 | 含义 |
|---|---|---|
| 百万 tokens 输入（**缓存命中**） | **0.2 元** | 模型「记得」这段内容、不必重新计算，相当于打 1 折，最便宜。 |
| 百万 tokens 输入（**缓存未命中**） | **2 元** | 标准输入价：全新内容或模型已「忘记」，每次从头读。 |
| 百万 tokens**输出** | **3 元** | 模型「开口写答案」最贵——生成新内容（写作、推理）比读取更耗算力。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00629 · 2026-03-02</span><h3>一次请求的实际费用算例</h3></div><div style="padding:14px 16px"><p>场景：上传一份 5000 tokens 长文（约 3000–4000 汉字），提问「请帮我总结一下」算 20 tokens，模型写出 1000 tokens 总结；假设第一次提问、未命中缓存。</p><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:170px">费用项</th><th style="width:230px">算式</th><th>金额</th></tr></thead><tbody><tr><td>输入（未命中）</td><td>(5000 + 20) × (2 ÷ 1,000,000) = 5020 × 0.000002</td><td><b>0.01004 元</b></td></tr><tr><td>输出</td><td>1000 × (3 ÷ 1,000,000) = 1000 × 0.000003</td><td><b>0.003 元</b></td></tr><tr><td><b>合计</b></td><td>0.01004 + 0.003</td><td><b>≈ 0.013 元（约 1 分钱）</b></td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>一句话记住这张表</h5><ul><li>0.2 元：让 AI 用已有记忆回答（最划算）。</li><li>2 元：让 AI 阅读新内容并思考（标准输入价）。</li><li>3 元：让 AI 开口写答案（最贵，因为生成内容最费劲）。</li></ul></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00660 · 2026-03-07</span><h3>Token 成本的四个角度</h3></div><div style="padding:14px 16px"><div>总费用 = (输入 Token 单价 × 输入数量) + (输出 Token 单价 × 输出数量)</div><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:170px">成本角度</th><th>具体内容</th></tr></thead><tbody><tr><td><b>计算与计费成本</b></td><td>API 按单价 × token 数计，分输入/输出定价；处理 token 越多，响应越慢、延迟越高。</td></tr><tr><td><b>系统运行成本</b></td><td>算力成本（GPU/AI 芯片、推理计算密集且耗电）、显存成本（长文本中间结果存于高带宽显存）、带宽成本（传输大量 token 文本的网络流量）。</td></tr><tr><td><b>开发者技术成本</b></td><td>上下文窗口管理（为超长文本写文本分割、摘要或向量检索逻辑）；结果质量控制（输出上限设太短会导致回答被截断）。</td></tr><tr><td><b>机会成本</b></td><td>上下文容量有限，无关输入会挤占模型「记住」关键信息的能力；输入太长时模型对中间部分的注意力容易下降。</td></tr></tbody></table></div><p>笔记的一句话总结：<b>Token 的成本，本质上是处理信息所需的算力资源，最终体现为你要支付的金钱和模型处理时的性能负担。</b></p></div></div>

## 03 · 上下文长度：128K / 168K / 1M 各能装多少（00640 / 01117 / 01278）

上下文指模型在一次对话或处理中能「记住」并参考的文本总量（含提问、历史对话、上传文档）。三份笔记分别给了 DeepSeek 的 1M、通用的 168K 与 V4 的对照，照录如下。

| 口径 | token 数 | 换算成常见文本量 |
|---|---|---|
| **168K 上下文** | **168,000 个 token** | 英文约 13 万单词（约一本 300 多页的书）；中文约**8 万–10 万汉字**（如整本《三体》第一部）。 |
| **DeepSeek 1M** | **100 万 token** | 《三体》三部曲总字数约 90 万字，正好在处理范围内；笔记 01278 引官方估算约能一次性处理**75 万字**中文内容。 |
| **常见旧窗口** | 128K / 168K | 笔记 01278 指出，与 128K 或 168K 相比，100 万窗口意味着能力大幅提升。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">上下文长度的意义（01278 照录）</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.8"><li>长文本处理：一次读完一本长篇小说或多份报告，再回答细节。</li><li>多轮对话：很长的对话中不「忘记」早期内容。</li><li>复杂分析：对比多份法律合同、分析完整财报。</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">模型参数与上下文（01117 · 2026-05-08）</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>架构</dt><dd>混合专家（MoE），总参数量<b>671B（6710 亿）</b>，每个 token 激活参数约<b>37B（370 亿）</b>。</dd><dt>上下文</dt><dd>支持<b>1M tokens（100 万）</b>窗口。</dd><dt>一句概括</dt><dd>大量参数保能力，MoE 架构控成本，超长上下文便于处理复杂长篇任务。</dd></dl></div></div>

> **使用提醒（01278 照录）**：上下文长度只是能力之一，模型理解质量同样重要；「168K / 1M」是技术上限，实际过长输入会消耗更多计算资源、响应更慢。168K 是中高端模型常见配置，如 Claude 3 Sonnet、GPT-4 Turbo 等都有类似或更高窗口。

## 04 · 缓存命中与未命中：速度和价格的分水岭（01052）

把缓存想象成**临时便签本**，原始数据放在远处的**图书馆**（主存或磁盘）。需要的数据在便签本里就是命中，不在就是未命中。两种情况照录。

| 对比 | 缓存命中 | 缓存未命中 |
|---|---|---|
| **过程** | 数据已在缓存里，直接快速读取，不用去图书馆。 | 数据不在缓存里，只能去主存/磁盘（或重新计算）把数据搬回来，顺便存入缓存。 |
| **结果** | **非常快、省算力、省功耗**。 | **慢、消耗更多算力和功耗**（多一次数据移动或计算）。 |
| **推理例子** | 生成第 2 个字时，第 1 个字的 Key-Value 向量还在缓存里，直接复用。 | 处理第一个词时没有历史缓存，必须计算全部注意力——一次彻底的未命中。 |
| **硬件例子** | 再次打开微信，它立刻弹出（已在内存中）。 | 杀掉微信后台再打开，需重新从闪存加载。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">对推理速度的影响</h3><p style="font-size:13.5px;color:inherit">缓存命中率直接影响<b>首 token 延迟 TTFT</b>（Time To First Token）与每 token 生成时间。高命中率接近「无限长上下文」的流畅体验；低命中率意味着模型在「费力回忆」刚说过的话。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">对硬件利用率的影响</h3><p style="font-size:13.5px;color:inherit">未命中会让昂贵的高带宽显存（HBM）或 GPU 计算单元空转等数据，拉低每秒处理 token 数（吞吐量）。若模型 200GB 而显存只有 80GB，大量参数访问会频繁在显存与内存间交换、推理变慢。</p></div></div>

> **一句话（01052 照录）**：命中了 = 直接复用，省时省力；未命中 = 重新获取，耗时耗力。工程师花大量精力设计**KV 缓存**、**页缓存**，就是为了让命中尽可能多发生。这也正是第 02 节里「输入缓存命中 0.2 元 vs 未命中 2 元」两档价差的技术来源。
