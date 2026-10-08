---
title: "腾讯 Marvis 硬件要求与兼容"
description: "Marvis 双模式与跨平台硬件要求表、HOMEPC 实测兼容对照、加内存升级建议与 16GB 门槛原因。"
pubDatetime: 2026-05-25
category: "AI与Agent"
kind: "长文"
tags: ["腾讯 Marvis", "硬件要求", "本地大模型", "兼容性"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：01204-2026-05-24 腾讯 Marvis 硬件要求（双模式与跨平台配置表）01205-2026-05-25 腾讯 Marvis 配置兼容性评估（HOMEPC 实测对照与升级建议）

## 01 · Marvis 是什么：双模式与多智能体（01204）

Marvis 是腾讯推出的**操作系统级个人 AI 助手**，支持**Windows、macOS、Android**，iOS 规划中；采用"1 主智能体 + 5 专项智能体"的多智能体架构。它在两种工作模式间切换，硬件需求也随之不同。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">隐私模式</h3><p style="font-size:13.5px;color:inherit">数据不出本地，核心由<b>Qwen 本地大模型</b>驱动，对算力（CPU 核数、内存容量）要求更高，适合处理敏感信息。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">效率模式</h3><p style="font-size:13.5px;color:inherit">采用端云协同，本地轻量模型 + 云端大模型，对硬件要求相对较低。</p></div></div>

## 02 · 跨平台硬件要求表（01204）

下表照录 Marvis 对各平台的配置要求。Windows 端按隐私模式与效率模式分别列出建议；macOS 与 Android 按机型 / 系统版本区分。

<table><thead><tr><th style="width:110px">平台</th><th style="width:130px">配置项</th><th style="width:230px">最低 / 建议配置</th><th>备注</th></tr></thead><tbody><tr><td rowspan="4"><b>Windows</b></td><td>处理器</td><td>隐私模式最低 8 核（如 Intel i7 / AMD Ryzen 7）；效率模式 4 核即可</td><td>核数越多，本地模型推理速度越快</td></tr><tr><td>内存</td><td>隐私模式建议 16GB 或以上；效率模式最低 8GB</td><td>内存不足会导致本地模型加载失败</td></tr><tr><td>存储</td><td>SSD，至少预留 2GB 可用空间</td><td>必须 SSD，HDD 无法保证加载速度</td></tr><tr><td>系统版本</td><td>Windows 10 / 11（64 位）</td><td>需开启虚拟化功能（WSL2）</td></tr><tr><td rowspan="2"><b>macOS</b></td><td>机型</td><td>MacBook Air（M1 及以上芯片）；MacBook Pro（M1 Pro 及以上）；Mac mini / iMac（M1 及以上）</td><td>不支持 Intel 芯片机型</td></tr><tr><td>系统版本</td><td>macOS 12 Monterey 及以上</td><td>需开启辅助功能权限</td></tr><tr><td><b>Android</b></td><td>系统版本</td><td>Android 9.0 及以上</td><td>需开启悬浮窗与无障碍服务权限</td></tr><tr><td><b>iOS</b></td><td>系统版本</td><td>规划中</td><td>暂未支持</td></tr></tbody></table>

## 03 · HOMEPC 实测兼容性评估（01205）

以一台实测机器（HOMEPC）对照 Marvis 要求逐项核对：系统与存储达标，CPU 略低于隐私模式建议（可运行但本地模型推理偏慢），**内存是硬伤**——8GB 无法满足本地大模型最低需求。

| 配置项 | HOMEPC 现有配置 | 评估结果 | 说明 |
|---|---|---|---|
| **操作系统** | Windows 11 专业版 | ✅ 兼容 | 系统版本满足 Win10/11（64 位）要求 |
| **CPU** | Intel Core i5-10400F（6 核 12 线程） | ⚠️ 基本兼容 | 低于隐私模式 8 核建议，效率模式可正常运行；隐私模式下本地模型推理速度较慢 |
| **内存** | 8GB DDR4 | ❌ 不兼容 | 低于隐私模式 16GB 建议，也低于"隐私模式最低 8GB"的边界——运行效率模式勉强，但本地大模型加载会失败 |
| **存储** | NVMe SSD，可用空间 200GB+ | ✅ 兼容 | 满足 SSD 且预留 2GB 以上要求 |
| **虚拟化** | WSL2 已开启 | ✅ 兼容 | 满足 Windows 端虚拟化要求 |

## 04 · 升级建议与 16GB 门槛原因（01205）

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>针对性升级</span><h3>加一条 8GB 内存即可满足最低要求</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:130px">项目</th><th>建议</th></tr></thead><tbody><tr><td><b>升级方案</b></td><td>加装一条 8GB DDR4 内存条，组成<b>16GB 双通道</b></td></tr><tr><td><b>推荐型号</b></td><td>A-DATA (威刚) 万紫千红 DDR4 3200MHz 8GB</td></tr><tr><td><b>预计价格</b></td><td>约<b>120 元</b></td></tr><tr><td><b>预期效果</b></td><td>满足 Marvis 隐私模式最低内存要求；Marvis 可正常安装运行，本地模型推理速度提升；同时改善 Windows 多任务整体流畅度</td></tr></tbody></table></div></div></div>

> **为什么是 16GB 内存？**
> - **本地大模型体积**：Marvis 内置的本地模型（如 Qwen 7B 级别），FP16 精度下模型权重约占**14GB 内存**；量化后（INT4）也需约 5-8GB。
> - **多智能体架构开销**：Marvis 采用"1 主智能体 + 5 专项智能体"，多智能体同时运行，上下文缓存、对话历史占用额外内存。
> - **本地索引与检索**：隐私模式下本地文档索引、向量检索需常驻内存。
> - **系统预留**：Windows 11 本身占用约 2-4GB 内存。

> **一句话结论**：HOMEPC 除内存外均达标，花约 120 元加一条 8GB DDR4（3200MHz，威刚万紫千红）组 16GB 双通道，即可让 Marvis 正常跑起来；若只想轻量使用效率模式，现有 8GB 也可勉强运行。
