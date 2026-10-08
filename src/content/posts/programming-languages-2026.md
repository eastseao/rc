---
title: "编程语言全景 · 2026 —— 特点、使用占比与整体分析"
description: "罗列 29 种主流编程语言，从范式、类型系统、内存管理、性能、典型领域、学习曲线等维度建档；以 TIOBE / PYPL / Stack Overflow / GitHub Octoverse 四大口径交叉呈现 2026 年使用占比，附性能×上手象限、薪资参考、AI 适配度与整体趋势分析。"
pubDatetime: 2026-09-23
category: "建站与技术"
kind: "长文"
tags: ["编程语言", "语言趋势", "TIOBE", "PYPL"]
---

## 00 · 总览：同一时刻，四种答案（四种统计口径 · 一个共同结论）

「哪种编程语言最流行」没有唯一答案，取决于统计口径。下表是 2026 年 9 月四大权威口径的对比——它们分别衡量搜索热度、学习者行为、开发者自报与实际工程贡献，合起来才能还原语言生态的全貌。

| 口径 | 统计方式 | 2026 第一 | 反映什么 | 数据时点 |
|---|---|---|---|---|
| **TIOBE 指数** | 搜索引擎查询热度加权（Google / Amazon / Wikipedia / Bing 等 25+ 站点） | Python117.76% | 「关注与搜索」热度，老牌语言权重高 | 2026-09 |
| **PYPL 指数** | Google 上语言教程的搜索频次 | Python152.08% | 「学习者与求职者」的搜索行为 | 2026-09 |
| **Stack Overflow 调查** | 4.9 万+ 开发者自报「使用过」的比例 | JavaScript166% | 开发者的「实际使用面」 | 2025（年度第 15 届） |
| **GitHub Octoverse** | 开源平台月度活跃贡献者数 | TypeScript1263.6 万 | 「工程实践与开源」的真实贡献 | 2025-08 |

> **先读口径**：四份榜单统计对象不同，数值不可直接横向相加；TIOBE / PYPL 衡量搜索热度（Python 因 AI 教程搜索量断层领先），Stack Overflow 与 GitHub 衡量实际使用（Web 语言与工程语言占优）。本页所有数字均标注来源与时点，详见页脚数据口径。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>发现 01</span><h3>Python：全口径领跑，AI 是主引擎</h3></div><div style="padding:14px 16px"><p>TIOBE / PYPL 双第一，SO 第三（57.9%，同比 +7 个百分点），GitHub 第二。</p><p>Python 已从脚本语言成长为 AI、数据科学、自动化与后端的事实标准；搜索口径下份额断层（PYPL 52.08%），但 TIOBE 热度同比回落 8.22 个百分点，属于 2025 年 AI 搜索峰值后的正常回归。</p></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>发现 02</span><h3>TypeScript：十多年来最大的一次登顶</h3></div><div style="padding:14px 16px"><p>2025 年 8 月首次超越 Python 与 JavaScript，成为 GitHub 使用最广语言。</p><p>月度贡献者 263.6 万、同比 +66.6%，一年新增超百万贡献者。框架默认 TypeScript + AI 时代类型信息的收益，共同推动「类型化的 JavaScript」成为新默认。</p></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>发现 03</span><h3>Rust：口碑与份额双升</h3></div><div style="padding:14px 16px"><p>TIOBE 首次进入前十（第 10，1.34%）；Stack Overflow 连续十年「最受喜爱」语言（72%）。</p><p>内存安全 + 零成本抽象让它成为系统软件、AI 基础设施与嵌入式的新宠，但绝对使用占比仍小，岗位供给有限、学习曲线陡峭。</p></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>发现 04</span><h3>科学计算座次变动，MATLAB 退潮</h3></div><div style="padding:14px 16px"><p>MATLAB 跌至 TIOBE 第 27（0.61%）；Julia 逼近前 20（第 21，0.74%）。</p><p>Python 与 R 持续分食数值计算市场，Julia 成为新变量；同时 Ada、Objective-C 重返前 20，Perl、Ruby 跌出——存量语言的周期性回归值得注意。</p></div></div></div>

## 01 · 四大榜单全景（TIOBE · PYPL · Stack Overflow · GitHub Octoverse）

每个口径下分别给出 2026 年最新的份额条形图与明细表。条形的意义因口径而异——TIOBE / PYPL 是「热度占比」，Stack Overflow 是「开发者使用率」，GitHub 是「月度贡献者规模」。

TIOBE · 热度

PYPL · 学习搜索

Stack Overflow · 使用率

GitHub · 贡献者

> **口径**：TIOBE 编程社区指数基于全球熟练工程师、课程与第三方供应商数量，经 Google、Amazon、Wikipedia、Bing 等 25+ 站点搜索查询加权计算，每月更新。它衡量「关注热度」，不衡量代码行数。

TIOBE 2026-09 · 前 15 名热度占比

绿色为榜首

Python

17.76%

C

10.28%

C++

8.67%

Java

7.54%

C#

4.22%

JavaScript

2.76%

Visual Basic

2.55%

SQL

2.16%

R

1.69%

Rust

1.34%

Fortran

1.24%

Go

1.10%

Delphi

1.08%

PHP

1.04%

Scratch

0.99%

TIOBE 2026-09 · 前 21 名明细

含较上年同期的排名与份额变化

| 排名 | 语言 | 份额 | 同比 | 较上年排名 | 一句话备注 |
|---|---|---|---|---|---|
| 1 | **Python** | 17.76% | −8.22% | 持平 | AI 搜索峰值后热度回落，仍稳居第一 |
| 2 | **C** | 10.28% | +1.63% | ↑1 | 嵌入式与系统软件基本盘回升 |
| 3 | **C++** | 8.67% | −0.13% | ↓1 | 与 C 交替第 2、3 位 |
| 4 | **Java** | 7.54% | −0.81% | 持平 | 企业存量庞大，缓慢下行 |
| 5 | **C#** | 4.22% | −2.16% | 持平 | .NET 生态稳定 |
| 6 | **JavaScript** | 2.76% | −0.46% | 持平 | 搜索热度口径下被低估 |
| 7 | **Visual Basic** | 2.55% | −0.28% | 持平 | 办公自动化存量语言 |
| 8 | **SQL** | 2.16% | +0.29% | ↑3 | 数据岗位需求带动 |
| 9 | **R** | 1.69% | +0.27% | ↑4 | 统计与数据分析回升 |
| 10 | **Rust** | 1.34% | +0.33% | ↑8 | 2026 年首次进入前十 |
| 11 | **Fortran** | 1.24% | −0.25% | ↑1 | 高性能计算存量稳固 |
| 12 | **Go** | 1.10% | −1.22% | ↓4 | 搜索热度波动，云原生基本盘不变 |
| 13 | **Delphi / Object Pascal** | 1.08% | −1.18% | ↓4 | 桌面开发存量 |
| 14 | **PHP** | 1.04% | −0.21% | ↑1 | Web 存量巨大（WordPress） |
| 15 | **Scratch** | 0.99% | −0.19% | ↑1 | 少儿编程教育语言 |
| 16 | **Assembly** | 0.89% | −0.15% | ↑1 | 底层与逆向工程利基 |
| 17 | **Ada** | 0.85% | −0.42% | ↓3 | 重返前 20，军工/航空安全关键系统 |
| 18 | **Swift** | 0.83% | +0.10% | ↑7 | Apple 生态开发 |
| 19 | **Objective-C** | 0.81% | +0.32% | ↑10 | 时隔多年重返前 20，存量 iOS 代码 |
| 20 | **COBOL** | 0.78% | −0.13% | ↑2 | 金融/政府核心系统，人才稀缺 |
| 21 | **Julia** | 0.74% | — | — | 距第 20 名仅 0.04 个百分点，逼近前 20 |

> **口径**：PYPL 统计 Google 上「语言教程」的搜索频次，更贴近学习者与求职者的选择行为。2026 年 9 月 Python 份额 52.08%，断层第一。

PYPL 2026-09 · 前 12 名搜索份额

Python

52.08%

Java

13.34%

C / C++

7.99%

R

3.83%

JavaScript

3.28%

Objective-C

3.21%

PHP

1.98%

Rust

1.70%

C#

1.60%

Swift

1.54%

Ada

1.47%

TypeScript

1.43%

PYPL 2026-09 · 前 15 名明细

趋势为一年变化

| 排名 | 语言 | 份额 | 一年趋势 |
|---|---|---|---|
| 1 | **Python** | 52.08% | +22.7% |
| 2 | **Java** | 13.34% | −0.7% |
| 3 | **C / C++** | 7.99% | −3.5% |
| 4 | **R** | 3.83% | −2.1% |
| 5 | **JavaScript** | 3.28% | −3.1% |
| 6 | **Objective-C** | 3.21% | +1.2% |
| 7 | **PHP** | 1.98% | −1.5% |
| 8 | **Rust** | 1.70% | −1.1% |
| 9 | **C#** | 1.60% | −2.7% |
| 10 | **Swift** | 1.54% | −1.8% |
| 11 | **Ada** | 1.47% | −1.0% |
| 12 | **TypeScript** | 1.43% | −0.8% |
| 13 | **Matlab** | 0.90% | −0.7% |
| 14 | **Ruby** | 0.73% | −0.3% |
| 15 | **PowerShell** | 0.69% | −0.5% |

> **口径**：Stack Overflow 年度开发者调查（2025 年第 15 届，超 4.9 万受访者）统计「过去一年使用过」的比例。JavaScript 连续第 11 年第一；HTML/CSS 为标记语言，单列口径。

Stack Overflow 2025 · 前 12 名开发者使用率

JavaScript

66.0%

HTML / CSS

61.9%

SQL

58.6%

Python

57.9%

Bash / Shell

48.7%

TypeScript

43.6%

Java

29.4%

C#

27.8%

C++

23.5%

PowerShell

23.2%

C

22.0%

PHP

18.9%

关键信号

调查中的喜爱度与增长

| 指标 | 结果 |
|---|---|
| **使用率增长最快** | Python（+7 个百分点，升至第三），Go 与 Rust（各 +2 个百分点）——均与 AI 开发与基础设施相关 |
| **最受喜爱语言** | Rust 连续第 10 年居首（72% 使用者愿继续使用）；其后 Gleam（70%）、Elixir（66%）、Zig（64%） |
| **最想学习语言** | Python 位列第一——开发者把职业赌注押在 AI / 数据科学方向 |
| **整体趋势** | 增长最快的语言均「AI 兼容」：Python 用于 AI 应用，Rust / Go 用于 AI 基础设施 |

> **口径**：GitHub Octoverse 2025（数据截至 2025 年 8 月）按「月度活跃贡献者」统计公开仓库。TypeScript 首次登顶，是十余年来最大的一次语言排名变动。

GitHub Octoverse 2025-08 · 前三名月度贡献者规模

单位：万人

TypeScript

263.6

Python

259.4

JavaScript

≈215

第 4–10 名为：4Java ·5C# ·6PHP ·7Shell ·8C++ ·9HCL ·10Go。

关键信号

| 指标 | 结果 |
|---|---|
| **登顶时刻** | 2025 年 8 月 TypeScript 以约 4.2 万贡献者的优势超越 Python；Python 此前已连续 16 个月第一 |
| **增量最大** | TypeScript 一年新增超 100 万贡献者（+66.6%）；Python 新增 85 万（+48%）——两者都在高速增长，是「超越」而非「取代」 |
| **驱动因素** | Next.js / Astro 等主流框架默认 TypeScript；AI 编程工具偏爱带显式类型的代码，形成「便利性循环」 |
| **Python 地位** | 仍为 GitHub 第二常用语言，AI / 数据科学仓库的主力，增长 +48% |

## 02 · 29 门语言档案（按族筛选 · TIOBE 前 50 为主 + 高频工程语言）

下表把每门语言按「诞生、范式、类型系统、内存管理、运行形态、性能档位、典型领域、上手难度、TIOBE 2026-09 位置、趋势」十个维度建档。性能与上手难度为相对档位（含主观判断），供横向比较；点击上方分类可只看某族语言。

全部 29

系统与底层 6

Web 5

移动与桌面 5

数据与科学 4

脚本与自动化 3

遗留与利基 6

| 语言 | 诞生 | 范式 | 类型系统 | 内存管理 | 运行形态 | 性能 | 典型领域 | 上手 | TIOBE 26-09 | 趋势 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Python** | 1991 | 多范式（OOP/函数式/过程式） | 动态 · 强类型 | GC | 解释型（CPython，可选 JIT） | 中 | AI / 数据科学 / 自动化 / 后端 | 平缓 | #1 · 17.76% | 高位·热度回落 |
| **C** | 1972 | 过程式 | 静态 · 弱类型 | 手动 | 编译型 | 极高 | 系统 / 嵌入式 / 内核 / 驱动 | 中等 | #2 · 10.28% | 回升 |
| **C++** | 1985 | 多范式（OOP/泛型/过程式） | 静态 · 强类型 | 手动 + RAII | 编译型 | 极高 | 游戏 / 高频交易 / 系统软件 | 陡峭 | #3 · 8.67% | 稳定 |
| **Java** | 1995 | 多范式（OOP 为主） | 静态 · 强类型 | GC（JVM） | 字节码 + JIT | 高 | 企业后端 / 大数据 / Android（传统） | 中等 | #4 · 7.54% | 缓慢下行 |
| **C#** | 2000 | 多范式（OOP/函数式/异步） | 静态 · 强类型 | GC（.NET） | .NET 编译 + JIT | 高 | 企业 / .NET / Unity 游戏 / 桌面 | 中等 | #5 · 4.22% | 稳定 |
| **JavaScript** | 1995 | 多范式（原型 OOP/函数式） | 动态 · 弱类型 | GC | 解释 + JIT（V8 等） | 中高 | Web 前后端 / 全栈 | 平缓（坑多） | #6 · 2.76% | 稳定·Web 统治 |
| **TypeScript** | 2012 | 多范式（OOP/函数式） | 静态 · 结构类型 + 推断 | GC（编译为 JS） | 编译为 JS | 中高（同 JS） | Web 全栈 / 大型前端 | 中等（需 JS 基础） | #39 · 0.43% | 上升·GitHub 登顶 |
| **SQL** | 1974 | 声明式（关系查询） | —（查询语言） | — | 数据库引擎解释 / 编译 | — | 数据库 / 数据分析 | 平缓（精通难） | #8 · 2.16% | 稳定微升 |
| **Go** | 2009 | 过程式 + 并发（goroutine） | 静态 · 强类型 + 推断 | GC（低延迟） | 编译型 | 高 | 云原生 / 微服务 / 基础设施 | 中等（语法简单） | #12 · 1.10% | 稳定中升 |
| **Rust** | 2010 | 多范式（函数式/并发） | 静态 · 强类型 · 所有权 | 无 GC（所有权 + 借用） | 编译型（LLVM） | 极高 | 系统 / 基础设施 / 嵌入式 / WASM | 陡峭 | #10 · 1.34% | 上升·首进前十 |
| **PHP** | 1995 | 过程式 + OOP | 动态 · 弱类型 | GC | 服务端解释型 | 中 | Web 服务端（WordPress / Laravel） | 平缓 | #14 · 1.04% | 缓慢下行·存量巨大 |
| **Kotlin** | 2011 | 多范式（OOP/函数式） | 静态 · 强类型 + 推断 | GC（JVM） | JVM / 原生 / JS 多平台 | 高 | Android 官方 / 后端 / 多平台 | 中等 | #26 · 0.67% | 稳定 |
| **Swift** | 2014 | 多范式（OOP/函数式/协议） | 静态 · 强类型 + 推断 | ARC | 编译型（LLVM） | 高 | Apple 生态（iOS / macOS） | 中等 | #18 · 0.83% | 回升 |
| **Ruby** | 1995 | 多范式（动态 OOP） | 动态 · 强类型 | GC | 解释型 | 中低 | Web（Rails）/ 脚本 | 平缓 | #22 · 0.73% | 缓慢下行 |
| **R** | 1993 | 统计计算范式 | 动态 · 强类型 | GC | 解释型（向量化） | 中低 | 统计 / 数据分析 / 学术 | 中等 | #9 · 1.69% | 稳定回升 |
| **MATLAB** | 1984 | 数值计算 / 矩阵 | 动态 | GC | 解释型（矩阵优化） | 中 | 科研 / 工程仿真 / 信号处理 | 平缓 | #27 · 0.61% | 下行·被分食 |
| **Scala** | 2004 | 多范式（OOP + 函数式） | 静态 · 推断强类型 | GC（JVM） | JVM | 高 | 大数据（Spark）/ 金融 / 后端 | 陡峭 | #44 · 0.39% | 利基稳定 |
| **Dart** | 2011 | 面向对象 | 静态 · 推断 | GC | AOT + JIT 编译 | 高 | 跨端 UI（Flutter）/ Web | 中等 | #41 · 0.43% | 稳定（Flutter 驱动） |
| **Perl** | 1987 | 过程式 + 文本处理 | 动态 · 弱类型 | GC | 解释型 | 中 | 文本处理 / 系统管理 / 遗留 | 中等 | #23 · 0.70% | 缓慢下行 |
| **Objective-C** | 1984 | 面向对象（消息传递） | 动态 | ARC | 编译型 | 高 | Apple 存量（iOS / macOS） | 中等 | #19 · 0.81% | 存量回升 |
| **Assembly** | 1950s | 底层机器指令 | 机器级 | 手动（寄存器 / 栈） | 汇编 | 极致 | 驱动 / 内核 / 嵌入式 / 逆向 | 陡峭 | #16 · 0.89% | 利基稳定 |
| **Visual Basic** | 1991 | 面向对象（快速开发） | 静态 · 可推断 | GC（.NET） | .NET | 中 | 桌面 / 办公自动化 / 遗留 | 平缓 | #7 · 2.55% | 存量稳定 |
| **Lua** | 1993 | 脚本 / 多范式 | 动态 | GC | 解释 + LuaJIT | 中高 | 游戏嵌入 / 配置 / 扩展 | 平缓 | #31 · 0.57% | 稳定 |
| **COBOL** | 1959 | 过程式（业务） | 静态 · 强类型 | 手动（记录） | 编译型 | 中 | 金融 / 政府核心系统 | 中等 | #20 · 0.78% | 存量稳定·人才稀缺 |
| **Delphi / Object Pascal** | 1995 | 面向对象 | 静态 · 强类型 | 手动 + ARC | 编译型 | 高 | 桌面开发 / 遗留 | 中等 | #13 · 1.08% | 缓慢下行 |
| **Fortran** | 1957 | 过程式（数值） | 静态 · 强类型 | 手动 | 编译型 | 极高（数值） | 高性能计算 / 科学计算 | 中等 | #11 · 1.24% | 存量稳定 |
| **Ada** | 1980 | 过程式 + 并发 | 静态 · 强类型 | 手动（受控） | 编译型 | 高 | 航空 / 军工 / 安全关键系统 | 陡峭 | #17 · 0.85% | 回归前 20 |
| **Shell / Bash** | 1989 | 命令脚本 | 动态 | 进程级 | 解释型 | 低 | 运维 / 自动化 / DevOps | 平缓 | #51+ | 稳定必备 |
| **Scratch** | 2003 | 可视化积木编程 | — | — | 图形化 | 低 | 少儿编程教育 | 平缓 | #15 · 0.99% | 稳定 |

上表含 TIOBE 前 20 的全部语言；TIOBE 第 51–100 名（Elixir、Erlang、F#、Clojure、Groovy、Scheme、Nim、Solidity、Tcl 等）未逐行建档，但第 01 章榜单章节已给出前 50 名位置。数据时点 2026-09。

## 03 · 维度横评：性能 × 上手 × 薪资 × AI 适配（把档案表的维度拿出来横向比）

语言选择的本质是权衡：性能与开发效率、底层控制与内存安全、生态规模与上手成本。下面按四个横切维度给出对照。

3.1 性能档位 × 上手难度象限

示意 · 语言位置为主观归类，仅作相对比较

上手：平缓

上手：中等

上手：陡峭

性能：高 / 极高

平缓 · 高性能

Go

Swift

Dart

Julia

Lua

Kotlin

中等 · 高性能

Java

C#

C

Objective-C

陡峭 · 高性能

Rust

C++

Assembly

Scala

Ada

性能：中低

平缓 · 中低性能

Python

JavaScript

PHP

Ruby

Shell

SQL

VB

Scratch

中等 · 中低性能

R

MATLAB

Perl

COBOL

Delphi

Fortran

陡峭 · 中低性能

—

> **解读**：右上象限（平缓且高性能）几乎不存在——Go / Swift / Dart 是最接近「兼顾性能与上手」的选择；Python / JavaScript 把「开发效率」放在第一位，性能靠运行时与生态（NumPy、V8、异步）弥补；Rust / C++ / Assembly 位于左下之外的右下象限——性能天花板最高、上手成本也最高。这是「写起来快」与「跑起来快」的经典权衡。

3.2 美国市场薪资参考

2025–2026 多方招聘数据综合 · 区间仅供参考

| 语言 | 资深岗位参考区间（万美元/年） | 需求与说明 |
|---|---|---|
| **Rust** | 13 – 17 | 高需求低供给，系统 / 区块链 / 基础设施岗位溢价明显 |
| **Go** | 12 – 16.5 | 云原生 / Kubernetes / 微服务，均值约 14.7 万 |
| **Scala** | 12.5 – 16 | 大数据（Spark）/ 金融科技利基岗位 |
| **Kotlin** | 12 – 14 | Android / 后端，需求年增约 15% |
| **TypeScript** | 12.5 – 13.5 | 均值约 13.2 万，相对 JavaScript 有 10–15% 溢价 |
| **C++** | 12.8 – 15 | 系统 / 游戏 / 量化，均值约 13 万 |
| **Swift** | 12 – 14 | iOS 原生开发，中位约 13 万 |
| **Python** | 12.5 – 14.5 | 均值约 12.6 万；AI / ML 工程师可至 14.5 万+ |
| **Java** | 11.7 – 15 | 企业后端岗位池最大，区间宽 |
| **JavaScript** | 11 – 13 | 岗位池最大，均值约 11.4 万 |
| **Ruby** | 10.5 – 14 | 均值约 12.1 万 |
| **PHP** | 8 – 13 | 主流语言中偏低，来源差异大 |

> **口径**：区间综合 VentureBeat 2025 均薪、Second Talent 2026 资深中位、DistantJob / Kickstart 2026 等招聘聚合数据；不同来源与地区差异显著（美国境内也因城市、年限、行业浮动 20–30%），仅用于相对比较，不构成薪酬承诺。

3.3 AI 时代的适配度

2025–2026 的证据：增长最快的语言都「AI 兼容」

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>AI 应用层</span><h3>Python</h3></div><div style="padding:14px 16px"><p>AI / 机器学习生态的事实标准（PyTorch、Transformers、LangChain）；SO 2025 使用率 +7 个百分点，增长最快；也是最想学习的语言。</p></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>AI 友好类型</span><h3>TypeScript</h3></div><div style="padding:14px 16px"><p>显式类型让 AI 编程工具生成与重构更可靠；框架默认 TS + AI 辅助，2025 年 8 月登顶 GitHub，一年新增超百万贡献者。</p></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>AI 基础设施</span><h3>Rust</h3></div><div style="padding:14px 16px"><p>推理引擎、向量数据库与工具链的新宠（内存安全 + 性能）；SO 连续十年最受喜爱，TIOBE 2026 首进前十。</p></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>AI 服务后端</span><h3>Go · Java · C#</h3></div><div style="padding:14px 16px"><p>承载 AI 服务的网关、调度与业务系统：Go 主打云原生并发，Java / C# 以企业生态与工程化成熟度见长。</p></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>推理内核</span><h3>C / C++</h3></div><div style="padding:14px 16px"><p>训练框架与推理引擎的底层基座（CUDA、ONNX Runtime 等），性能敏感路径几乎无法绕开。</p></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>浏览器端</span><h3>JavaScript</h3></div><div style="padding:14px 16px"><p>AI 应用的前端入口（WebLLM、Transformers.js 等浏览器端推理），仍是使用面最广的语言（SO 66%）。</p></div></div></div>

## 04 · 趋势与整体分析（2024–2026 关键节点 · 结论与选型建议）

把第 01–03 章的证据收拢成一条时间线和三组结论：谁在上升、谁在守成、谁在退潮，以及不同角色该怎么选。

4.1 关键节点时间轴

2024-10

Octoverse 2024

**Python 首次登顶 GitHub**：超越 JavaScript 成为开源平台最常用语言，此后连续 16 个月保持第一（至 2025-08）。

2025-07

SO 调查 2025

**Python 使用率 +7 个百分点**，以 57.9% 超越 SQL 升至第三；Rust 连续第十年「最受喜爱」（72%）；增长最快的语言全部与 AI 相关。

2025-08

Octoverse 2025

**TypeScript 登顶 GitHub**：月度贡献者 263.6 万（+66.6%），一年新增超百万贡献者，是十余年来最大的一次语言排名变动。

2026-07

TIOBE

**Rust 首次进入前十**；2026-09 排名第 10（1.34%，同比 +0.33 个百分点），内存安全语言持续渗透系统软件与 AI 基础设施。

2026-09

TIOBE

**科学计算座次变动**：MATLAB 跌至第 27（0.61%）；Julia 逼近前 20（第 21，距第 20 名 COBOL 仅 0.04 个百分点）；Ada、Objective-C 重返前 20，Perl、Ruby 跌出。

4.2 语言态势分组

综合四口径与一年变化

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>上升</span><h3>扩张中的语言</h3></div><div style="padding:14px 16px"><p>TypeScript · Rust · Python · Julia · Go</p><ul><li><b>TypeScript</b>：GitHub 登顶、SO 第六且上升，AI 工具链最受益</li><li><b>Rust</b>：TIOBE 首进前十 + SO 十年最受喜爱</li><li><b>Python</b>：绝对使用量仍高速增长（GitHub +48%）</li><li><b>Julia</b>：逼近 TIOBE 前 20，科学计算新变量</li><li><b>Go</b>：SO 使用率 +2 个百分点，云原生基本盘</li></ul></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>守成</span><h3>稳固的中坚</h3></div><div style="padding:14px 16px"><p>C · C++ · Java · C# · JavaScript · SQL · R · PHP · Kotlin · Swift · Dart · Lua · Shell · COBOL · Fortran</p><ul><li>企业、系统与 Web 的存量基本盘，岗位供给最大</li><li>排名小幅波动，但实际使用规模稳定</li><li>Swift / Objective-C 受 Apple 存量生态托底，出现回升</li></ul></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>退潮</span><h3>收缩中的语言</h3></div><div style="padding:14px 16px"><p>MATLAB · Perl · Ruby · Delphi · Visual Basic</p><ul><li><b>MATLAB</b>：从长期前 20 跌至第 27，被 Python / R / Julia 分食</li><li><b>Perl / Ruby</b>：2026 年跌出 TIOBE 前 20</li><li><b>Delphi / VB</b>：桌面与办公自动化存量缓慢收缩</li><li>均以「存量维护」为主，新项目占比低</li></ul></div></div></div>

4.3 选型建议

按角色与目标，非唯一答案

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:14.5px;margin-bottom:6px"><b>入门 / AI / 数据</b></h3><p style="font-size:13px;color:inherit">首选<b>Python</b>：语法平缓、生态最广、AI 全链路通用，学习与就业回报比最高。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:14.5px;margin-bottom:6px"><b>Web 前端 / 全栈</b></h3><p style="font-size:13px;color:inherit">从<b>JavaScript</b>起步，大型项目直接<b>TypeScript</b>：类型信息同时利于工程维护与 AI 工具辅助。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:14.5px;margin-bottom:6px"><b>后端 / 云原生</b></h3><p style="font-size:13px;color:inherit"><b>Go</b>（并发与部署简单）、<b>Java / C#</b>（企业生态）、<b>Python</b>（AI 服务）、新系统高性能可用<b>Rust</b>。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:14.5px;margin-bottom:6px"><b>系统 / 嵌入式 / 性能敏感</b></h3><p style="font-size:13px;color:inherit"><b>C</b>打底、<b>C++</b>扩展、新代码优先<b>Rust</b>（内存安全 + 同等性能）；极致底层才需要 Assembly。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:14.5px;margin-bottom:6px"><b>移动 / 跨端</b></h3><p style="font-size:13px;color:inherit">Android 用<b>Kotlin</b>、iOS 用<b>Swift</b>；一套代码跨双端可选<b>Dart + Flutter</b>。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:14.5px;margin-bottom:6px"><b>遗留系统维护</b></h3><p style="font-size:13px;color:inherit"><b>COBOL / VB / Perl</b>：存量需求稳定、供给稀缺，维护岗位竞争小、薪资不低，但天花板明显。</p></div></div>

##### 整体判断

语言生态正在被「AI 兼容性」重新排序，但头部格局不会快速重写。

Python 因 AI 成为全口径第一或前列；TypeScript 因 AI 工具与框架默认而登顶 GitHub；Rust 因 AI 基础设施而进入前十。与此同时，C / Java / JavaScript 凭借数十年存量仍是岗位与代码体量的绝对主体——2026 年的正确姿势是「增量用新语言，存量守基本盘」，而不是押注单一语言的兴衰。
