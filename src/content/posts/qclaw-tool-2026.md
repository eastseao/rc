---
title: "QClaw 功能与使用"
description: "QClaw 微信直连与远程操控工具：功能介绍、任务方向、文件存 E 盘方法与积分充值规则。"
pubDatetime: 2026-05-15
category: "AI与Agent"
kind: "工具"
tags: ["QClaw", "微信直连", "远程操控", "Skill 技能", "积分充值"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00784-2026-03-23 QClaw功能介绍00799-2026-03-24 QClaw任务询问00892-2026-04-10 QClaw文件存E盘方法01151-2026-05-15 QCLAW积分充值支持

## 01 · QClaw 是什么与核心能力（00784）

QClaw 是腾讯推出的本地 AI 智能体，你可以把它想象成电脑里的「数字员工」：**无需守在电脑前，在微信里下达指令，它就会自动执行**。配置时推荐选择 Kimi、DeepSeek 等大模型，任务执行会更聪明。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">远程操控电脑（核心能力）</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>文件整理</dt><dd>把桌面录屏文件整理进文件夹、整理发票目录。</dd><dt>信息处理</dt><dd>搜索 AI 科技新闻、总结文档、生成分析报告。</dd><dt>日程管理</dt><dd>帮你写文档、订日程、安排会议和待办。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">打通应用与扩展技能</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>多平台远控</dt><dd>除微信外，还支持 QQ、企业微信、飞书、钉钉等入口。</dd><dt>Skill 技能扩展</dt><dd>官方 SkillHub 已聚合超<b>1.3 万</b>个安全技能，覆盖文案润色、代码生成等场景。</dd></dl></div></div>

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:14px"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">特色交互与玩法</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.7"><li><b>像素工作室</b>：AI 化身一个像素风「打工人」，让你直观看到它的工作状态。</li><li><b>可视化定时任务</b>：在界面集中管理，设置新闻推送、喝水提醒等周期性任务。</li></ul></div><div><h4>注意事项 · 能力边界</h4><div>目前不能订酒店/机票，也无法自动发红包或读聊天记录</div><p>涉及支付安全的操作暂不支持，请勿相信网上相关谣言。需要特定功能（如小红书运营）时，去官方 SkillHub 安装对应技能即可。</p></div></div>

## 02 · 可以下达哪些任务（00799）

这篇早期笔记记录了对「QClaw 可以下达哪些任务」的一次梳理。由于当时 QClaw 这个名称还不常见，回答先按「Claw（爪）」这一意象推测了四类常见任务方向，再请用户补充背景以便给出更具体的清单。

| 任务方向 | 典型任务内容 |
|---|---|
| **数据抓取与采集** | 若它是爬虫或数据工具，任务可能包括抓取网页内容、提取结构化数据、监控网站更新，或下载特定格式的文件。 |
| **文件与资源管理** | 若涉及系统运维，可能包括批量文件整理、归档压缩、日志清理，或按规则自动删除过期文件。 |
| **系统监控与响应** | 作为监控脚本，它可以执行端口探测、服务状态检查、异常告警，或在检测到特定条件时自动执行修复操作。 |
| **网络与安全** | 在安全测试场景下，可能用于子域名收集、目录爆破、漏洞验证，或流量分析。 |

实际使用时，结合第 01 节的核心能力——文件整理、信息处理、日程管理、多平台远控与 Skill 扩展——即可按自己的场景下达指令；提供更具体的平台与使用背景，能梳理出更精准的可用任务清单。

## 03 · 生成文件改存 E 盘的四种方法（00892）

QClaw 生成的文件完全可以保存在 E 盘，甚至可以把整个程序都安装在 E 盘，以此避免占用宝贵的 C 盘空间。下面四种方法按推荐程度排列。

<details open><summary>方法一：安装时设置（最推荐）<span>图形化</span></summary><div><p>在软件安装过程中，系统会询问安装位置（默认 C 盘）。此时点击「浏览」按钮，将路径直接改为<code>E:\QClaw</code>或其他你喜欢的 E 盘文件夹即可。</p></div></details>

<details><summary>方法二：修改配置文件（永久设置）<span>config.yaml</span></summary><div><p>如果软件已经装好，可以通过修改配置文件来更改默认工作目录。QClaw 的主配置文件<code>config.yaml</code>通常位于<code>%APPDATA%\QClaw\</code>目录下：</p><ul><li>用记事本等文本编辑器打开<code>config.yaml</code>。</li><li>找到<code>base_dir:</code>这一行。</li><li>将其值修改为 E 盘下的目标路径，例如<code>base_dir: &quot;E:\MyQClawWorkspace&quot;</code>。</li><li>保存文件并重启 QClaw，设置即可生效。</li></ul></div></details>

<details><summary>方法三：使用命令行启动（临时生效）<span>-w 参数</span></summary><div><p>如果只是临时用一次，按<code>Win + R</code>打开「运行」窗口，输入<code>cmd</code>回车打开命令提示符，然后用以下命令启动 QClaw，本次会话生成的所有文件都会保存在指定的临时文件夹中：</p><pre>qclaw.exe -w E:\MyTempWorkspace</pre></div></details>

<details><summary>方法四：创建符号链接（高级操作）<span>mklink</span></summary><div><p>如果你已有固定文件夹结构不想改动，但又希望文件实际存储在 E 盘，可以使用「符号链接」。先确保 QClaw 没有运行，在 E 盘创建新文件夹（如<code>E:\QClawData</code>），把默认工作目录（如<code>C:\Program Files\QClaw\workspace</code>）重命名为<code>workspace_old</code>备份，再以管理员身份打开命令提示符执行：</p><pre>mklink /D &quot;C:\Program Files\QClaw\workspace&quot; &quot;E:\QClawData&quot;</pre><p>执行后，QClaw 会认为文件仍在 C 盘，但实际上所有数据都会写入到 E 盘的<code>QClawData</code>文件夹中。</p></div></details>

> **几个小建议**
> - **路径中避免使用中文**：新建文件夹路径建议只包含英文和数字，防止出现意外问题。
> - **注意读写权限**：确保为 QClaw 指定的 E 盘文件夹拥有读写权限。
> - **遇到路径问题**：使用中提示文件路径错误时，可在指令中明确文件的绝对路径，例如`E:\文档\报告.docx`。
> - **查看实时路径**：运行`qclaw --debug-path`，可实时查看程序解析的路径，帮助排查问题。

## 04 · 每日积分与充值机制（01151）

QCLAW 积分用完后**是支持充值的**，不过更建议先了解它每天都会赠送的免费积分——其核心策略是鼓励用户利用好每日赠送的额度。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">每日免费积分</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>每日赠送</dt><dd>目前采用每日刷新制，<b>每天赠送 800 积分</b>；当天没用完的积分不会累积，会在次日刷新重置。</dd><dt>消耗机制</dt><dd>不同的任务和使用的模型，消耗的积分额度也不一样；在客户端「设置」页面可随时查看用量统计。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">积分充值</h3><p style="font-size:13.5px;color:inherit;line-height:1.7;margin-bottom:10px">积分用完后需要充值，具体的充值方式和价格请参考官网的定价页面——这是最准确的官方信息来源。如果感觉赠送的 800 积分不够用，也可以通过官网的充值渠道继续使用服务。</p><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>口径说明</b>：每日 800 积分为笔记记录时的免费额度策略，官方可能调整，以官网与客户端「设置」页为准。</div></div></div>
