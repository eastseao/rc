---
title: "消费页面 layout 与 stop 页面开发"
description: "消费页面 layout/pagetitle 实现、Front Matter 与 tab 导航，以及增加 stop 停留页面的开发记录。"
pubDatetime: 2025-10-11
category: "建站与技术"
kind: "长文"
tags: ["layout/page", "Front Matter", "tab 导航", "stop 停留页", "_tabs"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00222-2025-10-11 layout / pagetitle「消费」per：媒体消费页的 Front Matter 与 tab 导航多轮迭代00224-2025-10-11 增加 stop 页面：在导航栏加入记录停留城市的 stop 页，及 media 的 _tabs 文件

## 01 · 消费页的 layout / pagetitle 配置（00222）

媒体页最终定名「消费」，放在`_tabs/media.md`。五个关键字段：`layout: page`、`title: "消费"`、`permalink: /media/`、`icon: fas fa-book`、`order: 4`。**permalink 必须与 navigation.yml 里的 url 完全一致**。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00222 · 2025-10-11</span><h3>media.md 头部定稿</h3></div><div style="padding:14px 16px"><p>--- layout: page title: &quot;消费&quot; permalink: /media/ icon: fas fa-book order: 4 --- # 媒体消费</p><div style="overflow-x:auto;margin:16px 0;margin-bottom:0"><table><thead><tr><th style="width:130px">字段</th><th style="width:180px">取值</th><th>作用</th></tr></thead><tbody><tr><td><b>layout</b></td><td>page</td><td>用 Chirpy 的独立页面布局，不走文章 post。</td></tr><tr><td><b>title</b></td><td>&quot;消费&quot;</td><td>页面标题，也是浏览器标签与导航显示名。</td></tr><tr><td><b>permalink</b></td><td>/media/</td><td>固定访问链接；必须与导航 url 一致。</td></tr><tr><td><b>icon</b></td><td>fas fa-book</td><td>Font Awesome 图标，从 fa-photo-video 换成 fa-book 表阅读。</td></tr><tr><td><b>order</b></td><td>4</td><td>导航栏排序序号，数字越小越靠前。</td></tr></tbody></table></div></div></div>

## 02 · 消费页的 tab 导航结构（00222）

正文用一组`.media-nav`按钮切换六个标签：爱好、书、电影、系列、游戏、其他；每个标签对应一个`.tab-pane`，条目用`.media-item`行（左侧名称、右侧时长或作者）。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00222 · 2025-10-11</span><h3>media-nav 按钮与 tab-pane 骨架</h3></div><div style="padding:14px 16px"><p>&lt;div class=&quot;media-nav&quot;&gt; &lt;button class=&quot;nav-btn active&quot; data-tab=&quot;hobby&quot;&gt;爱好&lt;/button&gt; &lt;button class=&quot;nav-btn&quot; data-tab=&quot;books&quot;&gt;书&lt;/button&gt; &lt;button class=&quot;nav-btn&quot; data-tab=&quot;movies&quot;&gt;电影&lt;/button&gt; &lt;button class=&quot;nav-btn&quot; data-tab=&quot;series&quot;&gt;系列&lt;/button&gt; &lt;button class=&quot;nav-btn&quot; data-tab=&quot;games&quot;&gt;游戏&lt;/button&gt; &lt;button class=&quot;nav-btn&quot; data-tab=&quot;others&quot;&gt;其他&lt;/button&gt; &lt;/div&gt; &lt;div class=&quot;tab-content&quot;&gt; &lt;div id=&quot;hobby&quot; class=&quot;tab-pane active&quot;&gt; &lt;h2&gt;我的爱好&lt;/h2&gt; &lt;div class=&quot;media-item&quot;&gt; &lt;span class=&quot;item-name&quot;&gt;摄影&lt;/span&gt; &lt;span class=&quot;item-duration&quot;&gt;5年&lt;/span&gt; &lt;/div&gt; ... &lt;/div&gt; &lt;div id=&quot;books&quot; class=&quot;tab-pane&quot;&gt; &lt;h3&gt;小说类&lt;/h3&gt; &lt;div class=&quot;media-item&quot;&gt; &lt;span class=&quot;item-name&quot;&gt;《三体》&lt;/span&gt; &lt;span class=&quot;item-author&quot;&gt;刘慈欣&lt;/span&gt; &lt;/div&gt; &lt;/div&gt; &lt;/div&gt;</p><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><h5>结构约定</h5><ul><li>按钮<code>data-tab</code>与面板<code>id</code>一一对应；<code>active</code>标记当前显示项。</li><li>爱好类条目用<code>item-duration</code>（持续年数），书类条目用<code>item-author</code>（作者）。</li><li>示例数据：摄影 5 年、游泳 8 年、徒步 3 年、瑜伽 2 年、模型制作 4 年、手账记录 6 年；书含《三体》《活着》《百年孤独》《围城》《挪威的森林》。</li></ul></div></div></div>

## 03 · 新增 stop 停留城市页面（00224）

用户要在导航栏加一个 stop 页记录停留城市。做法是两步：`_tabs/stop.md`建页面，`_data/navigation.yml`加导航项；可选再做一个`_layouts/stop.html`带时间线样式。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00224 · 2025-10-11</span><h3>stop.md 完整内容（_tabs/stop.md）</h3></div><div style="padding:14px 16px"><p>--- layout: page title: &quot;停留城市&quot; permalink: /stop/ icon: fas fa-map-marker-alt order: 5 --- # 我的停留城市记录 这里记录了我曾经停留过的城市和相关的回忆。 ## 🌍 城市足迹 ### 🏙️ 国内城市 | 城市 | 停留时间 | 印象深刻的经历 | | 北京 | 2020-2021 | 参观了故宫和长城 | | 上海 | 2019-2020 | 在外滩欣赏夜景 | | 杭州 | 2022 | 西湖边的漫步 | ## 📍 未来想去的地方 - [ ] 拉萨 - 感受高原的神秘 - [ ] 三亚 - 享受海滩阳光 &gt; &quot;旅行不是为了到达目的地，而是为了享受旅途中的每一刻。&quot;</p><div style="overflow-x:auto;margin:16px 0;margin-bottom:0"><table><thead><tr><th style="width:160px">可选图标</th><th>说明</th></tr></thead><tbody><tr><td><code>fas fa-map-marker-alt</code></td><td>定位标记，默认选用。</td></tr><tr><td><code>fas fa-plane</code>/<code>fas fa-globe-americas</code></td><td>飞机 / 地球，偏旅行主题。</td></tr><tr><td><code>fas fa-suitcase</code>/<code>fas fa-road</code></td><td>行李箱 / 道路，偏途中主题。</td></tr></tbody></table></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00224 · 2025-10-11</span><h3>导航栏挂 stop 项（_data/navigation.yml）</h3></div><div style="padding:14px 16px"><p>- title: 首页 url: / - title: 分类 url: /categories/ - title: 标签 url: /tags/ - title: 归档 url: /archives/ - title: 停留 url: /stop/ - title: 关于 url: /about/</p><p style="margin-bottom:0">归档页图标用户要求从<code>fas fa-archive</code>换成「印刷」，推荐<code>fas fa-print</code>（打印）、<code>fas fa-newspaper</code>（报纸）、<code>fas fa-file-alt</code>（文件）三选一。</p></div></div>

## 04 · _tabs 文件组织与生效验证（00224）

Chirpy 的导航栏页面统一放在`_tabs/`，主题遍历`site.data.navigation`生成导航链接。新增页面要「页面文件 + 导航项」两头对齐。

| 文件 | 职责 |
|---|---|
| `_tabs/about.md`/`categories.md`/`tags.md`/`archives.md` | Chirpy 自带的导航栏页面。 |
| `_tabs/stop.md` | 新增：停留城市记录，permalink /stop/。 |
| `_tabs/media.md` | 新增：媒体消费页，title「消费」，permalink /media/。 |
| `_data/navigation.yml` | 导航数据文件，加 title + url（+ 可选 children 下拉）。 |

> **验证步骤**
> - 页面文件放进 _tabs 目录；navigation.yml 里的 url 与页面 permalink 完全一致。
> - 提交推送后等 GitHub Actions 构建成功，导航栏即出现新项，通常立即生效。
> - 图标依赖 Font Awesome，确认主题已引入该图标库，否则图标不显示。
