---
title: "屏保开发·电子书格式·PDF 模板"
description: "Python 梦幻水族箱屏保开发、Win11 屏幕程序扩展名、屏保制作推荐、书籍 PDF 模板设计、亚马逊电子书格式与电子书编辑软件。"
pubDatetime: 2026-05-30
category: "建站与技术"
kind: "长文"
tags: ["Pygame 屏保", ".scr", "ReportLab", "Kindle 格式", "电子书编辑"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：01000-2026-04-21 Python 梦幻水族箱屏保开发指南01001-2026-04-21 Win11 屏幕程序扩展名（含 .scr 路径与制作工具）01238-2026-05-29 屏保制作推荐指南（技术方案 + 创意主题）01243-2026-05-30 书籍 PDF 模板设计生成01026-2026-04-26 亚马逊电子书格式特点01157-2026-05-16 电子书编辑软件推荐

## 01 · Python 梦幻水族箱屏保开发（01000）

用 Python 做水族箱屏保，图形库首选**Pygame**（2D 动画/精灵/音效，学习曲线适中）；Tkinter 自带但复杂动画性能弱，PyOpenGL 适合 3D 但门槛高。

| 步骤 | 做法 |
|---|---|
| 装库与素材 | `pip install pygame`；同目录建 resources 放 background.png、fish1.png…、bubble.png、music.mp3。 |
| 初始化窗口 | pygame.init() 后建全屏窗口、隐藏鼠标光标。 |
| 加载资源 | pygame.image.load() 读图并缩放适配，mixer.music.load() 加载背景音乐。 |
| 鱼精灵类 | 随机位置/速度/方向；update() 移动并边缘反弹；帧计数切换图片列表实现鱼鳍摆动。 |
| 气泡特效 | 底部随机生成，垂直上移，到顶回底循环。 |
| 屏保退出 | 主循环监听 KEYDOWN / MOUSEBUTTONDOWN，一旦按键或点鼠标即 pygame.quit() 退出；mixer.music.play(-1) 循环配乐。 |
| 打包 | `pyinstaller --onefile --windowed name.py`，产物在 dist/。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01000 · 2026-04-21</span><h3>设为系统屏保 / 立即启动</h3></div><div style="padding:14px 16px"><p style="margin-bottom:8px">把打包好的 .exe 重命名为<b>.scr</b>，右键选「安装」即加入 Windows 屏保列表。代码立即调用系统屏保：</p><p>import ctypes ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF140, 0)</p><p style="margin-bottom:0">扩展思路：透明 Sprite Sheet 鱼图、角落动态数字时钟、随时间昼夜交替。</p></div></div>

## 02 · .scr 扩展名、路径与制作工具（01001 / 01238）

屏保本质是**全屏普通 exe，只是扩展名改成 .scr**，且必须支持`/s`（运行）、`/c`（设置）、`/p [句柄]`（预览）三个命令行参数。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">存放路径</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>System32</dt><dd>系统自带屏保大本营，新 .scr 放这里。</dd><dt>SysWOW64</dt><dd>64 位系统里放 32 位屏保。</dd><dt>注册表</dt><dd>当前屏保记在 HKCU\Control Panel\Desktop 的 SCRNSAVE.EXE。</dd><dt>安全</dt><dd>.scr 是可执行程序，勿装来源不明文件，勿删系统自带。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">技术栈选型</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>C++/Win32+D2D</dt><dd>最原生，GPU 渲染，高性能粒子/3D。</dd><dt>C#/WPF</dt><dd>开发快、现代动画、硬件加速。</dd><dt>C#/WinForms+GDI+</dt><dd>简单 2D 绘图、分形线条。</dd><dt>现成工具</dt><dd>Screensaver Factory/Wonder、Animated Screensaver Maker、SCR Builder 等。</dd></dl></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01238 · 2026-05-29</span><h3>C#/WPF 屏保骨架与创意主题库</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>骨架</dt><dd>Main 解析 /s 启动全屏、/c 弹设置；WindowStyle=None + Maximized + Topmost，隐藏 Cursor；遍历 Screen.AllScreens 多屏；MouseMove 超阈值或 KeyDown/MouseDown 即退出；CompositionTarget.Rendering 驱动动画。</dd><dt>经典复刻</dt><dd>3D 迷宫、3D 文字、管道 Pipes、飞行星空、花样曲线。</dd><dt>自然物理</dt><dd>下雪落叶、流体烟雾（纳维-斯托克斯）、雨滴车窗、海浪水面。</dd><dt>数学艺术</dt><dd>Mandelbrot/Julia 分形、生命游戏、流动粒子线、几何体旋转。</dd><dt>信息极简</dt><dd>极简时钟、系统监控仪表盘、音乐可视化、格言词云。</dd></dl></div></div>

## 03 · 书籍 PDF 模板设计（ReportLab）（01243）

用 Python ReportLab 做一本书模板：封面 + 书籍信息 + 卷首语 + 目录 + 正文 + 卷尾寄语，**两遍渲染**算总页码，自动找系统宋体/黑体支持中文。

| 组成 | 内容 |
|---|---|
| 封面 / 信息页 | 书名、作者 Gervas、装饰；书籍信息页含版本/ISBN 占位。 |
| 卷首语 / 寄语 | 卷首语按参考文件插入；卷尾寄语写给读者。 |
| 目录 / 正文 | 目录列章节页码；两章示例正文演示页眉右侧动态章节名。 |
| 页眉 | 左书名、右当前章节名。 |
| 页脚 | 左「第 X 页 / 共 Y 页」、右「作者 Gervas WX：EastSeaO」，浅灰色。 |

> **待补充建议**
> - 打印成册：左侧装订留边 0.5cm、奇偶页镜像边距。
> - 每章从奇数页（右页）开始；目录做内部超链接跳转。
> - 页眉下/页脚上加浅灰分隔线；正文 10–11pt，标题分层。
> - 加版权页（出版信息、ISBN 条码）；完整封面含封底与书脊。
> - 用 ReportLab TableOfContents 自动生成真实页码替换静态目录。

## 04 · 亚马逊 Kindle 格式与编辑软件（01026 / 01157）

Kindle 格式分官方原生（AZW/AZW3/KFX/AZW4）、可发送转换（EPUB/PDF/DOCX/TXT…）、已淘汰（MOBI/PRC/TPZ）三类；编辑软件按深度选型。

| 格式 | 类别 | 特点与现状 |
|---|---|---|
| **AZW3 (KF8)** | 主流原生 | 支持 HTML5/CSS3、自定义字体表格；目前最成熟通用。 |
| **KFX (KF10)** | 最新原生 | 连字符/增强版式、画质佳；新 Kindle 效果最佳，老设备支持有限。 |
| AZW / AZW4 | 旧/固定版式 | AZW 基于 MOBI 已淘汰；AZW4 基于 PDF 固定版式，教材漫画用。 |
| **EPUB** | 推荐通用 | 2022 起亚马逊支持推送，云端转 AZW3；多平台首选。 |
| PDF | 可发送 | 固定版式小屏需频繁缩放，体验一般。 |
| MOBI/PRC/TPZ | 已淘汰 | 2022 底起邮件不再接收 MOBI，改推 EPUB。 |

| 软件 | 格式/价格 | 定位 |
|---|---|---|
| **Sigil** | EPUB / 免费开源 | WYSIWYG + 直接改 XHTML/CSS，正则查找替换，深度定制 EPUB 首选。 |
| **Calibre** | 多格式 / 免费开源 | 管理+编辑+转换+阅读全能；内置编辑器实时预览，常用流程 LibreOffice 写稿→Calibre 精校。 |
| Kindle Create | Kindle / 免费 | 亚马逊出版专用，界面友好。 |
| FLBOOK / GroupDocs | 在线 / 免费或付费 | 模板库拖拽编辑；GroupDocs 轻量在线改 MOBI/AZW3。 |
| Ulysses / 纯纯写作 | macOS·iOS / Android | Ulysses 极简写作 iCloud 同步；纯纯写作绝不丢稿云同步。 |

选型：快速上手用在线工具；管大量书偶尔改格式用 Calibre；深度定制 EPUB 用 Sigil。
