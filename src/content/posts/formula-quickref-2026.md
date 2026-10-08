---
title: "计算与公式速查"
description: "合并单元格求和函数、整理重复规格统计、涨价幅度计算、圆柱体体积公式四篇合并。"
pubDatetime: 2026-05-11
category: "建站与技术"
kind: "工具"
tags: ["Excel求和", "重复规格", "涨价幅度", "圆柱体积"]
---

> **本文合并自以下笔记**：00951-2026-04-16 圆柱体体积公式（含等体积换算实例）01119-2026-05-09 合并单元格求和函数（Excel 三种方法）01130-2026-05-11 整理重复规格统计（22 条 → 12 种）01136-2026-05-13 涨价幅度计算

## 01 · 圆柱体体积公式与等体积换算（00951）

圆柱体体积 = 底面积 × 高。已知半径或直径均可代入。

V = π · r² · h = π · (d/2)² · h = π · d² · h / 4

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>实例</span><h3>φ75×H60 的圆柱，换成 φ65 直径，高是多少？</h3></div><div style="padding:14px 16px"><p style="font-size:13.5px;color:inherit;line-height:1.8">原圆柱：直径 75 mm → 半径 37.5 mm，高 60 mm。新圆柱：直径 65 mm → 半径 32.5 mm，设高 h。体积相等：</p><div>π × (32.5)² × h = π × (37.5)² × 60<br></div><p style="font-size:13.5px;color:inherit;margin-top:8px">37.5² = 1406.25；32.5² = 1056.25；分子 1406.25 × 60 = 84375。<b>h = 84375 / 1056.25 ≈ 79.88 mm</b>（约 79.9 mm）。</p></div></div>

## 02 · Excel 合并单元格求和：三种方法（01119）

需求：L 列合并单元格内，等于左侧 J 列对应未合并列的求和。由于 Excel 公式无法自动感知合并单元格占据哪些行，需按场景选择方法。

| 方法 | 适用场景 | 操作要点 |
|---|---|---|
| **方法一：手动指定范围**（推荐） | 少量、大小固定的合并单元格 | 选中合并单元格，输入`=SUM(J2:J5)`（框选 J 列对应行），按 Ctrl+Enter。合并范围变化时需手动改行号。 |
| **方法二：VBA 自定义函数** | 大量、大小各异的合并单元格 | Alt+F11 插入模块，写 SumLeftJ 函数用`rng.MergeArea`自动获取合并行范围，再 SUM J 列。文件需存为 .xlsm。 |
| **方法三：数组公式** | 不愿启用宏且合并单元格有规律 | `=SUM(J2:INDEX(J:J,ROW()+ROWS($L$2:$L$5)-1))`按 Ctrl+Shift+Enter。仍需手动填行数，不如前两者方便。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>VBA 代码</span><h3>SumLeftJ 自定义函数（方法二）</h3></div><div style="padding:14px 16px"><div style="margin:14px 0">Function SumLeftJ(rng As Range) As Double Dim mergeArea As Range Dim firstRow As Long, lastRow As Long Set mergeArea = rng.MergeArea firstRow = mergeArea.Row lastRow = firstRow + mergeArea.Rows.Count - 1 SumLeftJ = Application.WorksheetFunction.Sum( _ Range(&quot;J&quot; &amp; firstRow &amp; &quot;:J&quot; &amp; lastRow)) End Function</div><p style="font-size:13.5px;color:inherit;margin-top:8px">在 L 列任意合并单元格内输入<code>=SumLeftJ(L2)</code>即可，L2 可以是该合并区域中任意单元格。</p></div></div>

## 03 · 涨价幅度计算公式（01136）

涨价幅度 = (涨价金额 ÷ 原价) × 100%

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>实例</span><h3>原价 1.35 元，涨价两毛（0.20 元），幅度多少？</h3></div><div style="padding:14px 16px"><div>幅度 = (0.20 / 1.35) × 100% ≈ 14.81%</div></div></div>

## 04 · 圆柱规格去重统计（01130 · 22 条 → 12 种）

用户提供了 22 条圆柱规格记录（格式含 φ75*H150mm、φ85x140mm、φ100mm*H180mm 等写法），要求整理重复规格。统一格式为「φ直径*H高度mm」后，统计结果如下：

| 规格 | 数量 | 规格 | 数量 |
|---|---|---|---|
| φ75*H80mm | 1 | φ75*H120mm | 1 |
| φ75*H90mm | 2 | φ65*H85mm | 2 |
| φ75*H92mm | 2 | φ85*H100mm | 1 |
| φ75*H100mm | 4 | φ85*H112mm | 1 |
| φ75*H150mm | 4 | φ85*H140mm | 1 |
| φ100*H180mm | 2 | φ85*H180mm | 1 |

共计**12 种唯一规格**，原始 22 条记录已去重。出现频次最高的是 φ75*H100mm 和 φ75*H150mm（各 4 条）。
