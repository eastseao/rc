---
title: "工厂前端应用·前后端解释·Actions·HTML转PDF"
description: "工厂前端七大应用、采购数据库与 Excel 模板、前后端餐厅比喻、sass-embedded 构建排错五方案与转 PDF 选型表。"
pubDatetime: 2026-06-29
category: "建站与技术"
kind: "长文"
tags: ["工厂数字化", "排错", "PDF", "前后端"]
---

> **本文合并自以下笔记**（序号即原笔记编号）：00355-2025-10-29 工厂网页前端功能应用总结01353-2026-06-29 前端后端具体工作解释00401-2025-11-06 GitHub Actions 构建错误解决方案00580-2026-02-11 HTML 转 PDF 工具选择指南

## 01 · 网页前端在工厂能干的七件事（00355）

前端不只是展示窗口，而是把 MES/SCADA/ERP/IoT 的数据变成一线员工能直接操作的界面。按从基础到高级排：

- 生产监控大屏 ：实时看板显示计划/实际产量、完成率、产线状态；设备三色灯（绿运行/黄待机/红故障）；工艺参数超限告警；自动出日报周报与 OEE、合格率图表。

- 设备管理与预测性维护 ：电子档案、实时振动/电流监测、接后端 AI 预警生成维修工单、保养到期提醒——从事后维修转预防性维护。

- 生产流程与工单 ：电子工单派发、作业指导书图文/视频、扫码确认物料追溯、工序完成一键上报，无纸化。

- 质量管控与追溯 ：检验录入、SPC 控制图、一物一码按序列号反查批次/设备/操作人、不良品分析看板。

- 仓储物流 ：库位地图可视化、扫码入库上架拣选、库存安全预警、AGV 路径实时显示。

- 人员绩效 ：个人任务看板、实时产量/效率排行、技能矩阵图。

- 安防环境 ：视频监控集成、车间温湿度/粉尘/有害气体监测报警、门禁电子地图。

**技术栈**：可视化 ECharts / D3.js / AntV G2 / Three.js（3D）；实时数据走 WebSocket 或 SSE；交互框架 Vue / React / Angular；响应式适配电脑、平板、手机与大屏。

## 02 · 包装采购本地数据库与 Excel 模板（00355）

中小型工厂先用本地 SQLite/Access/本地 MySQL 足够。包装采购围绕四张表组织数据：

| 表 | 关键字段 | 用途 |
|---|---|---|
| **suppliers 供应商** | supplier_id、名称、联系人、电话、付款条件、交货周期、评级(1-5) | 供应商档案与筛选 |
| **packaging_materials 物料** | material_id、名称、规格、类型、单位、单价、moq 起订量、保质期、存储条件、外键 supplier_id | 物料主数据 |
| **purchase_orders 采购订单** | po_number、供应商、订单/预计/实际交货日、总额、状态、优先级 | 订单全程跟踪 |
| **order_items 订单明细** | po_id、material_id、数量、单价、金额、已收数量、质检状态 | 一行货一条明细 |

Excel 版就是同构多工作表：Suppliers（S001…）、Materials（M001…）、PurchaseOrders（PO2024001…），用 ID 互相关联；另加价格历史表做成本分析。ID 按规则编号、评级用于筛选、最小起订量避免小额采购。

## 03 · 纯前端包材进度跟踪系统（00355）

完全可以：一个本地 index.html 就能连本地数据文件做日常包材进度跟踪。技术方案：纯静态 HTML+CSS+JS，数据存 data/orders.json 与 data/materials.json，双击浏览器打开即可用。

**文件结构**：index.html；data/orders.json、materials.json；css/style.css；js/app.js；lib/（Chart.js 等）。页面分四个页签：总览看板、采购订单、物料管理、供应商。看板顶部四张统计卡：进行中订单、待收货订单、本周到期、库存预警；下方两张 Chart.js 图：订单状态分布、近期交付情况。

> **局限提醒**：纯本地 JSON 方案只适合单台电脑单人/小团队；多人协作、要保留多人修改痕迹时再上本地数据库+后端。数据记得定期备份 JSON 文件。

## 04 · 前端和后端到底各做什么（01353 · 餐厅比喻）

前端是服务员和用餐环境，后端是厨房和仓库。顾客看菜单点菜，服务员把单递后厨，厨师取食材做菜再端回桌上。

| 维度 | 前端 | 后端 |
|---|---|---|
| **关注点** | 界面、交互、用户体验 | 数据、逻辑、安全、性能 |
| **核心工作** | HTML 结构、CSS 布局、JS 交互、fetch/axios 调 API、状态路由管理、性能兼容 | 业务规则（下单算价扣库存）、设计 GET/POST 接口、操作 MySQL/PostgreSQL/MongoDB/Redis、JWT 登录鉴权、防注入与缓存、Nginx 部署 |
| **运行环境** | 浏览器、手机等客户端 | 服务器（Linux） |
| **核心语言** | HTML + CSS + JavaScript / TypeScript、React/Vue/Angular | Node.js、Python、Java、Go、PHP 等 |

两者用 HTTP/HTTPS 走 API 沟通：前端请求 → 后端查库按逻辑处理 → 打包 JSON 返回 → 前端渲染。例：登录时前端做非空校验后提交 /api/login，后端核对密码生成 token 存回；两者都掌握就是全栈工程师。

## 05 · GitHub Actions 构建失败：sass-embedded 排错（00401 · Jekyll Chirpy）

现象：seamoonappear.github.io 跑「Build and Deploy Jekyll site」，`rake failed, exit code 1`，卡在`sass-embedded-1.93.3`原生扩展编译，Bundler 退出码 5。依赖链：jekyll-theme-chirpy 7.4.1 → jekyll 4.4.1 → jekyll-sass-converter 3.1.0 → sass-embedded；runner 是 Ruby 3.1.7。

| 方案 | 怎么做 |
|---|---|
| **① 升 Ruby（首选）** | workflow 里`ruby/setup-ruby`的`ruby-version`从 3.1.7 改 '3.2' 或更高（Ruby 最新稳定版为 3.4.7） |
| **② 锁版本或换 sassc** | Gemfile 里`gem 'sass-embedded', '~> 1.72.0'`，或直接注释掉 sass-embedded 换`gem 'sassc'` |
| **③ 升 Chirpy** | `gem "jekyll-theme-chirpy", "~> 7.4.2"` |
| **④ 装系统依赖** | 加一步`sudo apt-get install -y build-essential pkg-config` |
| **⑤ 清理重装** | 本地`bundle clean --force && bundle install`，提交新 Gemfile.lock；慎删 lock 文件 |

先试 ①；不行再 ②③。提交后重跑 Actions。

## 06 · HTML 转 PDF 选哪个工具（00580）

按使用场景选：偶尔转一个，浏览器打印最省事；要嵌进程序自动出报表，选开发库；服务器批量高质量，上命令行。

| 类别 | 工具 | 适用场景 |
|---|---|---|
| **开发库** | IronPDF | .NET 项目首选，Chromium 内核，动态生成报告/发票 |
| **开发库** | Aspose.HTML | .NET/Java 集成，无需外部浏览器，保真度高 |
| **开发库** | jsPDF | 纯前端，网页里点按钮导出指定内容 |
| **桌面软件** | 万兴 PDF | 图形界面，不编程用户，打开 HTML 另存 PDF |
| **在线/浏览器** | HiPDF、浏览器 Ctrl+P「另存为 PDF」 | 临时少量转换；浏览器打印最简单通用，敏感文件别传在线站 |
| **命令行** | pdfChip / wkhtmltopdf | 服务器端自动化、大批量；pdfChip 支持 CMYK 专色，wkhtmltopdf 开源基于 WebKit |
