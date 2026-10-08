---
title: "供应商寻源技能与调研维度"
description: "4 篇采购笔记合并：寻源/查找供应商 SKILL 设计要点，原料信息五大维度清单，网络检索七个背调维度与交叉验证流程。"
pubDatetime: 2026-04-21
category: "采购与供应链"
kind: "长文"
tags: ["供应商寻源", "SKILL 设计", "原料调研", "网络背调", "交叉验证"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00938-2026-04-15 供应商寻源技能设计（FindSupplier）00939-2026-04-15 设计供应商查找 SKILL（OpenClaw supplier-finder）00991-2026-04-21 供应商原料信息维度00992-2026-04-21 供应商网络检索维度

## 01 · 寻源与查找供应商 SKILL 设计要点（00938 / 00939）

两份笔记分别给了一个“轻量对话式寻源技能（FindSupplier）”和一个“OpenClaw 规范的 supplier-finder SKILL”。前者重流程与输出字段，后者重文件结构、参数与脚本化筛选，可互补使用。

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">FindSupplier 四步执行流程（00938）</h3><p style="margin-bottom:12px">用户按“产品/物料 — 供应商类型 — 目标地区 — 额外要求”发指令，技能依次跑四步：</p><div style="overflow-x:auto;margin:16px 0;margin-bottom:0"><table><thead><tr><th style="width:150px">步骤</th><th>要点</th></tr></thead><tbody><tr><td><b>第一步 需求解析</b></td><td>提取<span>product</span>（品名/规格）、<span>supplier_type</span>（原料/包装）、<span>location</span>（省/市/国家/经济区）、<span>extra_criteria</span>（认证、产能、MOQ 等）。</td></tr><tr><td><b>第二步 数据检索</b></td><td>数据源：公开商业目录（Alibaba、1688、ThomasNet、欧洲黄页）、行业协会数据库（中国包装联合会、食品配料协会）、政府/海关数据（企业注册、出口商名录）、企业官网与地图（百度/高德搜“XX 包装厂”+地区）。有联网则实时搜索，无联网则给结构化搜索方法与示例结果。</td></tr><tr><td><b>第三步 信息提取与验证</b></td><td>每家至少取：公司全称、所在地（详细到区县）、主营产品/服务、联系方式（电话/邮箱/官网至少两种）、资质摘要（ISO/FDA/QS 等）、备注（MOQ、产能、典型客户）。</td></tr><tr><td><b>第四步 输出格式</b></td><td>以表格/列表返回，每家含名称、地址、联系人/部门、电话、邮箱、官网、资质、匹配说明、数据来源、最后核实时间；若需对比可加“推荐指数”（⭐~⭐⭐⭐⭐⭐）。</td></tr></tbody></table></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">OpenClaw supplier-finder 文件结构与参数（00939）</h3><p style="margin-bottom:12px">严格按 SKILL 文件规则组织：<span>SKILL.md</span>（YAML frontmatter + 正文）、<span>scripts/search_suppliers.py</span>（筛选脚本）、<span>data/suppliers_sample.json</span>（示例数据库）。</p><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>触发条件</dt><dd>消息含“找供应商/找厂家/采购/哪里可以买”“原料/包装/材料供应商”并伴随地区名，或问“联系方式/联系电话/地址”。</dd><dt>参数 location</dt><dd>必填，支持城市名（深圳）或省份/区域（广东、华东）。</dd><dt>参数 material_type</dt><dd>选填，<span>raw</span>（原料）或<span>packaging</span>（包装），不指定返回全部。</dd><dt>参数 keyword</dt><dd>选填，进一步筛选关键词（塑料、纸箱、金属等）。</dd></dl></div><div><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>执行指令</dt><dd><span>python3 scripts/search_suppliers.py --location &quot;{{location}}&quot; --material-type &quot;{{material_type}}&quot; --keyword &quot;{{keyword}}&quot;</span></dd><dt>脚本筛选逻辑</dt><dd>地区三级匹配（城市/省份/区域）+ 区域映射表（珠三角/长三角/成渝/京津冀/华东等）双向模糊；再按 material_type 与 keyword（在名称、分类、主营产品中）过滤。</dd><dt>输出 JSON</dt><dd>含 status、location、count、suppliers[]；每家 name/type/category/address/contact{phone,mobile,email,website}/main_products/region。</dd><dt>设计要点</dt><dd>渐进式信息披露（description 常驻、正文触发后加载）；数据用 JSON 可随时扩充；可与 write_file（导出 CSV/Excel）、browser（看官网）、email（发询价）配合。</dd></dl></div></div></div>

> **技能边界与免责（照录）**
> - 信息来源于公开渠道或模拟检索，不保证实时准确性；实际交易前应自行核实供应商资质、信用与产品质量。
> - 用户未指定地区时需主动询问；返回结果过多时建议加关键词缩小范围。

## 02 · 原料信息五大维度清单（00991）

了解一家供应商的原料信息，按五大维度逐项问，再配一套采购注意事项。下表把每个维度要了解的具体内容照录成清单。

| 维度 | 需要了解的具体内容 |
|---|---|
| **1. 基础规格与理化指标** | 产品名称、CAS 号、执行标准（国标/行标/企标）；关键指标：纯度、含量、水分、粒度、pH 值、杂质限量（重金属、溶剂残留）；物理性质：外观、密度、粘度、熔点等。 |
| **2. 质量与食品安全** | 质量等级：工业级/食品级/药品级（是否需 GMP）；食品安全：是否符合 GB 2760、GB 2762 等，有无农残、兽残、真菌毒素、致敏原信息；检测报告：出厂检验报告、第三方型式检验报告（如 SGS、华测）。 |
| **3. 合规与资质证明** | 供应商资质：营业执照、生产许可证（如 SC）、经营许可证；原料专属证明：MSDS（物质安全数据表）、COA（分析证书）、TDS（产品技术说明书）；认证：ISO 9001、ISO 22000、HACCP、有机认证、非转基因证明、Kosher/Halal 等。 |
| **4. 供应与批次管理** | 产地：原料天然来源地或生产工厂位置；批次信息：批次编号规则、生产日期、保质期、存储条件；供应稳定性：年产量、库存水平、备选产地或替代原料方案。 |
| **5. 应用与风险数据** | 工艺适应性：溶解性、热稳定性、与其他原料的配伍性；风险物质：是否含塑化剂、三聚氰胺等非法添加物；环境影响：是否濒危物种（如某些中药材）、碳足迹数据。 |

#### 采购注意事项（实操指南）

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>样品与文件先行</dt><dd>正式下单前索要至少 2-3 个小样（最好来自不同批次）内部检测/试用；要求盖公章的最新版营业执照、生产许可证、COA、MSDS，并核对 COA 批号与样品是否一致。</dd><dt>合同与技术协议</dt><dd>把双方确认的关键指标及检测方法作为合同附件，写明具体标准号与指标值（如纯度≥99.5%，按 HPLC 法），避免“符合国家标准”这类模糊描述；约定验收期限（如 7 天）、不合格品处理方式与双方认可的第三方复检机构；约定保质期及因原料质量导致成品受损的赔偿责任。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>实地审核与监控</dt><dd>首次合作建议现场审核，看生产卫生、仓储温湿度与防虫鼠、检验实验室能力；每批到货留样密封保存（至少 1 个保质期+6 个月）；每半年或一年重新评估供货质量稳定性、价格变化与配合度。</dd><dt>特殊风险防范</dt><dd>进口原料核查海关报关单、检疫证明、原产地证明；易掺假原料（香精香料、植物提取物）增加指纹图谱或特征标志物检测条款；尽量开发备选供应商，防止单一来源断供/涨价。</dd><dt>法规红线</dt><dd>确认原料不含目标市场（中国、欧盟、美国等）禁用成分；宣传“有机/天然/无转基因”必须提供对应认证证书或检测报告。</dd></dl></div></div>

##### 快速核查 · 拿到资料先问这 6 个问题

COA 批号一致？证照范围覆盖？指标写进合同？产地/风险/存储清楚？首次合作做过审核？断供有无备选？

① COA 上批号和实际送样一致吗、是否盖公章？② 原料生产许可证范围是否覆盖该原料？③ 双方约定的关键指标和检测方法写进合同了吗？④ 是否了解原料产地、主要风险杂质和存储要求？⑤ 第一次合作安排过现场或视频审核吗？⑥ 如果这个原料断供，我们有备选方案吗？

## 03 · 网络检索供应商七个背调维度（00992）

在网络里检索供应商，为避免信息不对称，按七个维度做深度“背调”，每个维度都附检索动作与判断指标。

| 维度（判断什么） | 检索动作 | 关键指标 |
|---|---|---|
| **1. 基础工商与合规性**<br> | 国家企业信用信息公示系统，或天眼查/企查查 | 存续状态（是否在营、有无吊销注销风险）；注册资金与实缴资本（实缴更能体现资金实力）；司法风险（作为被告的买卖合同纠纷、失信被执行记录）；行政处罚（产品质量、环保、税务）。 |
| **2. 产品与供应能力**<br> | 阿里巴巴 1688、慧聪网等行业 B2B 平台搜其店铺 | 核心产品参数与认证（CE、UL、RoHS）；起订量 MOQ 与交付周期是否匹配采购规模；样品与定制能力；产能证明（工厂面积、产线数量、年产值，可从官网/宣传册推断）。 |
| **3. 财务健康与交易信用**<br> | 企业征信报告（部分付费），搜“企业名+拖欠货款/赖账” | 历史付款记录是否按时（反映现金流）；对外投资与负债是否过度扩张/高负债；纳税等级 A/B/M 级较健康、D 级需警惕。 |
| **4. 行业口碑与客户评价**<br> | 知乎、百度贴吧、小红书、行业论坛搜“企业名+怎么样/骗/质量差”；黑猫投诉 | 典型差评关键词：货不对板、延期交货、售后失联、发票问题；长期合作客户（知名企业/上市公司案例，可反向核实）；行业奖项或认证（高新、专精特新，有参考但非绝对）。 |
| **5. 技术与创新能力**<br> | 中国及多国专利审查信息查询系统、佰腾网查专利；招聘网站看研发岗薪资与数量 | 专利类型（发明专利>实用新型>外观设计，数量多且持续申请为佳）；软著或是否参与行业标准制定；从招聘信息推断研发团队规模与技术投入。 |
| **6. 供应链与抗风险能力**<br> | 询问其上游主要原材料供应商（部分官网公示），看是否多生产基地/仓储中心 | 关键物料库存政策（JIT 零库存还是备安全库存）；核心部件是否依赖单一来源；物流合作方（顺丰/德邦等正规物流还是小散车队）。 |
| **7. 网络存迹与数字足迹**<br> | 微信搜一搜、领英 LinkedIn 搜企业名；Wayback Machine 网页时光机看官网历史版本 | 官网真实性（ICP 备案是否与企业名称一致）；领英员工数量、职位、在职时长（频繁换高管需谨慎）；历史宣传变化（如从“年产值 10 亿”改口“5 亿”需追问原因）。 |

#### 信息交叉验证流程（照录）

| 步骤 | 动作 |
|---|---|
| **初筛** | 用天眼查排除有严重司法风险的企业。 |
| **深挖** | 在行业 B2B 平台看产品细节和起订量。 |
| **口碑** | 在知乎/贴吧搜“企业名+坑/骗”（注意辨别同行抹黑）。 |
| **验证** | 要求对方提供与其他客户的合作合同脱敏页、近期发货单、社保缴纳人数截图（可反映真实员工数）。 |
| **试探** | 第一次合作建议先小批量试单，而不是直接下大单。 |

##### 提醒 · “查不到信息”本身也是一种信息

网络上查不到任何负面的小公司，和负面满天飞的大公司，都需要同样警惕。

“查不到信息”往往意味着规模极小或刚成立不久，不能把“无负面”等同于“可靠”。
