---
title: "SVG 图标渲染与数据网址生成"
description: "SVG 宝箱图标渲染、矩形图标 SVG 数据网址（data URL）生成与 Emind 思维导图图标设计。"
pubDatetime: 2026-06-15
category: "建站与技术"
kind: "长文"
tags: ["SVG", "游戏图标", "data URL", "应用图标", "思维导图格式"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：01224-2026-05-27 SVG 宝箱图标渲染01277-2026-06-07 矩形图标 SVG 数据网址生成01304-2026-06-13 Emind 思维导图图标设计（含主流思维导图格式梳理）

## 01 · 游戏风宝箱图标的分层渲染（01224）

用户先给了一个扁平的宝箱 SVG（红箱体 + 深红上沿 + 金色竖条 + 顶部小三角）。AI 把它重写成 128×128、保留 64 视口的立体游戏图标：在原几何上叠加阴影、高光、锁孔，层次自下而上堆叠。

| 图层（自下而上） | 几何与配色 |
|---|---|
| 背景阴影 | rect 10,18 44×40 rx6，黑色 opacity 0.2，让图标浮起。 |
| 红色箱体 | rect 12,20 40×36 rx4，fill #e74c3c。 |
| 箱体高光 | rect 14,22 36×4 rx2，#ff5e4a opacity 0.4。 |
| 深红上沿 | rect 8,16 48×6 rx2，#c0392b。 |
| 金色中轴 | rect 28,20 8×36，#f39c12；叠 #fdd835 opacity 0.5 高光。 |
| 顶部皇冠 | polygon 32,8 40,16 32,12 24,16，#f1c40f；叠 #fff59d opacity 0.6 高光。 |
| 金属锁孔 | circle cx32 cy40 r3 + rect 31,40 2×6，#2c3e50，居中深色。 |

设计要点：红箱体为主、深色上沿压重、金色中轴提亮、顶部皇冠点题，中心加深色锁孔后更像「可解锁宝箱」。

## 02 · 线段几何到 SVG 数据网址（01277）

用户给出四条线段构成的矩形（左下角 -1,0、右上角 3,4）以及另一组 L 形线段，要「给出图标的网址」。做法是把 path 直接嵌进`data:image/svg+xml`，`<>#`等字符做 URL 编码，可直接粘进浏览器地址栏或 img src。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01277 · 2026-06-07</span><h3>两个侧边栏图标的数据网址</h3></div><div style="padding:14px 16px"><p style="margin-bottom:8px">第一个（矩形，代表展开侧边栏）：</p><p>data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='-2 -1 4 6'%3E%3Cpath d='M-1,0 L-1,4 M-1,0 L1,0 M-1,4 L1,4 M1,0 L1,4' stroke='black' fill='none' /%3E%3C/svg%3E</p><p style="margin-bottom:8px">第二个（L 形，代表收起侧边栏）：</p><p style="margin-bottom:0">data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='-8 -8 16 16'%3E%3Cpath d='M-7,-7 L7,-7 M7,-7 L7,7' stroke='black' fill='none' /%3E%3C/svg%3E</p></div></div>

> **编码要点**
> - `<`→%3C、`>`→%3E、`#`→%23；属性用单引号包裹避免转义双引号。
> - 按用户给的几何形状直接转换，不擅自改成 FontAwesome 风格；要标准图标库网址需另行说明。

## 03 · Emind 应用图标设计与思维导图格式（01304）

用户要做一款 Windows 桌面应用 Emind，用来读取思维导图文件，先设计 SVG 图标。AI 给了一套 512×512 深蓝渐变圆角方形、中心 E 标识、四周曲线连八个功能节点的方案；随后又梳理了 Windows 主流思维导图格式与 Typora 能否读取 mindmap。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01304 · 2026-06-13</span><h3>Emind 图标的结构拆解</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>背景</dt><dd>Win11 风圆角方形（rx100），深科技蓝渐变 #1e293b→#0f172a，外投 feDropShadow。</dd><dt>中心节点</dt><dd>200×200 rx40 方形，靛蓝→青绿渐变 #4f46e5→#06b6d4，内部三层网络线纹 + 白色「E」笔画。</dd><dt>连接线</dt><dd>八条贝塞尔曲线从中心连到八向，白色 0.15 透明度；交点处画发光数据圆点。</dd><dt>八个分支节点</dt><dd>上下左右 + 四角，青→蓝渐变方块，分别画 +（添加）、❤（收藏）、📁（文件）、🔗（链接）、💡（灵感）、⚙️（设置）、📄（文档）、👤（用户）白色小图标。</dd><dt>氛围点缀</dt><dd>一圈 #38bdf8 半透明小圆点，模拟神经元火花。</dd></dl></div></div>

| 软件 | 原生格式 | 定位 |
|---|---|---|
| **XMind** | .xmind | 主流标准，默认格式；也含 .xmap。 |
| **MindManager** | .mmap | 企业级标准（另有 .mapx/.mmat），XMind 可导入。 |
| **FreeMind** | .mm | 开源轻量标准，格式简单被广泛兼容。 |
| **亿图脑图** | .emmx | 国产新秀，XMind 支持导入。 |
| **WPS / 百度脑图** | 自有 / .km | 在线与办公集成。 |
| **iMindMap / Ayoa** | .imx | 手绘风格，Tony Buzan 公司出品。 |

几乎所有软件都支持导出 PNG、PDF、Word、Excel、Markdown、OPML 等通用格式供分享集成。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">Typora 能读 mindmap 吗</h3><p style="font-size:13.5px;color:inherit;margin-bottom:0">不能直接读 .xmind / .mmap 这类二进制源文件。变通：导图导出 Markdown（丢图形层级）、导出 PNG 嵌入（不可编辑）、或用 Typora 原生 Mermaid<code>mindmap</code>画文本导图。反向：Typora 大纲导出 OPML 再导入 XMind 生成导图。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">名词</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0;margin-bottom:0"><dt>英文</dt><dd>思维导图 = Mind Map（标准写法两个词，也写作 MindMap）。</dd></dl></div></div>
