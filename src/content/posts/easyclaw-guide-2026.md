---
title: "EasyClaw 安装与积分体系"
description: "EasyClaw 图形界面与命令行两种安装方式、国内版本说明，以及积分与 token 兑换关系。"
pubDatetime: 2026-04-27
category: "AI与Agent"
kind: "手册"
tags: ["EasyClaw", "图形界面安装", "命令行安装", "积分兑换", "token 计费"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：01037-2026-04-27 EasyClaw AI 安装指南01038-2026-04-27 EasyClaw积分与token兑换关系

## 01 · 两种安装方式与国内版本（01037）

EasyClaw 的安装主要有图形界面与命令行两种方式，国内用户还可选用零门槛专属版本；基础安装完成后，可通过「技能商店」扩展功能。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>推荐新手</span><h3>方式一：图形界面安装</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>下载</dt><dd>访问官网<code>https://www.easyclaw.app/</code>，按操作系统（Windows、macOS 或 Linux）下载对应安装包。</dd><dt>运行</dt><dd>双击运行安装包，程序自动检测系统环境并引导完成安装。</dd><dt>配置密钥</dt><dd>启动应用后，按提示输入所选 AI 模型（如 OpenAI、Anthropic）的 API 密钥。</dd></dl><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:14px;margin-bottom:0"><b>Windows 备用</b>：遇到环境问题可访问备用安装指南；该版本还支持 DeepSeek、Qwen 等模型，并提供免 API 密钥的 Gemini 访问选项。</div></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>适合开发者</span><h3>方式二：命令行安装</h3></div><div style="padding:14px 16px"><p>更习惯终端、或需要在服务器上部署时，命令行效率更高。在 macOS 或 Linux 终端粘贴并运行以下脚本，它会自动完成环境检测、依赖安装和配置流程：</p><pre>curl -fsSL https://openclaw.ai/install.sh | bash</pre><p style="font-size:13.5px;color:inherit;line-height:1.7">该命令来源于 EasyClaw 官方，适用于 macOS 和 Linux；Windows 用户请走备用安装指南。运行后留意终端提示完成后续配置。</p></div></div></div>

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:14px"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">国内用户专属版本（零门槛）</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.7"><li>访问<code>https://easyclaw.cn/</code>下载专属安装程序。</li><li>双击运行，安装程序自动完成所有配置。</li><li>已内置国内主流 AI 模型支持，<b>无需自行申请和配置 API Key</b>，开箱即用。</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">进阶：安装「社区技能包」</h3><p style="font-size:13.5px;color:inherit;line-height:1.7;margin-bottom:10px">打开客户端，点击左侧「技能商店」，搜索需要的技能，再点「安装」等待完成即可。</p><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:0"><h5>安全提示</h5><ul><li>安装前提防恶意插件，优先选择带「官方认证」标签的插件包。</li></ul></div></div></div>

| 安装前环境 | 要求 |
|---|---|
| **操作系统** | 支持 macOS、Windows、Linux；建议 Windows 10/11 或较新版本的 macOS/Linux。 |
| **硬件要求** | 无特殊配置，能流畅运行主流操作系统即可；本地运行 AI 模型（如 LLaMA）会占用更多内存和显存。 |
| **软件依赖** | **无需手动安装**Python 或 Docker 等环境。 |
| **其他依赖** | API 密钥等所有配置均在安装程序中自动引导，无需额外准备。 |

## 02 · 积分与 token 的兑换关系（01038）

关于 EasyClaw 的积分和 token 比例，**目前没有一个公开固定的兑换率，不是一个常数**。1 积分对应的实际 token 数量会根据多种因素动态调整。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>计费逻辑</span><h3>积分价值如何判定</h3></div><div style="padding:14px 16px"><p>EasyClaw 采用基于<b>实际 token 调用量</b>的计费模式，并通过「积分」体系计量。积分的核心价值并非与 token<b>数量</b>直接固定挂钩，而是与 token 在<b>不同模型</b>下的<b>实际货币成本</b>相关联。官方协议也强调：「积分由系统根据用户实际使用 AI 功能时消耗的 Token 量及<b>模型类型</b>自动换算抵扣」。</p><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>使用高级模型</dt><dd>调用 GPT-5.2、Claude 这类更强大的大模型，通常消耗更多积分来「购买」同等数量的 token。</dd><dt>执行复杂任务</dt><dd>指令越复杂、任务越长期，对话历史越长，消耗的 token 总数越高，所需积分也就越多。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">三大影响因素</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.7"><li><b>对话长度</b>：任务越复杂、轮次越多，token 消耗越多。</li><li><b>上下文长度</b>：AI 能「记住」的信息量，长文档/长对话消耗更多。</li><li><b>生成内容长度</b>：生成报告、代码或长文时，输出 token 消耗也很大。</li></ul></div></div></div></div>

| 参考标尺 | 数值 | 说明 |
|---|---|---|
| **EasyClaw 免费版** | 每日赠送**200 积分** | 最直观的标尺，可直接体验 200 积分能完成怎样的任务量。 |
| QClaw（同行对比） | 每日免费 4000 万 token | 来自第三方评测，仅供参考，非官方准确值。 |
| 悟空 Wukong（同行对比） | 每日免费约 500 万 token | 同上，用于建立数量级概念。 |

结合以上信息大致估算：对于普通或中等强度的模型，**1 积分大致可能对应相当于数万 token 的调用成本**。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:14px"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">个人版：按量「日用」</h3><p style="font-size:13.5px;color:inherit;line-height:1.7">更像一个「日用」工具，每天 200 积分是上限，用完即止；每次任务的实际消耗建议在使用中留意系统反馈。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">企业版：按需采购</h3><p style="font-size:13.5px;color:inherit;line-height:1.7">积分是充值后获得的一种「虚拟信用额度」，用于灵活管理和分配团队成本。最精确的实时兑换率，请以产品内的充值或使用页面公示为准。</p></div></div>
