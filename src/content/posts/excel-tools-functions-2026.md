---
title: "Excel 函数分类·公式·转 JSON·截图转表格"
description: "Excel 函数按类别总览与示例公式、列数据除以固定单元格绝对引用公式、Excel 转 JSON 三套方案与屏幕截图转表格方法。"
pubDatetime: 2026-03-19
category: "建站与技术"
kind: "长文"
tags: ["Excel 函数", "示例公式", "绝对引用", "Excel 转 JSON", "截图转表格"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00486-2025-12-10 Excel函数分类及使用指南00761-2026-03-18 Excel列数据除以固定单元格公式00333-2025-10-26 Excel转JSON工具推荐及方案总结00667-2026-03-07 屏幕截图转表格

## 01 · Excel 函数分类总览（00486）

Excel 有数百个函数，全部罗列并不实用。原笔记把它们按用途归成**十一个大类**，并指出：掌握核心的**50-100 个常用函数**即可解决 90% 以上的问题。下表照录分类与代表函数。

| 函数类别 | 代表函数与用途 |
|---|---|
| **财务函数** | `PMT`贷款支付额、`FV`投资未来值、`PV`现值、`NPV`净现值、`IRR`内部收益率、`RATE`利率。 |
| **日期与时间** | `NOW`当前日期时间、`TODAY`当前日期、`DATE`拼日期、`DATEDIF`日期间差、`YEAR`/`MONTH`/`DAY`取年月日、`WORKDAY`/`NETWORKDAYS`工作日计算。 |
| **数学与三角** | `SUM`求和、`SUMIF`/`SUMIFS`条件求和、`SUMPRODUCT`乘积和、`ROUND`四舍五入、`INT`取整、`MOD`取余、`RAND`随机数、`ABS`绝对值。 |
| **统计函数** | `AVERAGE`平均、`AVERAGEIF(S)`条件平均、`COUNT`数数字、`COUNTA`数非空、`COUNTIF(S)`条件计数、`MAX`/`MIN`极值、`MEDIAN`中位数、`MODE`众数、`STDEV`样本标准差、`RANK`排名。 |
| **查找与引用** | `VLOOKUP`垂直查找、`XLOOKUP`新一代查找（更推荐）、`HLOOKUP`水平查找、`INDEX`按位置取值、`MATCH`找相对位置、`INDIRECT`文本转引用、`OFFSET`偏移引用。 |
| **文本函数** | `LEFT`/`RIGHT`/`MID`截取、`LEN`长度、`FIND`/`SEARCH`找位置、`TEXT`数值转文本、`VALUE`文本转数值、`CONCATENATE`与`&`合并、`TEXTJOIN`带分隔符合并、`TRIM`去首尾空格、`SUBSTITUTE`/`REPLACE`替换。 |
| **逻辑函数** | `IF`条件判断、`IFS`多条件、`AND`/`OR`/`NOT`逻辑与或非、`TRUE`/`FALSE`逻辑值。 |
| **信息函数** | `ISERROR`是否错误、`ISNUMBER`是否数字、`ISTEXT`是否文本、`ISBLANK`是否为空、`CELL`取单元格信息。 |
| **工程函数** | `CONVERT`度量单位换算，另含复数、进制转换、贝塞尔函数等。 |
| **数据库函数** | `DSUM`、`DAVERAGE`、`DCOUNT`数据库式求和/平均/计数。 |
| **现代函数（365 / 2021+）** | `XLOOKUP`替换 VLOOKUP/HLOOKUP、`FILTER`筛选、`SORT`排序、`UNIQUE`去重、`SEQUENCE`生成序列、`LET`定义变量、`LAMBDA`自定义函数。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">在 Excel 里查完整函数列表</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>入口</dt><dd>顶部【公式】选项卡 →【函数库】分组，按类别（财务、逻辑、文本等）分组排列主要函数。</dd><dt>全部函数</dt><dd>点<code>fx</code>【插入函数】按钮，「或选择类别」下拉选「全部」，列表按字母显示所有可用函数，选中后下方显示功能与语法。</dd><dt>官方文档</dt><dd>微软支持站搜索「Excel 函数（按类别列出） - Microsoft 支持」。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">学习路径建议</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>优先掌握</dt><dd><code>SUM</code>、<code>AVERAGE</code>、<code>IF</code>、<code>VLOOKUP</code>/<code>XLOOKUP</code>、<code>INDEX</code>/<code>MATCH</code>、<code>COUNTIF</code>、<code>SUMIF</code>、<code>TEXT</code>、<code>DATE</code>。</dd><dt>遇到问题</dt><dd>再用【插入函数】对话框按类查找，或直接搜「Excel 如何按条件求和」学新函数。</dd></dl></div></div>

## 02 · 常用函数 · 典型场景与示例公式（00486）

同一份笔记的第二段，按功能给出可直接照抄的示例公式。结果注释照录原笔记。

<table><thead><tr><th style="width:150px">功能组</th><th style="width:170px">函数 / 场景</th><th>示例公式（// 后为结果）</th></tr></thead><tbody><tr><td rowspan="4"><b>文本处理</b></td><td>LEFT / RIGHT / MID 截取</td><td><code>=LEFT(&quot;Excel函数&quot;, 3)</code>// &quot;Exc&quot;<code>=MID(&quot;ABCDE&quot;, 2, 3)</code>// &quot;BCD&quot;</td></tr><tr><td>LEN 长度</td><td><code>=LEN(&quot;Excel&quot;)</code>// 5</td></tr><tr><td>TEXT 格式化</td><td><code>=TEXT(TODAY(), &quot;yyyy-mm-dd&quot;)</code></td></tr><tr><td>CONCAT / TEXTJOIN 合并</td><td><code>=CONCAT(&quot;A&quot;, &quot;-&quot;, &quot;B&quot;)</code>// &quot;A-B&quot;；<code>=TEXTJOIN(&quot;,&quot;,TRUE,A1:A3)</code>合并 A1:A3 且忽略空值</td></tr><tr><td rowspan="2"><b>日期时间</b></td><td>TODAY / NOW</td><td><code>=TODAY()</code>返回当前日期</td></tr><tr><td>DATEDIF 求差值</td><td><code>=DATEDIF(&quot;2024-01-01&quot;,&quot;2024-12-10&quot;,&quot;d&quot;)</code>按天求差</td></tr><tr><td rowspan="3"><b>逻辑</b></td><td>IF 条件判断</td><td><code>=IF(A1&gt;60,&quot;及格&quot;,&quot;不及格&quot;)</code></td></tr><tr><td>AND / OR 多条件</td><td><code>=IF(AND(A1&gt;60,B1=&quot;是&quot;),&quot;通过&quot;,&quot;不通过&quot;)</code></td></tr><tr><td>IFERROR 错误处理</td><td><code>=IFERROR(A1/B1, &quot;除零错误&quot;)</code></td></tr><tr><td rowspan="3"><b>查找引用</b></td><td>VLOOKUP 垂直查找</td><td><code>=VLOOKUP(&quot;张三&quot;,A:B,2,FALSE)</code>在 A 列找张三、返回 B 列值</td></tr><tr><td>XLOOKUP（2021+）</td><td><code>=XLOOKUP(&quot;产品A&quot;,A:A,C:C,&quot;未找到&quot;)</code></td></tr><tr><td>INDEX + MATCH 双向查找</td><td><code>=INDEX(C:C,MATCH(&quot;目标&quot;,A:A,0))</code></td></tr><tr><td rowspan="3"><b>数学统计</b></td><td>SUMIF / SUMIFS 条件求和</td><td><code>=SUMIF(A:A,&quot;&gt;100&quot;,B:B)</code>A 列 &gt;100 对应 B 列求和</td></tr><tr><td>AVERAGE / COUNTIF</td><td><code>=AVERAGE(A1:A10)</code>；<code>=COUNTIF(A:A,&quot;完成&quot;)</code>统计「完成」数量</td></tr><tr><td>MAX / MIN 极值</td><td><code>=MAX(A1:A100)</code></td></tr><tr><td><b>财务</b></td><td>PMT 贷款月供</td><td><code>=PMT(5%/12, 5*12, 100000)</code>5 年期 10 万贷款月供</td></tr><tr><td rowspan="2"><b>现代函数</b></td><td>UNIQUE 去重（2021+）</td><td><code>=UNIQUE(A1:A100)</code></td></tr><tr><td>FILTER 动态筛选</td><td><code>=FILTER(A:B, B:B&gt;100)</code></td></tr></tbody></table>

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">三个实用小技巧</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>参数提示</dt><dd>输入函数后按<code>Ctrl+Shift+A</code>查看参数说明。</dd><dt>函数向导</dt><dd>点公式栏<code>fx</code>图标搜索函数。</dd><dt>错误排查</dt><dd>按<code>F9</code>预览选中部分公式的计算结果。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">一个多条件实战示例</h3><p style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px;background:#f8fafc;border-radius:6px;padding:10px 12px">=SUMIFS(销售数据!C:C, 销售数据!A:A, A2, 销售数据!B:B, &quot;&gt;2024-01-01&quot;)</p><p style="font-size:13.5px;color:inherit">即：汇总「销售数据」表 C 列，条件为 A 列等于 A2、B 列晚于 2024-01-01。</p></div></div>

## 03 · 一整列除以固定单元格：绝对引用（00761）

高频问题：表格里 I 列的很多数据要除以 M9，用什么公式？答案是**绝对引用**——行和列都加`$`锁定，下拉填充时 M9 才不会跟着漂移。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00761 · 2026-03-18</span><h3>操作四步走</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">步骤</th><th>做法</th></tr></thead><tbody><tr><td><b>1. 写公式</b></td><td>在 J1 输入<code>=I1/$M$9</code>。<code>$M$9</code>表示无论往下拉多少行，除数始终是 M9。</td></tr><tr><td><b>2. 双击填充柄</b></td><td>选中 J1，鼠标移到单元格右下角小方块（填充柄），变黑十字时<b>双击左键</b>，自动填充到与 I 列同行的高度；数据量小也可按住往下拖。</td></tr><tr><td><b>3. 校验</b></td><td>J2 应为<code>=I2/$M$9</code>，J3 应为<code>=I3/$M$9</code>。</td></tr><tr><td><b>4. 覆盖回 I 列（可选）</b></td><td>先在新列算出结果 → 复制整列新结果 → 右键 I 列 → 选择性粘贴 →<b>数值</b>。</td></tr></tbody></table></div><div style="margin-top:14px"><h4>红线 · 除零错误</h4><div>M9 为空或为 0 时公式会报 #DIV/0!</div><p>务必先确认 M9 里已输入正确的除数，否则整列结果都是<code>#DIV/0!</code>。</p></div></div></div>

## 04 · Excel 转 JSON 的三套方案（00333）

原笔记担心在线工具可用性随时变化，于是给出「在线工具 + 本地代码 + 本地软件」三条路，并附一份选型对比。敏感数据一律先脱敏。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方案一 · 在线工具</span><h3>Table Convert Online（处理不敏感的临时数据）</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>网址</dt><dd><code>https://tableconvert.com/excel-to-json</code></dd><dt>优点</dt><dd>功能专一、支持复杂表格结构；可直接粘贴 Excel 内容或上传<code>.xlsx</code>/<code>.csv</code>；右侧 Options 可调生成格式（如第一行作键名），自动生成 JSON 后复制即用。</dd></dl><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:14px;margin-bottom:0"><b>安全提醒</b>：文件含敏感或机密数据时最安全的做法是<b>先脱敏再上传</b>。</div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方案二 · 本地代码（最安全灵活）</span><h3>另存 CSV，用浏览器控制台一段 JS 转换</h3></div><div style="padding:14px 16px"><p>把 Excel 另存为 CSV，再在浏览器开发者工具控制台运行下面这段<code>csvToJson</code>：</p><pre>function csvToJson(csvString) { const lines = csvString.split('\n'); const result = []; const headers = lines[0].split(','); for (let i = 1; i &lt; lines.length; i++) { const obj = {}; const currentline = lines[i].split(','); for (let j = 0; j &lt; headers.length; j++) { obj[headers[j].trim()] = currentline[j] ? currentline[j].trim() : ''; } result.push(obj); } return result; }</pre><p style="margin-bottom:10px">以示例数据<code>id,name,age / 1,张三,30 / 2,李四,25</code>运行，输出为：</p><pre>[{&quot;id&quot;:&quot;1&quot;,&quot;name&quot;:&quot;张三&quot;,&quot;age&quot;:&quot;30&quot;}, {&quot;id&quot;:&quot;2&quot;,&quot;name&quot;:&quot;李四&quot;,&quot;age&quot;:&quot;25&quot;}] // 用 JSON.stringify(jsonData, null, 2) 可格式化输出</pre></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方案三 · 本地软件</span><h3>VS Code + 转换插件</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>做法</dt><dd>装免费的 VS Code，在扩展商店搜索安装<code>Excel Viewer</code>或<code>CSV to JSON</code>等插件，用 VS Code 打开 CSV 后由插件侧边栏预览或一键转 JSON。</dd></dl></div></div>

| 方案 | 优点 | 缺点 | 适用场景 |
|---|---|---|---|
| **在线工具** | 方便快捷，无需安装 | 有数据安全风险，依赖网络 | 不敏感的、一次性或临时数据 |
| **本地代码** | **最安全、最灵活、免费** | 需要基本代码知识 | **任何数据，尤其是敏感数据** |
| **本地软件** | 功能丰富，安全性高 | 需要安装软件 | 需要频繁做格式转换 |

> **同篇延伸：绑定域名后的查询地址**
> - 库绑定域名`gervas.wang`、且在 gervasw.github.io 根目录建了`tz`文件夹与 index 等文件后，主访问地址为`https://gervas.wang/tz/`（或`/tz/index.html`）；子文件如`/tz/css/style.css`按路径直接拼。
> - 排查：GitHub Pages 的 Source 设为`main`分支、Custom domain 已配置、CNAME 文件在仓库根目录；推送与构建生效通常有几分钟延迟。

## 05 · 一张截图整理成 Markdown 表格（00667）

原笔记的诉求是「把截图改成表格形式放进 Markdown」。下面照录整理后的新品管线表——品名、规格、价格、状态均按原笔记转录，空缺处保持空白。

| 品名 | 规格 | 单位 | 价格 | 备注 | 状态 |
|---|---|---|---|---|---|
| 药食同源小瓶饮系列 | 420ml（60ml*7） | 盒 | 130-160 | 立项已提报集团，等待审批。1. 与药食院拉会确定上市时间 2. 改 24 瓶规格、确认毛利 | 暂缓 |
| 即食人参不定根-传澡款 | 700g（50g*14） | 盒 | 980 | 包装设计沟通确认打样 | 包装确认，6 月上市 |
| 六味地黄饮 | 500ml（50ml*24） | 盒 |  | 初步配方确定，物料采购打样中 | 配方研发，中秋前上市 |
| 乌鸡白凤饮 / 定坤饮 | 500ml（50ml*24） | 盒 |  | 初步配方确定，物料采购打样中 | 配方研发，中秋前上市 |
| 胶原蛋白冰糖燕窝饮 | 600ml（60ml*24） | 盒 |  | 测算 0.01g 洞燕投料成本，毛利控制 30-50%；下铝瓶 24+7 规格，电商/线上袋装规格，零售价成本测算；目标线下 498-598，线上 198；电商沟通 | 新品 |
| 有机枸杞西洋参饮（山姆） | 1.4L（50ml*28） | 箱 | 168 | 预处方、设计、提案已完成，修改完善中 | 方案提报 |
| 燕窝粥系列（5 款） | 900g（150g*6） | 盒 | 118 | 电商报价沟通 | 电商沟通 |
| 蓝莓原浆 |  |  |  | 电商意向不强，持续跟进 | 待定 |
| 西洋参、人参、石斛、陈皮、枸杞五味饮 / 西洋参铁皮石斛枸杞饮 |  |  |  | 六味地黄、乌鸡白凤两款饮品确定后跟进本品 | 配方研发 |
| 人参枸杞原浆 | 24/14 瓶 | 盒 |  | 24 瓶沟通传渠意向；14 瓶储备三渠；主打卖点鲜 / 有机 / 100% | 传渠沟通 |

这张表的价值在于：把一张看不清结构的截图，落成「品名—规格—单位—价格—备注—状态」六列，谁跟到哪一步、卡在什么环节一目了然，后续按状态列筛选即可推进。
