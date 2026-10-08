---
title: "安卓 APP 开发入门与 Windows 开发准备"
description: "安卓 APP 开发新手入门指南（Android Studio/JDK/Kotlin/Jetpack Compose）与 Windows 安卓开发准备（WSA）。"
pubDatetime: 2026-06-21
category: "建站与技术"
kind: "长文"
tags: ["Android Studio", "JDK", "Kotlin", "Jetpack Compose", "WSA"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00161-2025-10-03 安卓 APP 开发新手入门指南（零基础五步路径）01327-2026-06-20 Windows 安卓开发准备（技术路径 + 环境要求 + Jetpack Compose）

## 01 · 零基础入门五步路径（00161）

对完全不懂编程的新手，路线是「搭环境 → Hello World → 设计界面 → 加交互 → 后续系统学习」。工具就两个：JDK 与 Android Studio。

| 阶段 | 核心任务 | 关键做法 |
|---|---|---|
| **1 搭环境** | 装 JDK 与 Android Studio | JDK 17+ LTS；Studio 安装路径勿含中文/空格；Gradle 慢可换国内镜像。 |
| **2 Hello World** | 新建 Empty Activity | Start a new project → Empty Activity → 命名 MyFirstApp，语言先选 Java；AVD 模拟器或真机（开发者选项+USB 调试，真机更快）。 |
| **3 设计界面** | XML 布局 | res/layout/activity_main.xml 切 Design 模式，拖拽 Button/TextView，自动生成 XML。 |
| **4 加交互** | 按钮点击事件 | findViewById 拿控件，setOnClickListener 弹 Toast。 |
| **5 后续** | 系统学习 | 深入一门语言（Kotlin 为主流）；四大组件 Activity/Service/BroadcastReceiver；Jetpack Compose 与 ViewModel/LiveData。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00161 · 2025-10-03</span><h3>第一个交互：点击按钮弹 Toast</h3></div><div style="padding:14px 16px"><p>// 在 MainActivity 的 onCreate 中 Button myButton = findViewById(R.id.my_button); myButton.setOnClickListener(new View.OnClickListener() { @Override public void onClick(View v) { Toast.makeText(MainActivity.this, &quot;恭喜你！代码生效了！&quot;, Toast.LENGTH_SHORT).show(); } });</p><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><h5>新手建议</h5><ul><li>从模仿开始：先做计算器、待办列表这类经典小应用。</li><li>善用搜索：Stack Overflow、CSDN、GitHub 找答案是必备能力。</li><li>第一个 APP 简陋很正常，坚持定期写代码是进步关键。</li></ul></div></div></div>

## 02 · Windows 上开发安卓的准备（01327）

在 Windows 上开发安卓分两步：先选技术路径，再搭环境。新手强烈建议从**原生 Android 开发**起步，用官方 Android Studio 打基础。

| 开发路径 | 工具/语言 | 适用 |
|---|---|---|
| **原生 Android** | Android Studio + Kotlin/Java | 性能最佳、系统融合度高、深调系统 API。新手首选。 |
| 跨平台 | Flutter / React Native / .NET MAUI | 一套代码多端，覆盖安卓/iOS/Windows，成本低。 |
| 游戏开发 | Unity / Unreal | 2D/3D 手机游戏，强图形渲染与物理。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">硬件要求</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>系统</dt><dd>64 位 Win10/Win11。</dd><dt>内存</dt><dd>至少 8GB，跑模拟器建议 16GB。</dd><dt>CPU</dt><dd>支持虚拟化（Intel VT-x / AMD-V）的 x86_64。</dd><dt>硬盘</dt><dd>至少 8GB，推荐 SSD；分辨率最低 1280×800。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">环境与测试</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>装 Studio</dt><dd>官网下载 .exe，C 盘紧可自定义路径；首启引导下 Android SDK；可设 ANDROID_HOME。</dd><dt>测试</dt><dd>内置 AVD 模拟器，或 USB 真机开开发者选项+USB 调试。</dd><dt>WSA</dt><dd>Win11 可装 Windows Subsystem for Android，直接在 Windows 跑安卓应用快速测试。</dd><dt>语言</dt><dd>Kotlin 官方力推，Java 资料丰富作备选。</dd></dl></div></div>

## 03 · Jetpack Compose：声明式 UI（01327）

「Kotlin Compose」即 Jetpack Compose，Google 官方现代 UI 工具包。区别于传统 XML「画好图纸再指挥施工」，Compose 用 Kotlin 代码直接**描述界面长什么样**，数据变了界面自动更新。

| 维度 | Jetpack Compose | 传统 XML 布局 |
|---|---|---|
| **范式** | 声明式，描述 UI「是什么」 | 命令式，告诉系统「怎么做」 |
| 语言 | 纯 Kotlin | Kotlin/Java + XML |
| UI 构建 | @Composable 函数组合嵌套 | XML 定义 + findViewById 查找 |
| 状态更新 | 自动响应状态变化重组 UI | 手动 setText 等更新 |
| 实时预览 | @Preview 注解直接看效果 | 预览较弱 |
| 适用 | 新项目首选，Google 推荐 | 维护旧项目或与 Compose 混合 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">为什么用它</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:6px">代码更精简：同功能按钮代码量可缩到约 1/10，Bug 更少。</li><li style="margin-bottom:6px">@Preview 实时预览，不必每次装到手机。</li><li style="margin-bottom:0">UI 与逻辑同在一个 Kotlin 文件，不必 XML/Kotlin 间来回切。</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">三个核心概念</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>@Composable</dt><dd>带注解的 Kotlin 函数即一个 UI 积木，可自由组合嵌套。</dd><dt>State</dt><dd>状态驱动 UI；<code>var count by remember { mutableStateOf(0) }</code>自动触发刷新。</dd><dt>Modifier</dt><dd>链式统一配置大小、边距、点击事件。</dd></dl></div></div>

从 Android Studio 的 Empty Activity 模板起步即默认配好 Compose 环境，可直接上手；官方「Jetpack Compose 基础知识」Codelab 是好起点。
