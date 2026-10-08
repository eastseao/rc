---
title: "评论系统对比：Disqus·utterances·giscus·Cusdis"
description: "四系统七维对比表、utterances 配置、Cusdis app-id 查找与嵌入、Jekyll Chirpy 接入排错。"
pubDatetime: 2025-10-11
category: "建站与技术"
kind: "长文"
tags: ["评论系统", "Disqus", "utterances", "giscus", "Cusdis"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00183-2025-10-07 查找 Cusdis ID 的途径与方法00187-2025-10-08 评论系统 Disqus、utterances、giscus 分析00221-2025-10-11 用户提供 Cusdis ID 请求帮助

## 01 · 四款评论系统各自为谁而生（00187）

四个系统都能给网站加评论入口，但设计理念不同：Disqus 是成熟商业平台，utterances / giscus 把评论存进 GitHub，Cusdis 则是主打隐私的轻量开源方案。先看各家定位，再看对比表。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>商业老牌</span><h3>Disqus · 成立于 2007 年的第三方评论平台</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>用户管理</dt><dd>支持 Facebook、Twitter、Google 等社媒登录，访客无需单独注册。</dd><dt>内容管理</dt><dd>审核工具、垃圾邮件过滤、评论排序与黑名单齐全；内置分析仪表板。</dd><dt>互动</dt><dd>点赞、回复、线程式讨论、邮件通知。</dd><dt>代价</dt><dd>免费版可能显示广告；高级 CSS 定制与分析需付费；外部脚本拖慢静态站；数据存 Disqus 服务器，涉及 GDPR 合规。</dd><dt>适合</dt><dd>传统动态站、新闻媒体、需要强管理与数据分析、不介意隐私与性能代价的商业站点。</dd></dl></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>GitHub Issues</span><h3>utterances · 基于 GitHub Issues 的轻量评论</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>存储</dt><dd>评论落在你仓库的 Issues 里，访客用 GitHub 账号登录；完全免费、无广告、开源。</dd><dt>性能</dt><dd>无需数据库，脚本小巧加载快，专为 GitHub Pages / Jekyll / Hugo 等静态站优化。</dd><dt>代价</dt><dd>功能基础，缺反垃圾与复杂审核；评论者必须有 GitHub 账号，抬高普通访客门槛；依赖 GitHub 可用性。</dd><dt>适合</dt><dd>技术博客、开源项目文档、以开发者为主的社区，看重隐私与加载速度。</dd></dl></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>GitHub Discussions</span><h3>giscus · utterances 的 Discussion 升级版</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>存储</dt><dd>评论存进仓库的 Discussions，比 Issues 多了分类与标签；免费开源、脚本轻量。</dd><dt>功能</dt><dd>支持讨论分类、reaction 表情、搜索、更灵活的线程映射规则。</dd><dt>代价</dt><dd>同样要 GitHub 账号；缺商业级反垃圾；作为 utterances 分支，社区与文档不如 Disqus 成熟。</dd><dt>适合</dt><dd>比 utterances 需要更灵活讨论结构的技术博客、开源项目与文档站。</dd></dl></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>隐私轻量</span><h3>Cusdis · 主打数据隐私的开源评论系统</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>定位</dt><dd>轻量、注重隐私、对静态博客友好，可作为 Disqus 替代品；访客用昵称+邮箱留言，无需 GitHub 账号。</dd><dt>管理</dt><dd>独立后台，评论默认需审核后展示；支持邮件通知，并可在邮件中直接审核。</dd><dt>迁移</dt><dd>支持一键导入 Disqus 历史评论数据。</dd><dt>代价</dt><dd>默认界面英文，需自行加脚本中文化；官方服务在国内网络下可能访问不稳，可自托管后端。</dd></dl></div></div>

## 02 · 七维横向对比表（00187 / 00221）

把三套原方案的综合比较表，加上 Cusdis 这一列。Cusdis 与 giscus 的配置差异另在下表给出。

| 维度 | Disqus | utterances | giscus | Cusdis |
|---|---|---|---|---|
| **成本** | 免费版有广告，付费解锁高级功能 | 完全免费 | 完全免费 | 免费开源，可自托管 |
| **数据存储** | Disqus 第三方服务器（中心化） | GitHub Issues（去中心化） | GitHub Discussions（去中心化） | 你部署的数据库（如 PostgreSQL）/ 官方托管 |
| **用户认证** | Facebook / Twitter / Google 等社媒账号 | GitHub 账号 | GitHub 账号 | 昵称 + 邮箱，无需 GitHub 账号 |
| **功能丰富度** | 高：审核、反垃圾、分析仪表板 | 低：基本评论 | 中：讨论分类、reaction、搜索 | 中：审核、邮件通知、Disqus 导入 |
| **性能** | 外部脚本，可能偏慢 | 轻量快速 | 轻量快速 | 脚本轻量，加载快 |
| **隐私** | 可能跟踪用户数据 | 隐私友好 | 隐私友好 | 主打数据隐私 |
| **集成难度** | 简单：嵌一段 JS | 中等：需装 GitHub App 并配 repo | 中等：需在 giscus.app 取 repo_id / category_id | 中等：取 App ID，嵌 data-* 代码 |
| **管理后台** | Disqus 自带后台 | 通过 GitHub Issues 管理 | 通过 GitHub Discussions 管理 | 独立 Cusdis 管理后台 |
| **目标用户** | 通用网站、商业站点、媒体 | 静态站、技术博客 | 静态站、开源项目 | 注重隐私的个人静态博客 |

| 配置项 | 原配置（giscus） | 新配置（Cusdis） |
|---|---|---|
| **provider** | `giscus` | `cusdis` |
| **数据存储** | GitHub Issues / Discussions | 你部署的数据库（如 PostgreSQL） |
| **配置方式** | 需配`repo`、`repo_id`等 | 需配`data_app_id`/`app_id`与 host |
| **管理后台** | 通过 GitHub Issues / Discussions 管理 | 独立的 Cusdis 管理后台 |

## 03 · 怎么选：按场景对号入座（00187）

结论落在「目标用户是谁、网站什么类型、要不要 GitHub 门槛」三件事上。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">选 Disqus</h3><p style="font-size:13.5px;color:inherit">需要强大的评论管理、用户互动工具和数据分析，且不介意隐私与性能代价。适合商业网站、新闻媒体，或访客非技术用户居多的场景。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">选 utterances</h3><p style="font-size:13.5px;color:inherit">网站是静态的（GitHub Pages / Jekyll / Hugo），注重隐私和性能，读者主要是开发者或技术爱好者。功能简单，但足够应付基本评论。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">选 giscus</h3><p style="font-size:13.5px;color:inherit">比 utterances 更想要分类、标签、reaction 这类讨论结构，又愿意继续用 GitHub Discussions。适合技术博客、开源项目文档、社区驱动站点。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">选 Cusdis</h3><p style="font-size:13.5px;color:inherit">想绕开「评论必须有 GitHub 账号」的门槛，又要隐私友好、轻量、能自己管评论。个人静态博客、希望普通访客也能匿名留言时的现代选择。</p></div></div>

> **一句话总结**：对大多数静态网站和技术项目，utterances 或 giscus 是更现代、更轻量的选择；Disqus 留给需要一站式商业方案的场景；Cusdis 补上「不想让访客注册 GitHub」的缺口。

## 04 · utterances 实测配置参数（00187 · seamoonappear.github.io）

以用户名`seamoonappear`、仓库`seamoonappear/seamoonappear.github.io`为例。Chirpy 原生配置块里要填的两个核心参数：

utterances: repo: "seamoonappear/seamoonappear.github.io" issue_term: "pathname" # theme: "github-light" # 可选

| 参数 | 填法 | 说明 |
|---|---|---|
| **repo** | `"seamoonappear/seamoonappear.github.io"` | 必须改。格式「用户名/仓库名」；仓库必须**公开**，否则访客无法看评论。 |
| **issue_term** | `pathname` | 决定页面如何关联 Issue。可选：`pathname`（页面路径，省心推荐）、`title`、`url`、`og:title`、`issue-number`（手动指定 Issue ID，适合多页评论汇总到一个 Issue）。 |
| **theme** | `github-light`（可选） | 不设则跟随系统主题；可选`github-dark`、`github-dark-orange`等。 |

> **用前必做两步**
> - 访问`https://github.com/apps/utterances`，点 Install 并授权它访问你的`seamoonappear.github.io`仓库——不装 App，访客发不出评论。
> - 确认仓库设置里已开启**Issues**。原理：一篇新文章首次被评论时，utterances 自动新建一个 Issue，该文章后续评论都挂在这个 Issue 下。

## 05 · Cusdis 接入与 ID 查找（00183 / 00187 / 00221）

从 utterances / giscus 切到 Cusdis 的完整路径：注册取 App ID → 嵌 data-* 代码 → 中文化 → 后台审核。先解决最常见的问题——Cusdis ID 去哪看。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00183 · 2025-10-07</span><h3>Cusdis ID 从哪找</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:170px">查找位置</th><th>操作方法</th></tr></thead><tbody><tr><td><b>Cusdis 管理后台</b></td><td>登录后在网站设置 / 项目信息 / API 配置里找 &quot;App ID&quot;、&quot;Project ID&quot; 或 &quot;Website ID&quot;。</td></tr><tr><td><b>网站嵌入代码</b></td><td>在页面 HTML 的 Cusdis 初始化代码里找<code>appId</code>或<code>data-app-id</code>，其值就是你的 ID。</td></tr><tr><td><b>安装/设置文件</b></td><td>检查首次设置时的配置文件或安装说明文档。</td></tr></tbody></table></div><p style="margin-bottom:10px">从嵌入代码里照录出的真实 ID（UUID 格式）：</p><div>&lt;div id=&quot;cusdis_thread&quot; data-host=&quot;https://cusdis.com&quot; data-app-id=&quot;a507d22b-3586-405c-a6b5-50563ba8eb75&quot; data-page-id=&quot;{{ PAGE_ID }}&quot; data-page-url=&quot;{{ PAGE_URL }}&quot; data-page-title=&quot;{{ PAGE_TITLE }}&quot;&gt; &lt;/div&gt; &lt;script async defer src=&quot;https://cusdis.com/js/cusdis.es.js&quot;&gt;&lt;/script&gt;</div><div style="margin-top:14px"><h4>红线 · 保管 ID</h4><div>data-app-id 是 Cusdis 识别你网站的唯一标识</div><p>它虽出现在前端嵌入代码里，但仍属敏感标识——妥善保管，不要在公开仓库或公开场合额外扩散；配置 API、做集成时会用到它。</p></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00187 / 00221 · 2025-10</span><h3>四步接入 Cusdis</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>① 注册建站</dt><dd>用 GitHub 账号登录<code>https://cusdis.com</code>，点<code>New website</code>创建站点；进站点设置点<code>Embed Code</code>，拿到含<code>data-app-id</code>的代码。</dd><dt>② 嵌入代码</dt><dd>把片段放进评论组件文件（如<code>comments.html</code>/<code>cusdis.html</code>），按博客模板替换<code>data-page-id</code>、<code>data-page-url</code>、<code>data-page-title</code>三个变量；Hugo 用<code>.RelPermalink</code>/<code>.Title</code>，Jekyll 用<code>page.url | absolute_url</code>/<code>page.title</code>。</dd><dt>③ 中文化</dt><dd>默认界面英文，在嵌入代码后加<code>window.CUSDIS_LOCALE = { ... }</code>脚本翻译「发送 / 加载中 / 昵称 / 评论已发送待审核」等字段。</dd><dt>④ 审核与通知</dt><dd>所有评论默认需在后台审核通过后展示；在<code>Email Notification</code>绑定邮箱即可收新评论通知并在邮件里直接审核。从 Disqus 迁移时支持一键导入历史评论。</dd></dl></div></div>

## 06 · Jekyll Chirpy 接入排错（00187 / 00221）

Chirpy 原生只认 disqus / utterances / giscus，接 Cusdis 要自建 include 文件。真实踩坑集中在「配了却不显示」，按下面顺序排。

<details open><summary>需要动的四个文件与职责<span>Chirpy 结构</span></summary><div><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:230px">文件路径</th><th>核心作用</th></tr></thead><tbody><tr><td><code>_config.yml</code></td><td>启用并配置 Cusdis：<code>comments.provider: cusdis</code>+<code>cusdis.data_app_id</code>/<code>host</code>。</td></tr><tr><td><code>_layouts/post.html</code></td><td>定义评论区位置，在<code>{{ content }}</code>之后<code>{% include comments.html %}</code>。</td></tr><tr><td><code>_includes/comments.html</code></td><td>按配置选择提供商：<code>{% if site.comments.provider == 'cusdis' %}{% include comments/providers/cusdis.html %}{% endif %}</code>。</td></tr><tr><td><code>_includes/comments/providers/cusdis.html</code></td><td>Cusdis 评论框具体实现：<code>#cusdis_thread</code>+ 五个<code>data-*</code>属性 + 异步脚本。</td></tr></tbody></table></div><p>注意 Chirpy 原生<b>不识别</b><code>provider: cusdis</code>，评论显不显示主要靠 post.html 里的<code>{% if page.comments %}</code>判断；文章 Front Matter 写<code>comments: true</code>才会渲染评论框。</p></div></details>

<details><summary>评论框「不显示」四步排查<span>高频故障</span></summary><div><ul><li><b>核对 _config.yml</b>：<code>data_app_id</code>与<code>host</code>（官方为<code>https://cusdis.com</code>）是否正确；注意参数名连字符与下划线写法（<code>data-app-id</code>vs<code>data_app_id</code>）要和模板里取值方式一致。</li><li><b>检查模板嵌入</b>：<code>data-app-id</code>、<code>data-host</code>、<code>data-page-id</code>、<code>data-page-url</code>、<code>data-page-title</code>五个属性都要有效赋值；模板里别残留 giscus / disqus 旧代码。</li><li><b>看浏览器控制台</b>：F12 → Console，看<code>cusdis.es.js</code>是否加载失败、有无 CORS / API 报错。</li><li><b>核对 Cusdis 后台与网络</b>：后台绑定域名必须与博客地址完全一致；本地<code>http://localhost:4000</code>未在后台登记时评论框不加载是正常现象，需推到 GitHub Pages 生产环境再测；国内网络下官方服务可能不稳，可自托管后端。</li></ul></div></details>

<details><summary>接入时连带踩的两个坑<span>layout 被改坏</span></summary><div><ul><li><b>文章排版全变、丢了时间作者和底部推荐</b>：多半是新写 post.html 时漏掉了 Chirpy 原有的<code>&lt;header class=&quot;post-meta&quot;&gt;</code>元信息块与<code>related_posts</code>推荐块。补回发布时间、作者、分类，以及<code>{% for post in site.related_posts limit:5 %}</code>推荐列表。</li><li><b>评论区带滚动条/想完全展开</b>：给<code>#cusdis_thread</code>与 iframe 设<code>height:auto; overflow-y:visible</code>，去掉<code>max-height</code>限制，即可让评论区随内容自然撑开、不出现内部滚动条。</li></ul></div></details>
