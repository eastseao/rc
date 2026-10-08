---
title: "本地媒体播放器网页与清单页面设计"
description: "本地媒体播放器网页设计方案（播放列表/localStorage）与 GitHub 清单页面格式建议（旅行打包清单）。"
pubDatetime: 2025-10-15
category: "建站与技术"
kind: "长文"
tags: ["媒体播放器", "播放列表", "清单页面", "localStorage", "旅行打包"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00255-2025-10-15 本地媒体播放器网页设计方案00256-2025-10-15 GitHub清单页面格式建议

## 01 · 本地媒体播放器网页（00255）

需求：用一个本地网页播放电脑里的媒体，右侧挂一个**可隐藏的播放列表**。设计思路是左右分栏 + 响应式。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00255 · 2025-10-15</span><h3>左右分栏布局</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:170px">区域</th><th>职责</th></tr></thead><tbody><tr><td><b>左侧主播放区</b></td><td>播放器控件 + 当前播放信息；毛玻璃卡片，深色渐变背景。</td></tr><tr><td><b>右侧播放列表</b></td><td>宽 350px；可折叠——折叠时收窄到 60px，只留切换按钮；支持添加/删除本地文件。</td></tr><tr><td><b>整体</b></td><td>flex 布局、gap 20px、max-width 1400px；响应式适配不同屏幕。</td></tr></tbody></table></div><p style="font-size:13.5px;color:inherit">播放列表折叠用一个<code>.collapsed</code>类：宽度从 350px 变 60px，列表头与列表内容隐藏，只留圆形切换按钮；悬停主播放区时控制条渐显。</p></div></div>

## 02 · 本地功能集合页（00255）

同一篇笔记后半段升级为「搭一个本地网页功能集合页面」：把多个常用工具收进一个首页，卡片式入口。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00255 · 2025-10-15</span><h3>卡片式门户的设计思路</h3></div><div style="padding:14px 16px"><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>布局</dt><dd>现代化卡片式布局，每个功能模块独立展示；顶部标题 + 搜索框 + 分类按钮。</dd><dt>交互</dt><dd>视觉反馈与微动画提升体验；柔和配色；响应式适配各屏幕。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>配色</dt><dd>主色<code>#4361ee</code>系，渐变背景<code>#667eea→#764ba2</code>；卡片半透明白底。</dd><dt>注意</dt><dd>原方案外链了 Font Awesome CDN——移植到 rc 站时按「零外部依赖」改为内联 SVG，不引外部图标字体。</dd></dl></div></div></div></div>

## 03 · 在线清单登记页的六种格式（00256）

个人站`seamoonappear.github.io`想做一个在线清单登记页，先问「有哪些清单格式」。笔记列了六类格式 + 技术实现建议。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00256 · 2025-10-15</span><h3>六种清单格式</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:160px">格式</th><th>样子</th></tr></thead><tbody><tr><td><b>简单待办</b></td><td><code>- [ ] 任务</code>/<code>- [x] 已完成</code>，可带<code>@日期</code>。</td></tr><tr><td><b>表格清单</b></td><td>项目 / 状态 / 优先级 / 截止日期 / 备注。</td></tr><tr><td><b>分类卡片式</b></td><td>按「购物清单 / 学习计划」分组，组内缩进待办。</td></tr><tr><td><b>优先级矩阵</b></td><td>重要且紧急 / 重要不紧急 / 紧急不重要 三堆。</td></tr><tr><td><b>进度条格式</b></td><td><code>████████░░ 80%</code>，按阶段标绿黄红。</td></tr><tr><td><b>标签分类式</b></td><td>条目挂<code>#项目A #前端 #紧急</code>标签。</td></tr></tbody></table></div><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:14px"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>基础功能</dt><dd>增删清单项、标记完成、分类管理、优先级设置。</dd><dt>进阶功能</dt><dd>截止日期提醒、进度统计、数据导出、分享。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>技术栈</dt><dd>纯 HTML/CSS/JS 最简单；要丰富交互再上 Vue/React；本地存 LocalStorage，无需后端。</dd><dt>数据格式</dt><dd>JSON：清单数组 → 每项含 id、text、completed、priority、dueDate、tags。</dd></dl></div></div></div></div>

## 04 · 出差旅行物品清单与「自由删减」（00256）

接着做一份出门出差旅游所带物品清单，并要求**所有物品都能自由删减**，最终在根目录建`travellist/index.html`。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00256 · 2025-10-15</span><h3>六大分类与默认物品</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">分类</th><th>默认物品（按优先级）</th></tr></thead><tbody><tr><td><b>📄 证件与财务</b></td><td>护照/身份证(高)、机票/车票(高)、信用卡/银行卡(高)、现金(中)、酒店预订确认单(中)、旅行保险单(中)、驾照(低)</td></tr><tr><td><b>📱 电子产品</b></td><td>手机(高)、充电器(高)、充电宝(高)、笔记本(中)、耳机(中)、相机(低)、转换插头(中)</td></tr><tr><td><b>👕 衣物</b></td><td>内衣裤(高)、袜子(高)、上衣(高)、裤子(高)、外套(中)、睡衣(中)、泳衣(低)、鞋子(高)</td></tr><tr><td><b>🧴 洗漱用品</b></td><td>牙刷(高)、牙膏(高)、洗发水(中)、沐浴露(中)、毛巾(中)、剃须刀(低)、护肤品(低)、防晒霜(中)</td></tr><tr><td><b>💊 药品与健康</b></td><td>处方药(高)、止痛药(中)、创可贴(中)、晕车药(低)、维生素(低)、免洗洗手液(中)、口罩(中)</td></tr><tr><td><b>🎒 其他物品</b></td><td>背包(高)、水杯(中)、太阳镜(中)、雨伞(低)、书籍/电子书(低)、零食(低)、笔和笔记本(低)</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>交互与存储（照录）</h5><ul><li>勾选完成：文字划线、变灰；每个分类头部显示完成进度。</li><li>「自由删减」：每条物品可单独删除；分类卡片用<code>repeat(auto-fill,minmax(300px,1fr))</code>网格。</li><li>数据存<code>localStorage('travelChecklist')</code>：有存档就读存档，没有就用上面这份默认数据；无需后端。</li></ul></div></div></div>
