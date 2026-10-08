---
title: "价格计算与抽成算账"
description: "抖音商家抽成计算、涨幅计算澄清、终端价求出厂价计算、统计金额、价格表整理为表格五篇合并。"
pubDatetime: 2026-06-24
category: "生活杂记"
kind: "长文"
tags: ["抖音抽成", "涨幅", "出厂价", "价格表"]
---

> **本文合并自以下笔记**：01153-2026-05-16 抖音商家抽成计算01181-2026-05-20 涨幅计算澄清01220-2026-05-26 终端价求出厂价计算01221-2026-05-27 价格表整理为表格01337-2026-06-24 统计金额

## 01 · 抖音商家抽成怎么算（01153 · 2026-05-16）

抖音小店的技术服务费（俗称「抽成」）按类目不同而不同，并非统一百分比。核心规则是按**实付金额**（扣除退款后）乘以对应费率。

| 类目 | 技术服务费率 |
|---|---|
| 大部分实物商品（服装、家居、食品等） | 约**1% ~ 5%**，常见 5% |
| 虚拟商品 / 充值 / 线上服务 | 约**5% ~ 10%** |
| 珠宝文玩、部分高客单类目 | 可能更高，按平台当期规则 |

计算示例：客单价 100 元，类目费率 5%

平台抽成 = 100 × 5% =

5 元

商家实际到账 ≈ 100 − 5 − 支付通道费（约 0.6%）− 退款部分

注意：直播间「达人佣金」是另一笔费用（达人带货时从佣金比例中扣），与平台技术服务费叠加计算。

## 02 · 涨幅澄清与出厂价反推（01181 / 01220）

两笔算账：一笔是「涨幅」口径澄清（是涨了多少钱还是涨了百分之几），一笔是从终端价反推出厂价（把税、加价率一层层除回去）。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01181 · 2026-05-20</span><h3>涨幅计算澄清</h3></div><div style="padding:14px 16px"><p>用户原话问「涨了多少」，AI 先澄清口径：涨幅可以是<b>绝对金额</b>（现价−原价），也可以是<b>百分比</b>（(现价−原价)/原价×100%）。笔记里给出了两种口径的计算示例，并提醒「涨了 10 块」和「涨了 10%」是两回事，后者还要看原价基数。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01220 · 2026-05-26</span><h3>终端价求出厂价</h3></div><div style="padding:14px 16px"><p>已知终端零售价，要反推工厂出厂价，需要把终端价里的税、渠道加价一层层除回去。典型链路是：终端价 → 批发价 → 出厂价。</p><div>示例（假设增值税 13%，渠道加价率 30%）：<br></div><p style="margin-bottom:0">实际行业里，从出厂到终端还会叠多级分销、物流、营销费用，反推只能给一个近似区间，不能当精确财务数据用。</p></div></div>

## 03 · 统计金额（01337 · 2026-06-24）

一笔简单的金额统计需求：把若干条明细金额加总，核对合计。笔记里没有给出具体数字（用户在对话中贴了金额列表），核心动作就是求和并核对与预期是否一致。

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><p style="margin-bottom:0">这类「统计金额」问题最容易出的错是：单位不统一（有的写「万」有的写「元」）、把小数点点错、漏加一行。AI 的做法是先把所有金额按同一单位列出来，逐项累加，最后再与用户预期交叉核对。</p></div>

## 04 · 价格表整理为表格（01221 · 2026-05-27）

用户把一段散文式的价格描述贴给 AI，要求整理成结构化表格。AI 提取品名、规格、单价、单位等字段，输出为可直接复制到 Excel 的表格。

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><p style="margin-bottom:12px">整理原则：</p><ul style="padding-left:20px;font-size:13.5px;color:inherit;line-height:1.8"><li>把口语描述拆成列：品名 / 规格 / 单位 / 单价 / 备注。</li><li>同一品名不同规格分行，不合并单元格。</li><li>价格统一保留两位小数，单位统一为「元」。</li><li>原文里含糊的价格（如「大概几十块」）单列「备注」列标注，不臆造数字。</li></ul></div>
