---
title: "浏览器推荐·Windows 小工具·图标格式·杂项"
description: "电脑浏览器好用指数参考、Windows 本地小软件开发工具推荐、Windows 图标格式像素指南、窗口布局 Markdown 绘制、电脑死机翻出陈年精油与氮化镓快充原理。"
pubDatetime: 2026-06-12
category: "建站与技术"
kind: "长文"
tags: ["浏览器指数", "WinForms", ".ico", "氮化镓"]
---

> **本文合并自以下笔记**：00769-2026-03-20 电脑浏览器好用指数参考00253-2025-10-15 Windows 本地小软件开发工具推荐01299-2026-06-11 Windows 图标格式像素指南01302-2026-06-12 Windows 窗口布局 Markdown 绘制00117-2025-09-19 电脑死机翻出陈年精油00264-2025-10-17 氮化镓快充原理详解

## 01 · 主流电脑浏览器「好用指数」参考（00769 · 2026-03-20）

没有唯一标准答案，看你追求速度、隐私还是功能。下表照录原笔记整理的跑分与特点（跑分数值为原笔记引用的评测参考）。

| 浏览器 | 跑分 / 体型 | 核心优点 | 适合人群 |
|---|---|---|---|
| **Google Chrome** | 标杆 52.3 分；内存占用偏高 | 兼容性无敌、插件生态最丰富、同步成熟 | 追求稳妥、依赖插件、多设备切换 |
| **Microsoft Edge** | 43.1 分；体型近 1GB 偏臃肿 | Windows 集成度高、启动快、办公功能丰富、AI 突出 | 办公一族、阅读 PDF、轻薄本用户 |
| **Apple Safari** | 48.2 分；能耗极佳 | 苹果生态无缝衔接、隐私强、阅读模式好 | 苹果全家桶用户 |
| **Mozilla Firefox** | 36.2 分；体型精简 | 开源、隐私标杆、独立 Gecko 引擎、账号容器 | 重视隐私、老电脑、程序员 |
| **Brave** | 48.4 分；内置广告拦截 | 默认强力拦广告和追踪器、Chromium 内核快 | 讨厌广告、注重隐私 |
| **Opera** | 46.9 分；常规套壳 | 创新功能多（侧栏工具、免费 VPN、工作区、Aria） | 喜欢尝鲜、要集成小工具 |
| **Vivaldi** | 49.7 分；资源偏中上 | 高度可定制、标签组/分屏强，像「工作台」 | 浏览器重度用户、效率控 |
| **Arc / Zen** | Arc 44.7 / Zen 32.5；Arc 833MB 臃肿 | 激进 UI 创新，颠覆传统标签栏 | 追求新鲜和设计感的先锋用户 |

选法速记：极致兼容选 Chrome；办公与 Windows 深度选 Edge；苹果生态选 Safari；隐私反广告选 Brave / Firefox；老电脑内存紧选 Firefox / Edge；爱折腾效率选 Vivaldi。夸克 AI 浏览器走的是另一条路——背靠通义千问做「AI 超级框」（Alt+空格 唤起、PDF 对照翻译、学术搜索、搜题），短板是不支持插件生态、部分格式转换收费。

## 02 · Windows 本地小软件开发工具推荐（00253 · 2025-10-15）

想做日常可用的本地小软件，主流方案四条路线，原笔记推荐从 C# + WinForms 起步——最平衡，易学又实用。

| 方案 | 优点 | 上手难度 |
|---|---|---|
| **C# + WinForms / WPF**（最推荐） | 微软官方、与 Windows 完美集成、可视化设计器、控件库丰富、性能优秀 | ★★ 新手首选 |
| **Python + Tkinter / PyQt** | 学习曲线平缓、快速原型、第三方库丰富 | ★ 极易上手 |
| **Electron**（Web 技术栈） | 前端开发者友好、跨平台、界面美观 | ★★ |
| **Delphi / Lazarus** | 编译型语言性能极佳、快速开发、单文件分发 | ★★★ |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">新手路线</h3><p style="font-size:13.5px;color:inherit">第一阶段装 Visual Studio Community（免费）+ .NET Desktop Development 工作负载，拖拽式做 WinForms；第二阶段进阶 WPF——更现代的界面、更强的自定义和数据绑定。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">起步项目创意</h3><p style="font-size:13.5px;color:inherit">文件批量重命名工具、系统监控小部件、快捷笔记应用、自动化脚本运行器。注意：考虑 Win10/11 兼容性、是否需要管理员权限、打包时带上必要运行库。</p></div></div>

## 03 · Windows 图标格式像素指南 · 窗口布局绘制（01299 / 01302）

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01299 · 2026-06-11</span><h3>托盘 / 任务栏 / 窗口图标是什么格式、多少像素</h3></div><div style="padding:14px 16px"><p style="margin-bottom:10px">最推荐做法：准备一个把多尺寸打包在一起的<b>.ico</b>文件，Windows 根据显示位置和 DPI 自动选最合适尺寸渲染；256×256 大尺寸建议用 PNG 压缩存内部。</p><div style="overflow-x:auto;margin:16px 0;margin-bottom:12px"><table><thead><tr><th style="width:150px">位置 / 缩放</th><th>显示尺寸</th></tr></thead><tbody><tr><td><b>核心尺寸清单</b></td><td>16×16、24×24、32×32、48×48、256×256（另可补 20/40/64/128 应对高 DPI）</td></tr><tr><td><b>托盘（通知区域）</b></td><td>100% 缩放 16×16；125% 20×20；150% 24×24；200% 32×32</td></tr><tr><td><b>任务栏</b></td><td>100% 24×24；125% 30×30；150% 36×36；200% 48×48</td></tr><tr><td><b>标题栏 / 桌面 / 资源管理器</b></td><td>标题栏 16×16；桌面经典 32×32；资源管理器常用 48×48</td></tr></tbody></table></div><p style="font-size:13.5px;color:inherit">实践建议：图标用透明背景，明暗双主题各自适配；经典尺寸做像素级精细调整避免边缘模糊。UWP/WinUI 以 44×44 逻辑像素为基准生成 scale-100/125/150/200 变体；.exe 打包用含全部尺寸的 .ico，UWP 应用在 Package.appxmanifest 里指明图标路径。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01302 · 2026-06-12</span><h3>Markdown 画一个 Windows 应用窗口布局</h3></div><div style="padding:14px 16px"><p style="margin-bottom:10px">原笔记用 ASCII 画出典型窗口框架（照录）：标题栏 → 菜单栏 → 工具栏 → 客户区 → 状态栏。</p><pre>+------------------------------------------------------------+ | [记事本] - 无标题.txt [ - ] [ □ ] [ X ] | +------------------------------------------------------------+ | 文件(F) 编辑(E) 格式(O) 查看(V) 帮助(H) | +------------------------------------------------------------+ | [新建] [打开] [保存] [打印] [剪切] [复制] [粘贴] | +------------------------------------------------------------+ | | | | | 编辑区域 / 工作区 | | （文本、图形等内容） | | | | | | | +------------------------------------------------------------+ | 就绪 Windows (CRLF) UTF-8 | +------------------------------------------------------------+</pre><p style="font-size:13.5px;color:inherit">标题栏左上角为图标+名称+文档标题，右上角三个窗口按钮；菜单栏按主题分组下拉；工具栏是常用功能快捷按钮；客户区是实际工作区；状态栏显示状态、编码、进度。实际应用可能加侧边导航、搜索框、滚动条，但这套结构是绝大多数传统窗口的基础框架。</p></div></div>

## 04 · 陈年精油小记 · 氮化镓快充原理（00117 / 00264）

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00117 · 2025-09-19</span><h3>电脑死机，翻出十几年前的精油</h3></div><div style="padding:14px 16px"><p style="font-size:13.5px;color:inherit">一段润色小记：电脑突然「脑梗」，翻箱倒柜找祖传的特殊口螺丝刀没找着，反而挖出十几年前买的精油——一开盖，半瓶余香宛如时光胶囊，一点没挥发也没变质，仿佛在说「我还能再战十年」。这品质、这持久度，不研究一下精油市场都对不起这份跨越时空的香气惊喜。周末计划：左手拧螺丝，右手写报告，全方位解密精油界的「不老传奇」。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00264 · 2025-10-17</span><h3>氮化镓（GaN）快充为什么又小又快</h3></div><div style="padding:14px 16px"><p style="margin-bottom:10px">氮化镓快充不是「单纯增大功率」，而是材料革新 + 开关电源高频化 + 智能协议三者合力：传统硅充电器像普通省道（频率低、易发热堵车），氮化镓像新建高速。</p><div style="overflow-x:auto;margin:16px 0;margin-bottom:12px"><table><thead><tr><th style="width:150px">层面</th><th>原理</th></tr></thead><tbody><tr><td><b>材料革命</b></td><td>氮化镓禁带宽度约 3.4eV（硅约 1.1eV）：耐高压耐高温、电子迁移率高（开关快）、导通电阻低（损耗小发热低）。</td></tr><tr><td><b>高频化</b></td><td>核心公式：变压器体积 ∝ 1 / 频率。硅充电器频率几十 kHz，氮化镓轻松几百 kHz 甚至 MHz，变压器、电容、电感随之大幅缩小——这是充电器小巧的根本原因，转换效率通常 &gt;90%。</td></tr><tr><td><b>快充协议</b></td><td>充电器与手机通过数据引脚「对话」：手机问支持哪些电压电流档 → 充电器答（如 5V/3A、9V/3A、12V/3A、15V/3A、20V/3.25A）→ 手机按电量选档（如 9V/3A = 27W）→ 确认后进入快充。主流协议 USB PD 最高最通用，另有高通 QC、华为 SCP/FCP、OPPO VOOC 等私有协议。</td></tr></tbody></table></div><p style="font-size:13.5px;color:inherit">完整链路：氮化镓替代硅（高耐压、高开关速度、低损耗）→ 高开关频率让磁性元件小型化 → 快充协议动态调压调流，在安全前提下喂给设备最大可接受功率。</p></div></div>
