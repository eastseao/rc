---
title: "采购工具与桌面应用"
description: "四款采购工具笔记——本地供应商管理系统三方案对照、「采购物流通」桌面应用功能与归档规则、采购单按类别归类合并规则、采购账本 APP 垫资与差旅功能优化点。"
pubDatetime: 2026-06-04
category: "建站与技术"
kind: "工具"
tags: ["本地 SRM 选型", "流程勾选表", "采购单归类", "垫资报销", "发票管理"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00779-2026-03-22 本地供应商管理系统推荐01260-2026-06-04 采购物流通桌面应用01262-2026-06-04 采购单按类别归类合并01264-2026-06-04 采购账本APP功能优化

## 01 · 本地供应商管理系统推荐对照（00779 · 2026-03-22）

「本地」的含义是把系统装在公司服务器或自己可控的电脑上、数据掌握在自己手里。按企业规模与技术能力，笔记给出三档方案，从免费单机到大型定制排列。

| 推荐系统 | 定位与部署 | 适合企业 / IT 要求 | 核心优势 |
|---|---|---|---|
| **百卓优采** | 轻量免费单机：直接下载 exe 安装包装在个人办公电脑，安装包约 28.9MB | 中小微企业、采购 3-5 人；**无 IT 要求**，下载即用 | 完全免费，上手极快；功能覆盖请购、询价、下单到收付款全流程；数据就在本机 |
| **索谷 SRM** | 专业供应商关系管理：部署在公司内部服务器，员工用办公电脑经网络访问 | 有深度供应商管理需求的中型企业；**需要专人**维护服务器与系统 | 专注供应商协同（订单/送货/品质在线协同），永久授权、一次付费长期使用 |
| **数商云等** | 大型定制化采购平台：部署在公司自有数据中心或云服务器 | 大型集团、对数据安全要求极高的企业；**要求高**，需专业 IT 运维团队 | 可量身定制，与内部 ERP/WMS 无缝集成，数据完全自主可控 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">三个自问怎么选</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>预算</dt><dd>预算有限 → 百卓优采免费起步；预算充足求稳定 → 索谷 SRM 永久授权。</dd><dt>IT 能力</dt><dd>没有 IT 人员 → 百卓优采；有专业运维团队 → 数商云这类大型系统。</dd><dt>核心需求</dt><dd>告别 Excel 管供应商 → 百卓优采够用；要管招标/合同/绩效深度协同 → 索谷 SRM；要对接 ERP、流程复杂 → 数商云定制。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">「电脑端」的两种形态</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>单机版</dt><dd>软件和数据都装在办公电脑上（如百卓优采），换台电脑看不到数据，适合个人或小团队。</dd><dt>服务器-客户端版</dt><dd>系统装在公司服务器、数据集中存放（如索谷 SRM / 数商云），多人协作更安全方便。</dd></dl></div></div>

## 02 · 「采购物流通」桌面应用功能（01260 · 2026-06-04）

这是一个纯前端单页应用：把代码存成 .html 文件、用浏览器打开即可用，数据存浏览器 localStorage，无需安装与后端。核心是一行物料 + 一串环节勾选框，跟踪从比价到归档的全流程。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">新增物料：五个必填字段</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>必填五项</dt><dd>物料名称、项目号、厂家、型号、单位——缺任一项不允许添加，提示「请完整填写」。</dd><dt>流程环节</dt><dd>每行七列勾选框：比价 → 合同 → 通知厂家 → 生产 → 发货 → 到货 → 归档。</dd><dt>统计</dt><dd>底部实时显示「N 条物料（已归档 M 项）」。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">归档联动规则</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>启用前提</dt><dd>只有「到货」勾选后，「归档」框才可用。</dd><dt>归档锁定</dt><dd>归档后整行灰化加删除线，所有环节勾选框禁用，仅可删除或「取消归档」；基础信息也不可编辑。</dd><dt>反向约束</dt><dd>到货取消勾选时，若已归档则自动取消归档（兜底再校验一次）。</dd></dl></div></div>

> **上手三步（照录）**
> - 把完整代码复制保存为**采购物流通.html**（注意扩展名是 .html 而非 .txt）。
> - 双击用 Chrome / Edge / Firefox 打开；顶部填五个字段点「+ 添加物料」。
> - 按实际进度逐行打勾，到货后勾归档；所有记录自动存浏览器本地，关闭重开不丢失。

## 03 · 采购单按类别归类合并规则（01262 · 2026-06-04）

面对几百行混合采购单，目标是「按类别拆表、同名合并、数量累加、原序号全保留」。规则本身不难，坑全在「规格是否相同」的判定上。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>合并四步规则</span><h3>怎么归、怎么并</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:120px">步骤</th><th>做法</th></tr></thead><tbody><tr><td><b>① 按类别分组</b></td><td>以采购单「类别」列为准，每个类别拆成独立表格。原单共拆出 11 类：原料、PET、标签、PE袋、卡盒、复合膜、珍珠棉、铝碗、勺子、封口贴、50ml玻璃瓶。</td></tr><tr><td><b>② 定合并键</b></td><td>组内以「名称 + 规格」作为唯一键；<b>规格不同不合并</b>（如同名 PET 直筒罐 85*180，250克 / 200克 / 150克 分别成行）。</td></tr><tr><td><b>③ 数量累加</b></td><td>同一键的数量直接相加，单位统一（如 kg 小写）。</td></tr><tr><td><b>④ 列原序号</b></td><td>序号列把所有来源行按原顺序列出（如 A81, A92, A106…），便于反向追溯到原始采购单。</td></tr></tbody></table></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>照录示例</span><h3>合并与「不合并」的真实例子</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0;margin-bottom:14px"><table><thead><tr><th style="width:200px">例子</th><th>处理结果</th></tr></thead><tbody><tr><td>塑料小罐（A62, A67, B35 三行）</td><td>规格均为「/」，合并为一个键：91800 + 51000 + 84000 =<b>226800 个</b></td></tr><tr><td>PET 白罐 95*181 套装（A81 等 8 行）</td><td>规格一致，合并 5100×8 =<b>40800 套</b></td></tr><tr><td>50ml 玻璃瓶含盖（C18, C43, C66）</td><td>规格一致，合并 51000×3 =<b>153000 个</b></td></tr><tr><td>杏仁七白粉标签（A82 = 350克 / B60 = 规格「/」）</td><td><b>规格不一致，不合并</b>，两行分别列出</td></tr><tr><td>梯形袋 81019955（A44 与 A58 都是 200克）</td><td>同规格但当时分行列出，若需可累加为 8200 个——实际采购前再确认</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>口径提醒（照录）</b>：原始数据中部分同名物料规格字段写法不一（如「/」与具体克数混用），同名不同规格时已分别列出；正式采购前建议按实物规格再核对一遍，避免把不同克重的罐子并成一行。</div></div></div>

## 04 · 采购账本 APP 功能优化点（01264 · 2026-06-04）

原构想只有两页：一页记日常物料垫资、一页记差旅花费。优化思路是把「记事本」升级成「垫付—开票—报销—分析」闭环：字段补全、记录分层、再加五个增强模块。

<details open><summary>第 1 页：日常物料垫资 —— 升级为完整采购流水<span>字段补全</span></summary><div><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:140px">字段组</th><th>优化点</th></tr></thead><tbody><tr><td><b>基础信息</b></td><td>垫资日期（支持选今天/昨天）；物资明细支持多行，每行填名称/规格型号/数量/单价，<b>系统自动算总额</b>；用途/项目归属做成预设列表（A 项目研发、行政办公等）一键选择，便于按项目核算</td></tr><tr><td><b>支付与票据</b></td><td>支付平台保留（微信/支付宝/银行卡/现金），加支付账号/卡号便于对银行流水；「是否开票」升级为状态机：<b>未开票 → 已开票 → 发票已收到/已上交</b>，点「已开票」可拍照发票、填发票号与金额</td></tr><tr><td><b>附件与经手人</b></td><td>小票/收据/合同拍照存档作垫资凭证；多人垫资时记录经手人/采购人</td></tr></tbody></table></div></div></details>

<details><summary>第 2 页：差旅花费 —— 改「行程-明细」二级结构<span>父子两层</span></summary><div><p style="margin-bottom:12px">不再把一次出差的交通住宿混在一行，而是先建一个「出差行程」（父级），再在行程下按天或按类别加明细（子级），每笔明细有独立开票状态。</p><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">父级：出差行程</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>基本信息</dt><dd>出差事由、目的地（可多选城市）、起止日期——系统自动算出差时长。</dd><dt>汇总看板</dt><dd>进入行程即显示已花总额、已开票金额、未开票金额。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">子级：费用明细</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>交通</dt><dd>工具类型（飞机/火车/汽车/出租网约车/公交）、航班或车次、起止地、金额；独立标记是否已拿行程单/发票。</dd><dt>酒店</dt><dd>酒店名称、入住/退房日期、房间数、金额；标注专票/普票。</dd><dt>其他</dt><dd>餐饮宴请、会务费、材料费等杂项，同样记金额与开票状态。</dd></dl></div></div></div></details>

<details open><summary>五个增强模块 + 建议的底部导航<span>闭环</span></summary><div><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:160px">增强模块</th><th>做什么</th></tr></thead><tbody><tr><td><b>扫发票自动填</b></td><td>摄像头扫发票二维码，自动识别发票号/金额/抬头/税号并匹配到对应垫资记录；自动查重，防同一张票重复提交</td></tr><tr><td><b>一键生成报销单</b></td><td>勾选多条已完结记录，按项目与费用类别自动归集，导出 PDF 或直接分享，带全部发票影像</td></tr><tr><td><b>首页驾驶舱</b></td><td>打开 APP 先看汇总：待报销总额、未回款；待办提醒（超期未开票、已报销未到款）；大号「+」提供「记一笔采购 / 记一次出差」</td></tr><tr><td><b>多维统计</b></td><td>采购看板按供应商/品类/项目看花费分布；差旅看板看项目差旅成本与个人出差趋势；支持导出 Excel</td></tr><tr><td><b>预算预警（进阶）</b></td><td>为项目或月度差旅设预算阈值，接近阈值自动提醒</td></tr></tbody></table></div><p style="margin-top:14px">建议底部导航收为<b>4 个 Tab</b>：首页（驾驶舱）/ 账本（全部记录列表与筛选）/ 发票（独立发票管理中心，按状态分类、扫码录入）/ 我的（项目部门、支付账户、导出数据）。</p></div></details>
