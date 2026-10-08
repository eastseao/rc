---
title: "采购管理系统 UI/GUI 优化方案"
description: "5 篇采购笔记合并——三篇同题 UI 方案去重为导航布局、配色视觉、交互组件三组对照表，优化建议分析单列（看板与各业务页专项 + V2.3.0/V3.0 路线图），附前端采购工具创意清单。"
pubDatetime: 2026-06-11
category: "建站与技术"
kind: "长文"
tags: ["分组侧栏", "莫兰迪配色", "圆角阴影", "看板升级", "V2.3.0 路线图"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00359-2025-10-30 前端采购工具创意与实现建议01285-2026-06-10 采购系统UI优化方案（基于开发者文档 V1.4 + UI 展示 V1.9.1）01286-2026-06-10 采购管理系统GUI优化方案（V1.4 架构 / V1.9.1 风格，7 个方向）01288-2026-06-10 采购管理系统UI优化方案（基于 V1.9.5，十节）01300-2026-06-11 采购管理系统优化建议分析（看板与各页面专项 + 路线图）其中 01285 / 01286 / 01288 为同题三轮对话，结论高度重叠，已按「布局 → 配色 → 交互」三个视角去重合并为前两节对照表；01300 单列第三节；00359 为系统之外的前端工具创意，作末节附录。

## 01 · 导航与布局重构（三篇同题合并）（01285 / 01286 / 01288）

三篇共同诊断出的核心痛点是：**导航信息密度低、功能分组缺失、视觉层级不清**。一致结论是——把 90px 图标侧栏扩成**200px 可折叠分组侧栏**，把十个功能按业务分四组，同时统一所有列表页的页面骨架。

| 优化项 | 01285（方案三+精炼莫兰迪） | 01286（7 方向） | 01288（V1.9.5） |
|---|---|---|---|
| **侧栏分组** | 10 功能分 4 组：仪表盘独立；采购管理 5（物料下单/报价单/合同生成/物料查询/供应商管理）；财务 3（催款记录/采购垫付/差旅报销）；工具 2（备忘录/设置），宽度 90→200px | 不重复分组，侧重交互：悬浮 scale 1.02 + 阴影过渡；右缘 4px 拖拽条调宽 155px↔46px，<80px 切纯图标紧凑模式；底部加「最近使用 3 个模块」 | 分组标题加 ▶/▼ 三角与悬停浅底 #F0E6DA；角标 [n] 改胶囊气泡（#A89080 底白字）；底部加「全部折叠/全部展开」按钮 |
| **选中指示** | 当前页左侧 3px 陶土色竖条 #C1816D + 背景高亮 | 同样保留左侧 3px 竖条 #C1816D 作视觉锚点 | 选中项高亮加 4px 宽圆角指示条；子项点击瞬间 scale 0.98 |
| **图标统一** | 合同生成 📝→📋、备忘录 📝→📌；全部导出 20×20 PNG，折叠时可辨识 | 紧凑模式 tooltip 改用 CTkToolTip，延迟 0.5s 出现 | 统一 Feather 风格 1.5px 线宽、20×20 区域；未选中 #8F7A63、选中 #C1816D |
| **页面骨架** | 每页统一：标题+面包屑 \| 操作栏 → 统计卡片+筛选 → Treeview 数据表格 → 底部固定「导出/导入/新增」 | 所有列表/表单收进 CTkFrame 卡片（corner_radius=16），内边距上下 20px、左右 24px，卡片间距 16px | 渐进分层：主操作区大卡片 18px 粗体标题；次要区浅背景 #F5F0EB、圆角 10px、标题 14px |
| **重点页改造** | 合同生成分三步向导（合同信息→供应商→产品明细），右侧窄预览栏，每步自动存草稿到本地 JSON；顶部加 Ctrl+K 全局搜索（SQLite LIKE / fts5） | 表单改标签-控件同行两列网格（标签宽 100px）；必填前加红 *（#B56A6A），未填边框变红+抖动 | 表格整行可点击进详情；表头 ↑↓ 排序指示，>500 行显示 loading |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">01285 的三阶段实施路径</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>第一阶段</dt><dd>导航栏重构 + 视觉微调：200px 分组侧栏、图标统一、圆角/字体调整，每阶段 1-2 周，2 周内出 V1.10 尝鲜版。</dd><dt>第二阶段</dt><dd>页面布局统一 + 交互增强：统一卡片+表格结构、合同分步向导、表格排序与悬浮行高亮。</dd><dt>第三阶段</dt><dd>高级功能（可选）：全局搜索框、仪表盘迷你趋势图、深/浅色主题切换。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">01285 为什么淘汰其他导航方案</h3><div style="overflow-x:auto;margin:16px 0;margin-bottom:0"><table><thead><tr><th>被淘汰方案</th><th>原因</th></tr></thead><tbody><tr><td>折叠侧边栏（方案一）</td><td>未解决分组问题，信息仍混乱，治标不治本</td></tr><tr><td>顶部标签（方案二）</td><td>10+ 标签需溢出菜单，操作不便</td></tr><tr><td>图标+浮层（方案四）</td><td>实现复杂，CustomTkinter 浮层体验差</td></tr><tr><td>混合双栏（方案五）</td><td>过度设计，学习成本高，当前功能量无需</td></tr><tr><td>全新蓝色主题</td><td>改变用户习惯，需维护两套主题，留作后续可选</td></tr></tbody></table></div></div></div>

## 02 · 配色与视觉规范（三篇同题合并）（莫兰迪暖色微调）

三篇都主张**保留现有莫兰迪暖色调、不推倒重来**，只做圆角、阴影、字体、间距、功能色五项系统化微调。下表把三篇的具体取值对照列出，同一组件不同笔记给的数值并列照录。

| 维度 | 建议取值（照录各笔记） | 来源 |
|---|---|---|
| **圆角体系** | 01285：卡片 10→12px、按钮/输入框 6→8px、弹窗 0→16px。<br> | 01285 / 01288 |
| **阴影分层** | 01285：单层阴影改三层叠加（CustomTkinter 不支持直接阴影，用 border_color #E8DDD0 + fg_color #FFFAF5 模拟）。<br> | 01285 / 01288 |
| **字体字号** | 01285：正文 11pt→13pt（微软雅黑）；导航按钮高 44px（图标 24 + 文字 20）。<br> | 01285 / 01286 / 01288 |
| **间距节奏** | 01285：页面边距 32px、模块间距 24px。<br> | 01285 / 01288 |
| **配色微调** | 01288 对照表：侧边栏背景 #F5F0EB→#F3EDE6（更中性）；主内容区 #FFFAF5→#FEF9F2（提高与白卡对比）；高亮色 #C1816D→#D4917A（略增饱和）；新增成功 #5B9279、警告 #E4A36A。<br> | 01288 / 01286 |
| **深色模式** | 01286：莫兰迪深色——主背景 #2A2420、卡片 #3A322C、文字 #E6DED5。<br> | 01286 / 01288 |
| **仪表盘图表** | 01286：柱状图（近 6 个月下单金额）+ 饼图（各模块占比），配色取 #C1816D / #8FA882 / #C9A96E，去网格线、背景透明 | 01286 |

> **表格既有好设计，保持不动**（01285）：现有选中色 #E8D5C4、文字色 #4A3728 效果良好，无需修改；仅补充鼠标悬浮行背景 #E8DDD0，表头加 ▲/▼ 排序箭头。

## 03 · 交互与组件建议（三篇同题合并）（表格 / 表单 / 反馈 / 看板）

把三篇在「表格交互、表单效率、操作反馈、仪表盘增强」上的重合建议合并去重：哪些三篇都提、哪些是单篇独有，一表看清。

| 组件域 | 建议内容（照录） | 来源 |
|---|---|---|
| **表格行交互** | 行高加到 36px；悬浮行变色（#FDF2EE 或 #FFF2E6 或 #E8DDD0，三篇各给一色）；整行可点击、鼠标手型；行首加「···」操作按钮防误触；固定首列用双 Treeview 滚动同步模拟 | 01286 / 01288 / 01285 |
| **表头排序** | 右侧 ↑↓ 图标，点击排序并高亮方向；数据量 >500 时排序显示短暂 loading | 01286 / 01288 / 01285 |
| **列宽** | 允许拖拽调列宽并写入 settings.txt 下次恢复；默认列宽按内容分配（文本 200px、数字 100px、日期 120px） | 01288 / 01286 |
| **表单输入** | 必填前红 * + 提交时边框红/抖动提示；合同编号、供应商名等 Combobox 自动补全历史记录；金额失焦自动千分位格式化 | 01286 |
| **操作反馈** | 成功导出/保存不再用 messagebox，改右下角非模态 Toast（3 秒自动消失、可堆叠、随类型变色半透明滑入）；加载超 300ms 显示骨架屏 + CTkProgressBar（indeterminate） | 01286 / 01288 |
| **窗口行为** | 记录上次窗口大小、位置、侧栏宽度、表格列宽并存 settings.txt，启动恢复 | 01286 |
| **看板 KPI 卡** | 卡片统一 280×100；右上角趋势标签改 Sparkline 迷你折线；环比改色块箭头（绿升 / 红降 / 灰平）；底部加微进度条；悬停上浮 y_offset=-2 + 阴影 | 01288 / 01286 |
| **看板待办** | 待办聚合条默认折叠为「📋 你有 3 项待办」横幅，展开后每条左侧加紧急程度色块（红/橙/蓝），「前往处理」改圆角胶囊按钮 | 01288 |
| **看板动态流** | 左侧时间轴圆点（新增=绿、修改=蓝、删除=红）；超过 5 条底部「查看更多」链接弹模态框 | 01288 |
| **时间筛选** | 仪表盘顶部加日期范围选择器（本周/本月/自定义），CTkSegmentedButton 切换、默认「本月」，所有卡片联动 | 01286 |
| **页面动效** | 页面切换淡入淡出；侧栏折叠用 after 循环每 10ms 增减 5px 做平滑动画 | 01286 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">01286 优先级表（V1.5 先落实高项）</h3><div style="overflow-x:auto;margin:16px 0;margin-bottom:0"><table><thead><tr><th>优先级</th><th>优化点</th><th>工作量</th></tr></thead><tbody><tr><td>高</td><td>表格行高、悬浮效果</td><td>1h</td></tr><tr><td>高</td><td>必填标记 + 表单同行布局</td><td>2-3h</td></tr><tr><td>高</td><td>非模态通知</td><td>1-2h</td></tr><tr><td>中</td><td>窗口状态持久化 / 仪表盘图表与趋势</td><td>1h / 2h</td></tr><tr><td>中</td><td>深色模式</td><td>3-4h</td></tr><tr><td>低</td><td>侧边栏拖拽 / 页面淡入淡出</td><td>2h / 4h</td></tr></tbody></table></div></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">01288 优先级表（V1.9.5 起）</h3><div style="overflow-x:auto;margin:16px 0;margin-bottom:0"><table><thead><tr><th>优先级</th><th>优化项</th><th>工作量</th></tr></thead><tbody><tr><td>P0</td><td>圆角统一 + 阴影分层</td><td>2h</td></tr><tr><td>P0</td><td>表格行悬浮与排序指示器</td><td>4h</td></tr><tr><td>P1</td><td>分组三角 + 胶囊角标 / 待办折叠化 / 字体间距系统化</td><td>1-2h</td></tr><tr><td>P2</td><td>KPI 卡片迷你趋势图 / 暗色模式基础架构</td><td>3h / 8h</td></tr><tr><td>P3</td><td>交互式图表（Plotly）</td><td>6h</td></tr></tbody></table></div></div></div>

## 04 · 优化建议分析：看板与各页面专项（01300 · 2026-06-11）

这篇不再谈配色，而是站在「看板 + 各业务页面 + 架构性能」三个层面，按高/中/低优先级给出可落地清单，并收敛出 V2.3.0 优先 5 项与 V3.0 智能化路线图。

<details open><summary>看板页面（Dashboard）优化<span>高/中/低三档</span></summary><div><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:90px">优先级</th><th style="width:230px">优化点</th><th>说明</th></tr></thead><tbody><tr><td><b>高</b></td><td>动态流点击跳转详情</td><td>每条动态按类型+记录 ID 打开对应页面并定位，目前仅静态文字、需人工查找</td></tr><tr><td><b>高</b></td><td>待办一键完成 / 延后</td><td>聚合条内直接「✔ 完成」「⏱ 延后 1 天」，免跳转</td></tr><tr><td><b>高</b></td><td>KPI 卡片自定义指标</td><td>设置页从预设列表（下单/催款/垫付/差旅/合同/比价/报价）勾选 4 个，2×2 网格动态生成</td></tr><tr><td>中</td><td>动态流类型筛选</td><td>顶部胶囊按钮按类型过滤（如只看催款）</td></tr><tr><td>中</td><td>趋势图悬停提示</td><td>Canvas 折线绑定事件，悬停显示月份与数值，或用文字「近 6 月：+12%, -3%, +5%」替代</td></tr><tr><td>中</td><td>待办按紧急度排序</td><td>紧急红 / 一般橙 / 普通蓝，今天到期置顶</td></tr><tr><td>低</td><td>仅看未读模式 / 同比数据</td><td>记录上次查看时间标记未读；系统满一年后补同比</td></tr></tbody></table></div></div></details>

<details><summary>通用优化（适用大多数页面）<span>高频复用</span></summary><div><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:90px">优先级</th><th style="width:220px">优化点</th><th>适用页面</th></tr></thead><tbody><tr><td><b>高</b></td><td>统一快速筛选条（关键词 + 日期范围 + 状态下拉），封装为 FilterBar 组件全页复用</td><td>物料下单/催款/垫付/差旅/备忘录/合同/BOM 等列表页</td></tr><tr><td><b>高</b></td><td>列宽拖动并记忆到 settings.txt</td><td>所有含 Treeview 页面</td></tr><tr><td><b>高</b></td><td>导出当前筛选视图为 Excel（字段与表格列一致）</td><td>所有列表页</td></tr><tr><td>中</td><td>批量操作：行首复选框多选后批量删除/归档/改状态</td><td>物料下单/供应商/催款/垫付/备忘录</td></tr><tr><td>中</td><td>字段合法性校验 + 未填高亮 Tooltip</td><td>所有表单页</td></tr><tr><td>中</td><td>长表单每 30 秒自动存草稿</td><td>物料下单（22 字段）/报价单/合同生成</td></tr><tr><td>低</td><td>快捷键 Ctrl+S 保存 / Ctrl+F 搜索 / Ctrl+E 导出；表格行右键上下文菜单</td><td>全局 / 所有表格页</td></tr></tbody></table></div></div></details>

<details><summary>九个业务页面专项清单<span>点到点改造</span></summary><div><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">页面</th><th>高优先改造</th><th>中低优先补充</th></tr></thead><tbody><tr><td><b>物料下单</b></td><td>顶部生命周期步骤条（比价→签批→通知→生产→发货→入库→完成）按字段自动高亮；一键复制相似订单</td><td>物流单号接快递 100 查轨迹；预计到达临近在动态流提醒并整行高亮</td></tr><tr><td><b>报价单生成</b></td><td>产品库支持 Excel 批量导入（含阶梯价）</td><td>生成前内嵌表格预览；历史报价「再次使用」一键回填</td></tr><tr><td><b>三方比价</b></td><td>按输入数量自动算三家阶梯总价，绿色高亮最低价供应商并打「推荐」标签</td><td>同物料历次比价价格曲线；导出比价报告（PDF 需评估 reportlab 打包体积）</td></tr><tr><td><b>合同生成</b></td><td>支持上传自定义 .docx 模板并映射占位符（类似邮件合并）；合同编号按年份+供应商缩写+顺序号自动生成保唯一</td><td>有效期字段到期前 30 天在动态流提醒、列表高亮</td></tr><tr><td><b>台账查询</b></td><td>AND/OR 多条件高级筛选（如：供应商=A 且金额&gt;10000 或物料名含「包材」）</td><td>按供应商/品类透视汇总出柱状图；Excel 导入自动识别列头、允许手动映射</td></tr><tr><td><b>BOM 管理</b></td><td>Treeview 树形展示多层子 BOM，支持展开/折叠全部</td><td>按最近采购价累加成品成本；BOM 多版本（V1.0/V2.0）切换与差异比较</td></tr><tr><td><b>催款记录</b></td><td>按应付款日期自动着色：逾期 &gt;30 天标红、7 天内标橙</td><td>一键唤起邮件客户端发催款函（预填收件人/主题/正文）；同供应商催收历史时间线</td></tr><tr><td><b>垫付 &amp; 差旅</b></td><td>批量勾选一键「已报销」</td><td>发票/收据图片存 attachments/ 目录并在列表打图标；按标准报销单格式导 PDF</td></tr><tr><td><b>备忘录</b></td><td>截止时间到点发系统桌面通知（plyer / win10toast + 后台轮询）</td><td>每日/每周周期性备忘自动生成下一截止日；可关联到订单/供应商并跳转</td></tr><tr><td><b>厂家 &amp; 设置</b></td><td>设置页一键备份（zip 打包 procurement.db）与恢复；厂家页 0-5 星评分字段</td><td>供应商联系人拆子表（采购/财务/技术多人）；日志自动轮转保留最近 30 天；界面布局一键重置</td></tr></tbody></table></div></div></details>

<details><summary>架构性能与 V2.3.0 / V3.0 路线图<span>下一版本怎么排</span></summary><div><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:170px">方向</th><th>要点</th></tr></thead><tbody><tr><td><b>异步加载分页</b></td><td>台账超 1 万行用 threading 加载、每页 100 行分页，避免一次性全量卡死</td></tr><tr><td><b>数据库运维</b></td><td>启动迁移加版本标记，只在版本变化时跑 _migrate_tables；每天凌晨自动备份保留最近 7 份；操作写 audit_log 审计表</td></tr><tr><td><b>V2.3.0 优先 5 项</b></td><td>①动态流可点击跳详情 ②列表统一快速筛选栏+列宽记忆 ③物料下单生命周期流程图 ④数据备份/恢复 ⑤大表异步加载+分页</td></tr><tr><td><b>V3.0 智能化</b></td><td>按历史价/准时率/评分智能推荐供应商；移动平均做 1-3 个月需求预测；录入单价超该物料近 6 次均价 ±20% 自动弹窗记录原因</td></tr><tr><td><b>V3.0 自动化</b></td><td>后台定时任务按「通知日期/预计交期/发货日期」自动流转合同状态；逾期 &gt;30 天应付自动生成催款待办；Excel 导入用 difflib 模糊匹配列头</td></tr><tr><td><b>V3.0 报表与延伸</b></td><td>独立报表中心（月度采购堆积面积图/准时率 Top10/待报销折线/采购频次 Top20 词云）；Flask 只读查询端 + 邮件/企业微信 Webhook 通知 + 二维码扫码录入</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:14px;margin-bottom:0"><b>系统背景（照录）</b>：「采购助手」桌面管理系统 V2.2.0，技术栈 Python 3.12 + CustomTkinter + SQLite，作者王维（EastSeaO），北京同仁堂健康药业（青海）有限公司采购部，已在部门实际运行；功能覆盖物料下单、报价比价、合同生成、垫付报销、催款台账等核心环节。</div></div></details>

## 05 · 附录：前端采购工具创意清单（00359 · 2025-10-30）

这篇是更早的一份「采购 + 前端」跨界工具构想，按「流程效率 → 数据决策 → 小工具」三档列出八类可独立做的小工具，技术栈与起步建议一并照录。

| 工具 | 做什么 | 技术亮点 |
|---|---|---|
| **采购比价助手 / 价格看板** | 一表录入各供应商报价/税率/运费，自动算含税总价与单价并高亮最优，柱状图对比，导出 PDF/Excel | React Table / Handsontable、ECharts / Chart.js、文件导出 |
| **供应商信息管理中心** | 卡片化展示联系人/主营品类/信用等级/最近交易，按品类地区信用筛选，一键发邮件或复制联系方式 | 组件化 + 状态管理 + LocalStorage |
| **采购需求收集器** | 生成标准链接/二维码发内部同事填需求，看板实时汇总，提交人可看自己需求状态（待处理/已询价/已下单） | Formik / React Hook Form、WebSocket 或轮询、二维码生成 |
| **支出分析仪表盘** | 上传 Excel 采购记录，出月度/季度趋势、品类占比饼图、供应商排名，点击图表联动筛选 | D3.js / AntV G2、文件解析 |
| **合同/订单到期提醒器** | 录入合同与长单到期日，自动算剩余天数按颜色预警，配日历视图 | Day.js / date-fns、日历组件、桌面通知 |
| **单位换算与税率计算器** | 货币换算、件↔箱换算、含税/不含税价互算 | 实时计算 |
| **采购模板生成器** | 询价单（RFQ）/合同标准模板在线填字段，一键生成规范 Word/PDF | docx.js / pdf-lib |
| **采购术语与 SOP 知识库** | 静态站整理专业术语与标准流程，支持搜索，自用或培训新人 | VitePress / Docusaurus + Markdown |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">怎么起步</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>选题目</dt><dd>回想工作中最重复、最耗时、最头疼的任务，作为第一个项目。</dd><dt>MVP 原则</dt><dd>先做核心功能可用的简单版本（如本地比价表格），再逐步加数据持久化。</dd><dt>展示跨界</dt><dd>说明工具解决了采购哪个具体问题，按采购员操作习惯做界面，发布到 GitHub / 个人博客。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">技术栈推荐</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>框架</dt><dd>React（生态丰富）/ Vue（易上手）/ Solid.js（性能好）</dd><dt>UI 库</dt><dd>Ant Design、Chakra UI、Element Plus 等，快速搭专业界面</dd><dt>构建</dt><dd>Vite，开发体验佳</dd><dt>推荐起点</dt><dd><b>采购比价助手</b>：目标明确、能串联表单/表格/计算/图表/导出，做完立刻能用</dd></dl></div></div>
