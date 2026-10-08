---
title: "电子书下载宝库 · 24,071 册实时检索"
description: "基于 18K+ stars 开源仓库的客户端实时检索子页，零服务端。"
pubDatetime: 2026-09-10
category: "建站与技术"
kind: "工具"
tags: ["电子书", "检索", "开源"]
---

GERVAS

电子书宝库

### 结论 · TL;DR一句话判断 + 4 条核心洞察

「源仓库 18K stars / 7.2 MB / 1,000 类，中文电子书垂直开放数据集中规模最大的一份。本子页把它搬进 rc 站做实时客户端检索：

- 无服务端 —— 一个 HTML 文件走天下；JSON 数据由 raw.githubusercontent.com 跨域直供

- 多关键词 AND ——「python 入门」「刘慈欣 三体」「东野圭吾 推理」按空格组合

- 关键字高亮 —— 命中片段用米色背景标记，长字符串里一眼定位

- 移动端友好 —— 桌面三栏 / 平板两栏 / 手机单栏 + 抽屉章节

工具 · 检索

· 2026-09-10 · eastseao

## eBook Treasure Chest电子书下载宝库 · 24,071 册实时检索

把开源仓库[jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest)（18K+ stars，2,533 forks）里的全部中文电子书搬到本页面：7.1 MB JSON，1,000 个分类，epub / mobi / azw3 三格式齐备。客户端实时检索，多关键词（空格分隔）+ 分类筛选 + 关键字高亮，**没有服务端**——打开即用。

数据源

books.json

· 7.06 MB

语言

全 ZH（24,071 / 24,071）

格式

epub + mobi + azw3（每册齐备）

匹配

书名 / 作者 / 分类（多关键词 AND）

24,071

册（中文电子书 · 全量）

1,000

分类（最长尾：文学 2711 · 历史 1748 · 科普 743）

7.06 MB

JSON 体积（首次拉取 5-15 s · 浏览器缓存后秒开）

3

每册格式（epub · mobi · azw3）

### SEARCH · 检索面板实时客户端筛选

清空

多关键词

空格分隔，

全部

命中才算匹配（例

python 入门

）；

分类

点下方任意分类胶囊即切换；

清除

顶部 ✕ 或右侧清空按钮

#### 热门分类

请输入关键词或选择分类

### 方法 · METHOD数据采集说明

源仓库结构层次：`md/<分类>.md`每个文件一个分类（如`md/文学.md`收录 2,711 册文学类），每行结构化收录三格式下载链接。仓库用[`scripts/parse_md_to_json.py`](https://github.com/jbiaojerry/ebook-treasure-chest/blob/main/scripts/parse_md_to_json.py)解析成`docs/books.json`，本子页直接 fetch 该 JSON。

<table><tr><th style="width:160px">字段</th><th>样例</th></tr><tr><td>title</td><td>三体</td></tr><tr><td>author</td><td>刘慈欣</td></tr><tr><td>category</td><td>科幻 / 三体</td></tr><tr><td>link</td><td><code>https://url89.ctfile.com/f/.../?p=8866</code>（城通网盘，复制后浏览器打开提取码）</td></tr><tr><td>formats</td><td><code>[&quot;epub&quot;, &quot;mobi&quot;, &quot;azw3&quot;]</code></td></tr><tr><td>language</td><td><code>ZH</code></td></tr></table>

#### 为什么走客户端

⚡ 实时响应

输入即筛，无服务端往返；24K 册

filter

+

slice

单次 < 20 ms

🔒 数据零拷贝

JSON 仅驻留浏览器内存；不缓存到任何第三方

🌐 CORS 友好

raw.githubusercontent.com 默认

Access-Control-Allow-Origin: *

，跨域直拉

📦 零依赖

纯 vanilla JS · 无 React/Vue · 单 HTML 文件可直接托管到任意 Pages

🗜️ 体积友好

rc 库不进 7 MB 数据，仅 1 个 HTML；浏览器二次访问走磁盘缓存秒开

🔄 自动更新

源仓库每天有 PR；新版 books.json 直接覆盖，刷新即拉新

### CATEGORIES · 分类速览Top 20 大类

源仓库按主题 / 作者 / 国别 / 朝代四类维度细分 1,000 个标签。下表为册数前 20 的分类。

<table><tr><th>#</th><th>分类</th><th style="text-align:end">册数</th></tr><tr><td>01</td><td>文学</td><td style="text-align:end">2,711</td></tr><tr><td>02</td><td>历史</td><td style="text-align:end">1,748</td></tr><tr><td>03</td><td>科普</td><td style="text-align:end">743</td></tr><tr><td>04</td><td>管理</td><td style="text-align:end">613</td></tr><tr><td>05</td><td>社会</td><td style="text-align:end">558</td></tr><tr><td>06</td><td>推理</td><td style="text-align:end">531</td></tr><tr><td>07</td><td>经典</td><td style="text-align:end">494</td></tr><tr><td>08</td><td>经济</td><td style="text-align:end">487</td></tr><tr><td>09</td><td>哲学</td><td style="text-align:end">431</td></tr><tr><td>10</td><td>传记</td><td style="text-align:end">413</td></tr><tr><td>11</td><td>美国</td><td style="text-align:end">399</td></tr><tr><td>12</td><td>心理</td><td style="text-align:end">396</td></tr><tr><td>13</td><td>悬疑</td><td style="text-align:end">393</td></tr><tr><td>14</td><td>商业</td><td style="text-align:end">387</td></tr><tr><td>15</td><td>励志</td><td style="text-align:end">373</td></tr><tr><td>16</td><td>金融</td><td style="text-align:end">370</td></tr><tr><td>17</td><td>随笔</td><td style="text-align:end">368</td></tr><tr><td>18</td><td>投资</td><td style="text-align:end">365</td></tr><tr><td>19</td><td>思维</td><td style="text-align:end">353</td></tr><tr><td>20</td><td>文化</td><td style="text-align:end">344</td></tr></table>

数据观察

·

文学 + 历史

两个分类就占据全库的

18.5%

，是检索最高频入口

·

管理 / 商业 / 投资 / 金融 / 经济 / 思维 / 励志

7 个经管心智分类合计

~2,950 册

，垂直知识库形态已成型

· 长尾分类（≤ 10 册）仍超过

600 个

，含「三体 / 易中天 / 李白 / 撒哈拉 / 巴菲特」等专题库

### HINTS · 使用提示四类场景的最佳姿势

🔎 找一本具体书

直接输入书名；多版本会自动展开；点「下载」复制链接到浏览器（提取码

8866

）

👤 按作者扫库

输入作者名即可；如「刘慈欣 / 东野圭吾 / 易中天 / 曾国藩 / 巴菲特」

📂 浏览某主题

点下方分类胶囊；想看「投资」类的所有 365 册，点一下即过滤

🧪 交叉筛

点「文学」+ 输入「日本」，得到文学分类下的日本作家；多关键词 + 分类可叠加

📱 移动端

搜索框粘性置顶，点击聚焦即弹键盘；横向滑动分类胶囊

🔌 离线

浏览器首次拉取后会缓存；断网下分类胶囊仍可点，但搜索需联网重新拉取

### APPENDIX · 全量索引24,068 册 · 1,000 个分类 · 按分类展开

本页是源仓库`docs/books.json`全量数据的纯文字索引，按分类聚合、册数倒序排列。点击分类展开完整书单；搜索框可按书名筛选。

注：与上面"实时检索面板"共用同一份源数据；区别在于本节无下载链接、纯索引性质，便于通览。

共

1,000

个分类 /

24,068

册去重书名 / 体积

679 KB

紧凑 JSON（嵌入本页）。点击分类标题展开书名；左侧搜索框实时筛选所有可见分类。

全部展开

全部收起

📚

索引加载中…

首次需下载 679 KB · 浏览器二次访问走 sessionStorage 缓存秒开

致谢与免责

本检索页仅做客户端聚合，

所有电子书版权归原作者及出版社所有

。请勿用于商业用途；如遇链接失效请前往

源仓库 Issue

反馈。本子页不代表本站点的商业立场，仅作为日常检索工具。

COLOPHON · 页脚

数据源：

jbiaojerry/ebook-treasure-chest

·

docs/books.json

@ 2026-09-10 · 24,071 册

检索引擎：纯客户端 · vanilla JS · 单 HTML 文件 ·

返回 rc 首页
