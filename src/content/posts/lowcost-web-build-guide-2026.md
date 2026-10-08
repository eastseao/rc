---
title: "低成本建站与企业官网搭建指南"
description: "两篇笔记合并——GitHub Pages 零成本搭建静态采购管理系统的完整步骤（仓库命名、目录结构、localStorage/BaaS、部署与局限），及国内企业官网低成本方案选型对比，含费用明细与域名、ICP 备案两条避坑要点。"
pubDatetime: 2026-05-08
category: "建站与技术"
kind: "手册"
tags: ["GitHub Pages", "静态站", "WordPress", "ICP 备案", "SaaS 建站"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00387-2025-11-03 GitHub Pages搭建采购管理系统指南01118-2026-05-08 企业官网最低成本搭建指南

## 01 · GitHub Pages 静态站搭建五步（00387 · 2025-11-03）

GitHub Pages 只托管静态资源（HTML / CSS / JS），**不支持 PHP、Java、Python 等服务端语言**。所以所谓「在上面建采购管理系统」，本质是做一个前端单页应用（SPA），交互与数据全在浏览器端完成。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>架构与局限</span><h3>先想清楚能做什么、不能做什么</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>可行路线</dt><dd>前端 SPA：页面与交互逻辑全由浏览器 JavaScript 处理，用 Bootstrap / Layui 等 UI 框架快速搭后台风格界面。</dd><dt>数据持久化</dt><dd>初级用浏览器 localStorage；进阶接免费 BaaS（Firebase / Supabase / Airtable），在前端直接读写、跨设备同步。</dd><dt>核心局限</dt><dd>无法做真正的服务端逻辑（用户会话、服务器端数据库、微信支付等）。定位是<b>前端演示原型</b>，适合项目展示、毕业设计、学前端，切勿用于真实敏感商业数据或金钱交易。</dd></dl></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>五步走</span><h3>从建仓库到上线访问</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:60px">步骤</th><th style="width:180px">做什么</th><th>关键细节</th></tr></thead><tbody><tr><td><b>1</b></td><td>准备 GitHub 仓库</td><td>想用<i>https://用户名.github.io</i>直达，仓库名必须叫「用户名.github.io」；否则任意仓库名都可，地址为<i>用户名.github.io/仓库名</i>。克隆到本地。</td></tr><tr><td><b>2</b></td><td>建项目目录</td><td>典型结构：index.html 主入口；css/、js/（app.js 主逻辑、auth.js 模拟登录、storage.js 数据存取）；pages/ 放 products.html、suppliers.html；libs/ 放第三方库。</td></tr><tr><td><b>3</b></td><td>开发界面与交互</td><td>用 Bootstrap / Layui 搭表格、表单、导航；jQuery 做提交、列表渲染筛选、弹窗。可参考网上的 Vue 资产采购管理、JavaWeb 采购系统——只学它的前端布局思路，后端技术不适用。</td></tr><tr><td><b>4</b></td><td>实现数据模拟</td><td>localStorage 版：读 JSON.parse(localStorage.getItem(...)) 作初始数组，每次操作后 localStorage.setItem 写回；要跨设备同步再上 BaaS。</td></tr><tr><td><b>5</b></td><td>部署上线</td><td>代码 git 推送后，进仓库 Settings → Pages → Source 选部署分支（main / master）保存，稍等即可通过 github.io 地址访问。</td></tr></tbody></table></div><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:14px"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">典型功能模块</h3><p style="font-size:13.5px;color:inherit">模拟登录、仪表盘统计、商品增删改查与分类、采购单创建审批流程模拟、供应商信息维护、简单留言/动态——按需逐步实现。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">三个增强方向</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>多页组织</dt><dd>多页面用 VuePress / Docsify 这类静态站点生成器组织路由。</dd><dt>自动部署</dt><dd>用 GitHub Actions 在每次推送后自动构建部署。</dd><dt>自定义域名</dt><dd>已有域名可在 Pages 设置里绑定，访问更短更好记。</dd></dl></div></div></div></div>

## 02 · 企业官网低成本方案选型对比（01118 · 2026-05-08）

在国内用最低成本搭企业官网，总思路是「自己动手 + 免费开源工具 + 只花必须的固定费用」。2026 年当下最省心的是全托管 SaaS 建站，首年几百元即可；愿意折腾则云服务器自建性价比最高。

| 对比维度 | 方案一 · SaaS 平台建站（首选） | 方案二 · 云服务器自建 | 方案三 · 传统定制开发 |
|---|---|---|---|
| **建站方式** | 零代码可视化拖拽，用平台模板 | 镜像一键部署 WordPress 等开源程序，自己配置维护 | 全权委托第三方公司从零设计开发 |
| **年投入** | **约 150–900 元**（通常含服务器） | **约 250–1800 元**（需单独买服务器） | **约 5,000–30,000 元+** |
| **上手难度** | 极低 | 中等（需基础学习） | 无需动手但沟通成本高 |
| **功能灵活度** | 中（受平台功能限制） | 高（插件生态丰富，可深度定制） | 极高（完全按需求定制） |
| **后期维护** | 平台负责，省心 | 自管安全更新与数据备份 | 依赖开发公司，通常另收维护费 |
| **推荐人群** | 追求低价高效的小微企业与个人 | 愿意折腾、有学习意愿的站长 | 个性化需求复杂、预算充足的企业 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">费用明细（照录）</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>SaaS 参考价</dt><dd>乔拓云初级版活动价一年 132.7 元；码云数智基础版 698 元/年（通常含域名与 SSL）；凡科建站 800–3000 元/年。注意首年便宜、次年续费可能上涨，问清独立域名绑定与 SSL 证书是否另收费。</dd><dt>自建开销</dt><dd>服务器抓新客/活动：阿里云或腾讯云入门级轻量应用服务器可低至 38 元/年；.com 域名约 55–60 元/年，.cn 约 38–42 元/年；WordPress 等开源程序软件本身免费。</dd><dt>定制开发</dt><dd>阿里云定制服务起步价就在 5480 元/年，远超低成本范畴，初创企业不推荐。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">自建四步流程</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>① 购买</dt><dd>买轻量应用服务器 + 域名。</dd><dt>② 装面板</dt><dd>装宝塔面板。</dd><dt>③ 部署</dt><dd>面板里一键部署 WordPress（或 Halo 等开源 CMS）。</dd><dt>④ 选主题</dt><dd>挑免费主题模板换上，内容即可上线。</dd></dl></div></div>

> **两件绕不开的事（避坑）**
> - **域名选好**：.com / .cn 是性价比最高的选择；.vip、.shop 等非刚需后缀不推荐。
> - **ICP 备案必做**：用国内服务器必须备案；企业备案需营业执照、审核更严，约 15–20 个工作日；**备案期间网站不能访问，要提前排期；个人备案不能用于商业网站**。

> **结论（照录）**：2026 年在国内低成本搭官网，SaaS 全托管是大多数人的最优解——首年成本最低、最省心；愿意投入时间学习的「折腾派」，云服务器自建 WordPress 提供更高的性价比与自由度。
