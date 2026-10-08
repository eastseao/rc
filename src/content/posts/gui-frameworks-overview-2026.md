---
title: "GUI 框架与 Windows 应用框架概览"
description: "GUI 框架介绍、应用 GUI 框架概览、Windows 应用框架介绍与 Qt 框架，含 WinUI3/WPF 技术选型。"
pubDatetime: 2026-06-26
category: "建站与技术"
kind: "长文"
tags: ["GUI 框架", "WinUI3", "WPF", "Qt", "技术选型"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：01284-2026-06-09 GUI 框架介绍（按开发语言分类）01311-2026-06-16 应用 GUI 框架概览（跨平台 / 原生 / Web / 轻量四类 + Tauri 典型应用）01313-2026-06-16 Windows 应用框架介绍（含 WinUI 3 全方位介绍）01339-2026-06-26 Windows Qt 框架介绍

## 01 · GUI 框架全景：按语言与类别（01284 / 01311）

两份概览互为补充：01284 按**开发语言阵营**讲特点与适用，01311 按**跨平台 / 平台原生 / Web 技术 / 新兴轻量**四类列表并标注语言、平台与许可证。合并成一张总表。

| 框架 | 语言 | 平台 | 特点与定位 |
|---|---|---|---|
| **Qt** | C++ / Python | Win/mac/Linux/嵌入式 | 行业标准级跨平台框架，信号与槽、Designer 拖拽；WPS、VirtualBox 在用。LGPL/商业。 |
| **wxWidgets** | C++ | Win/mac/Linux | 用原生控件，外观与系统统一、包小；生态不如 Qt。 |
| **Dear ImGui** | C++ | 跨平台/游戏 | 即时模式，每帧直接绘制，集成极简；游戏调试面板、引擎编辑器。 |
| **Electron** | Node.js+前端 | Win/mac/Linux | 嵌 Chromium+Node，复用 Web 生态；包大（~150MB+）内存高。VS Code、Slack、Notion。 |
| **Tauri** | Rust+前端 | Win/mac/Linux | 系统 WebView，打包 <5MB、内存低、安全；Electron 现代替代品。 |
| **WPF / WinForms** | C# | 仅 Windows | WPF 基于 XAML、数据绑定强；WinForms 拖拽简单。VS 生态。 |
| **.NET MAUI** | C# | Win/mac/iOS/Android | 微软跨平台，Xamarin.Forms 演进版，XAML 布局。 |
| **PyQt / PySide** | Python | 跨平台 | Qt 官方绑定，专业界面；受 GIL 与调用开销影响不适合极致性能。 |
| **Tkinter** | Python | 跨平台 | 自带轻量、打包方便；控件少、界面老旧。 |
| **Flet / Streamlit** | Python | 桌面/Web | Flet 基于 Flutter；Streamlit 几行脚本变数据网页，适合 AI/数据演示。 |
| **egui / Iced** | Rust | 跨平台/wasm | egui 纯 Rust 即时模式；Iced 受 Elm 启发、声明式类型安全。 |
| **Flutter** | Dart | 全平台 | Skia/Impeller 自绘，UI 高度一致、Hot Reload；一套代码覆盖移动与桌面。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">怎么选（速查）</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>专业桌面软件</dt><dd>Qt（C++/Python）。</dd><dt>Web 转桌面快出产品</dt><dd>Electron / Tauri。</dd><dt>游戏引擎 / 调试工具</dt><dd>Dear ImGui（C++）/ egui（Rust）。</dd><dt>数据科学 / AI 界面</dt><dd>PyQt 或 Streamlit。</dd><dt>Windows 企业应用</dt><dd>WPF（C#）。</dd><dt>移动 + 桌面一套代码</dt><dd>Flutter。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">跨平台补充项（01311）</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>GTK</dt><dd>C，GNOME 生态核心，Adwaita 设计语言。</dd><dt>Avalonia UI</dt><dd>C#，类 WPF 的 XAML，自绘渲染，支持 MVVM。</dd><dt>Compose 多平台</dt><dd>Kotlin，JetBrains 维护，声明式 UI，Skia 渲染。</dd><dt>Slint</dt><dd>Rust/C++/JS，声明式极轻量，适合嵌入式。</dd><dt>Neutralinojs</dt><dd>系统 WebView，比 Electron 更轻的小工具壳。</dd></dl></div></div>

## 02 · Web 技术桌面壳与 Tauri 典型应用（01311）

01311 把基于 Web 技术的桌面框架单列，并追问「Tauri 有哪些典型应用」。结论：原本用 Electron 嫌体积大、吃内存的项目，新项目越来越多直接选 Tauri。

| 框架 | 渲染引擎 | 体积 | 特点 |
|---|---|---|---|
| **Electron** | Chromium | 大（~150MB+） | 生态最丰富，VSCode/Discord；内存占用高。 |
| **Tauri** | 系统 WebView | 极小（<5MB） | Rust 后端，安全、体积小、性能好，2.x 成熟。 |
| NW.js | Chromium | 较大 | Node 集成更直接，不如 Electron 流行。 |
| Neutralinojs | 系统 WebView | 极小 | 轻量替代品，适合小工具。 |

| Tauri 领域 | 代表应用 |
|---|---|
| 开发工具 | Lapce（Rust 编辑器，WASM 插件）、Spacedrive 文件管理器、HTTPie Desktop、Clash Verge Rev、DevToys Tauri 复刻版。 |
| 笔记知识 | 思源笔记（桌面端迁 Tauri）、Outline 桌面客户端、AppFlowy（部分场景用 Tauri 作壳）。 |
| 媒体创意 | Cider（第三方 Apple Music）、LosslessCut（部分版本）、Radiograph（3D 模型查看器）。 |
| 聊天社交 | ChatGPT 非官方桌面客户端、Ferdium（实验支持）、Spacebar（Discord 兼容客户端）。 |
| 系统效率 | EcoPaste 剪贴板、Pake（网页一键打包成桌面应用）、Bloop AI 代码搜索。 |
| 密码安全 | Padloc、Buttercup（桌面重写版迁移中）。 |

## 03 · Windows 应用框架与 WinUI 3（01313）

Windows 框架分微软官方原生与第三方/跨平台两类。微软目前主推**WinUI 3**（Build 2026 后正式定名「WinUI」），WPF/WinForms 维护旧项目与简单工具，MAUI 负责跨平台。

| 框架 | 年代/语言 | 定位与适用 |
|---|---|---|
| **WinUI 3** | 现代 / C#·C++ | 微软主推，Windows 应用 SDK + XAML + Fluent Design；新项目首选。 |
| **WPF** | 2006 / C# | .NET + XAML，生态成熟；维护大型企业应用。 |
| **WinForms** | 2002 / C# | 拖拽式，简单高效；快速内部工具。 |
| **UWP** | 2015 / C#·C++ | XAML 触控，面向 Win10/11/Xbox 多设备。 |
| **Win32/MFC/ATL** | 老牌 / C/C++ | 直接调底层 API，性能高但开发复杂。 |
| **.NET MAUI** | 2021 / C# | 跨 Windows/macOS/iOS/Android，代码复用。 |
| 第三方/跨平台 | — | Electron、Qt、React Native Desktop、Blazor Hybrid、Uno Platform、DuiLib。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01313 · 2026-06-16</span><h3>WinUI 3 核心特性（截至 2026-06）</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>与系统解耦</dt><dd>通过 NuGet 包独立分发，新控件不再受系统更新周期限制。</dd><dt>Fluent Design</dt><dd>原生云母（Mica）、亚克力（Acrylic）半透明材质与流畅动画。</dd><dt>性能</dt><dd>文件管理器基准：内存分配 -41%、临时分配 -63%、函数调用 -45%、启动时间 -25%。</dd><dt>API 访问</dt><dd>作为 Win32 进程运行，可不受限访问全部 Windows 系统 API。</dd><dt>开发体验</dt><dd>C#/C++ + XAML，VS 2022 项目模板与 XAML 热重载。</dd><dt>环境要求</dt><dd>Windows 10 1809+，VS 2022 17.1+，勾「.NET 桌面开发」「C++ 桌面开发」工作负载。</dd><dt>未来动态</dt><dd>Build 2026 定名「WinUI」不再另起炉灶；窗口缩放黑边 2026 夏修复；将出 DataGrid/Charting 企业控件并适配 AI 智能体开发。</dd></dl></div></div>

## 04 · Windows 上的 Qt：环境、模块与许可（01339）

Qt 是跨平台 C++ 框架，Windows 支持成熟。两套界面方案：**Qt Widgets**（传统控件，办公软件）与**Qt Quick/QML**（声明式，现代触控动画）。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">编译器与 IDE 选择</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>MSVC</dt><dd>需装 Visual Studio + C++ 桌面负载；Qt 6 主要支持 MSVC 2019/2022；适合调原生 API。</dd><dt>MinGW</dt><dd>安装器自带编译器，无需 VS；习惯 GCC、追求轻量可选。</dd><dt>IDE</dt><dd>官方 Qt Creator 开箱即用；VS 装「Qt Visual Studio Tools」；VS Code + CMake 插件亦可。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">Windows 特殊点</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>构建</dt><dd>CMake（现代首选，与 VS 集成好）/ qmake（传统）。</dd><dt>高 DPI</dt><dd>Qt 5.6 起原生支持高 DPI 缩放。</dd><dt>打包</dt><dd><code>windeployqt</code>自动拷贝运行所需 DLL 与插件。</dd><dt>混编</dt><dd>可经<code>nativeEvent()</code>处理 MSG 结构与 Win32 混合。</dd></dl></div></div>

| 模块 | 用途 |
|---|---|
| QtCore | 事件循环、文件、线程、容器等核心非 GUI 功能。 |
| QtWidgets | 按钮、窗口、布局、表格等经典控件。 |
| QtQuick | QML 引擎，现代界面。 |
| QtNetwork | TCP/UDP/HTTP 网络。 |
| QtSql | 数据库（SQLite、MySQL 等）。 |
| QtMultimedia | 音视频播放、摄像头。 |

> **许可与分发**
> - 开源版 LGPLv3/GPLv3：动态链接发布可不公开源码，但需允许用户替换 DLL。
> - 商业版：可静态链接、免开源传染、获官方支持。
> - Windows 静态编译较麻烦（需自编静态 Qt），初期动态链接 + windeployqt 即可。
