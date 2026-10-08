---
title: "建站技术与数据工程"
description: "data.json数据库文件制作（84KB）、获取全国行政区划数据方案、Halo项目介绍及技术特点、推荐记录行动轨迹的APP四篇合并。"
pubDatetime: 2025-12-30
category: "建站与技术"
kind: "工具"
tags: ["JSON数据库", "行政区划", "Halo", "轨迹APP"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00335-2025-10-26 data.json数据库文件（采购台账转JSON，82.5KB）00371-2025-11-02 Halo项目介绍00459-2025-11-25 记录行动轨迹APP推荐00509-2025-12-25 行政区划数据整理方案（18.1KB）

## 01 · 采购台账 JSON 数据库方案（00335 · 82.5KB 大文件）

将 Excel 采购台账转换为结构化 JSON 文件，便于程序读取与检索。这份笔记记录了完整的字段设计与数据整理过程。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00335 · 2025-10-26</span><h3>data.json：采购台账结构化</h3></div><div style="padding:14px 16px"><p>目标：将采购台账 Excel 中的数据按统一格式整理为 data.json 文件，字段包括：合同编号、供应商名称、项目号、项目名称、数量、单位、采购单价、订单金额。</p><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:130px">JSON 字段</th><th style="width:150px">类型</th><th>说明</th></tr></thead><tbody><tr><td><b>contractNo</b></td><td>string</td><td>合同编号，唯一标识</td></tr><tr><td><b>supplierName</b></td><td>string</td><td>供应商全称</td></tr><tr><td><b>projectNo</b></td><td>string</td><td>项目编号</td></tr><tr><td><b>projectName</b></td><td>string</td><td>项目名称</td></tr><tr><td><b>quantity</b></td><td>number</td><td>采购数量</td></tr><tr><td><b>unit</b></td><td>string</td><td>计量单位（个/套/吨等）</td></tr><tr><td><b>unitPrice</b></td><td>number</td><td>采购单价（元）</td></tr><tr><td><b>orderAmount</b></td><td>number</td><td>订单总金额（元）</td></tr></tbody></table></div><p>整理过程中需要注意：金额字段统一为数值类型（不含千分位逗号）、空值统一为 null、日期格式统一为 ISO 字符串。整个文件约 82KB，包含数百条采购记录。</p></div></div>

## 02 · 行政区划数据整理（00509 · 18.1KB）

中国行政区划数据的层级结构与整理方案，用于前端级联选择器或地址库。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00509 · 2025-12-25</span><h3>省市区三级行政区划数据</h3></div><div style="padding:14px 16px"><p>行政区划数据采用三级嵌套结构：省 → 市 → 区/县。每条记录包含行政编码（如 110000 北京市）与名称。</p><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>数据来源</dt><dd>国家统计局公布的年度行政区划代码，或民政部官方数据。</dd><dt>JSON 结构</dt><dd>每个节点包含 code（行政区划代码）、name（名称）、children（下级数组）。</dd><dt>应用场景</dt><dd>前端级联下拉选择、地址自动补全、统计报表按区域聚合。</dd></dl><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>整理注意事项</h5><ul><li>直辖市（北京、上海、天津、重庆）在&quot;市&quot;层级直接下辖区，无地级市中转。</li><li>省直辖县级行政单位（如河南济源、湖北天门）需单独处理。</li><li>数据需定期更新，每年行政区划可能有微调。</li></ul></div></div></div>

## 03 · Halo 建站与轨迹工具（00371 / 00459）

Halo 开源博客系统的介绍，以及记录行动轨迹的 APP 推荐。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00371 · 2025-11-02</span><h3>Halo 项目：开源博客系统</h3></div><div style="padding:14px 16px"><p>Halo 是一款开源的 Java 博客系统，主打&quot;现代化的个人站点解决方案&quot;。相比传统的 WordPress，Halo 界面更现代，插件与主题生态活跃，适合技术爱好者搭建个人博客。</p><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>技术栈</dt><dd>后端 Java + Spring Boot，前端 Vue，数据库支持 MySQL/PostgreSQL/H2。</dd><dt>部署方式</dt><dd>Docker Compose 一键部署，或手动安装 JDK 与数据库。</dd><dt>核心特性</dt><dd>主题市场、插件扩展、Markdown 编辑、多图床支持。</dd></dl></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00459 · 2025-11-25</span><h3>行动轨迹记录 APP</h3></div><div style="padding:14px 16px"><p>用于记录日常出行轨迹的手机 APP，可在地图上绘制步行、骑行或驾车路线，记录距离、时间与耗时。适合户外运动爱好者记录训练数据。</p><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>核心功能</dt><dd>GPS 轨迹记录、路线回放、距离与配速统计。</dd><dt>推荐场景</dt><dd>徒步路线记录、骑行数据追踪、出差行程留痕。</dd></dl></div></div>
