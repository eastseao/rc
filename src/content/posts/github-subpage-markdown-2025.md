---
title: "GitHub 子网页创建与 Markdown 页面"
description: "GitHub 子目录/子域名两方案、A 记录与 CNAME 解析、Enforce HTTPS、仓库容量红线与 Markdown 实时页面。"
pubDatetime: 2025-10-02
category: "建站与技术"
kind: "手册"
tags: ["子目录", "域名解析", "A 记录", "CNAME", "容量红线"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00144-2025-10-01 GitHub 子网页创建与关联指南00146-2025-10-01 GitHub 个人主页添加子网页方法00152-2025-10-02 现在我的网站已经建好，我要在网页里加入 markdown 页面，并且……

## 01 · 子网页两种挂法：子路径 vs 子域名（00144 / 00146）

源笔记把「在个人主页下加子网页」归成两条路：**子目录/子路径**（同一域名下的一段路径）与**子域名**（独立二级域名）。新手先从子路径入手最直接。

| 对比维度 | 子路径页面 | 子域名页面 |
|---|---|---|
| **访问形式** | `用户名.github.io/项目路径` | `子域名.你的域名.com` |
| **适用场景** | 在个人主页下扩展内容：博客、作品集 | 独立项目站点：工具文档、演示页 |
| **核心操作** | 在主站仓库建文件夹并放内容（00146），或新建项目仓库开 Pages（00144 方案 A） | 为子页建独立仓库 → 开 Pages → DNS 加 CNAME 记录 |
| **管理复杂度** | 内容集中、管理方便 | 项目独立、边界更清晰 |

> **源笔记建议**：希望内容紧密关联、统一管理 → 选子路径；项目相对独立或想有特色子域名 → 选子域名。00144 的 mermaid 流程图把两条路都收敛到「最终访问地址」这一节点：子路径是`username.github.io/my-project`，子域名是`blog.yourdomain.com`。

## 02 · 子目录建站五步：以 myblog 为例（00146）

00146 把「方法一：子目录」拆成可照做的五步。核心就一句：**在`用户名.github.io`仓库里建个文件夹，里面放一个`index.html`**。

| 步骤 | 网页操作 | 关键点 |
|---|---|---|
| **1 进入仓库** | 登录 GitHub，进入个人主页仓库（名为`用户名.github.io`） | 这是主站仓库，子网页要放它里面。 |
| **2 建子目录** | 点**Add file → Create new file**；文件名先打`myblog/`（斜杠会让 GitHub 自动建文件夹），再在后面补`index.html`，完整路径`myblog/index.html` | 斜杠是「建文件夹」的关键手法。 |
| **3 写内容** | 在编辑框写 HTML，底部填 Commit message，点**Commit changes** | 子目录入口文件必须叫`index.html`，否则要输全路径。 |
| **4 等部署** | GitHub Pages 自动构建，通常 1–5 分钟 | 也可本地用 git 命令提交：`git add . → commit -m "..." → push origin main`。 |
| **5 访问** | 浏览器开`https://用户名.github.io/myblog` | 绑定自定义域名后变成`你的域名/myblog`。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">资源路径与多页面</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:8px">子网页内的 CSS / JS / 图片<b>一律用相对路径</b>，例如图放<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">myblog/images/</code>，HTML 里写<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">images/photo.jpg</code>。</li><li style="margin-bottom:8px">在<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">myblog/</code>里继续建<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">about.html</code>，访问<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">.../myblog/about.html</code>。</li><li>从主站链接过来：<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">&lt;a href=&quot;/myblog&quot;&gt;查看我的博客&lt;/a&gt;</code>。</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">框架项目与 .nojekyll</h3><p style="margin-bottom:10px">用 Vue / React 等框架写的子网页，必须先本地<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">npm run build</code>，把<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">dist</code>/<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">build</code>产物传上去，而非源码。</p><p style="margin-bottom:0">GitHub Pages 默认走 Jekyll，会忽略下划线开头的目录；子目录里放已构建静态站时，在主站仓库根目录放空文件<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">.nojekyll</code>即可跳过。</p></div></div>

> **子网页打不开 / 样式丢了，按这三点查**
> - **404**：子目录名拼写对不对、`index.html`是不是真在该子目录根下。
> - **样式/图片不加载**：多半是资源路径写错，回到相对路径规则核对。
> - **改了没变化**：浏览器缓存，强制刷新`Ctrl + F5`，或 URL 后加`?v=2`。

## 03 · 自定义域名解析到 gervasw.github.io（00144）

00144 的真实诉求：注册一个域名，解析到`https://gervasw.github.io/`。分三步：DNS 加记录、GitHub 仓库填自定义域名、勾 Enforce HTTPS。

| 记录类型 | 适用 | 配置（照录） |
|---|---|---|
| **A 记录** | 根域名`yourdomain.com` | 主机记录填`@`，记录值依次填 GitHub Pages 的 4 个 IP：<br> |
| **CNAME 记录** | 子域名`www.yourdomain.com` | 主机记录填`www`，记录值填`gervasw.github.io.`（末尾点号可选）。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">GitHub 侧：CNAME 文件</h3><ol style="margin:0;padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:7px">进<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">gervasw.github.io</code>仓库 → Settings → Pages。</li><li style="margin-bottom:7px"><b>Custom domain</b>框填你注册的域名（如<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">www.yourdomain.com</code>），保存。</li><li>GitHub 会自动在仓库根目录生成<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">CNAME</code>文件，内容就是那一行域名。</li></ol></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">Enforce HTTPS 勾不上？</h3><p style="margin-bottom:10px">DNS + CNAME 配好后回 Settings → Pages，找<b>Enforce HTTPS</b>。若复选框<b>灰色不可勾</b>：先把 Custom domain 清空保存、再重新填回域名保存——这会触发 GitHub 重新申请证书。</p><p style="margin-bottom:0">签发需几分钟到几小时；期间勾选项会变可选。DNS 全球生效也是几分钟到几小时，可用<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">dig</code>/<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">nslookup</code>核对是否解析到那 4 个 IP。</p></div></div>

> **选记录的口诀**：用`www.你的域名`→ CNAME；用裸域名`你的域名`→ A 记录；两者可同时配，让带不带 www 都能开。

## 04 · 往网站里加能实时更新的 Markdown 页面（00152）

00152 的核心诉求：网站已建好，要加 Markdown 内容页且**能实时更新**。答案是借助 GitHub Pages 内置的 Jekyll——你只管把 md 文件 push 上去，Pages 自动转网页、自动重部署。两种做法：

| 特性 | 方法一：单页添加 | 方法二：多页网站 |
|---|---|---|
| **场景** | 快速加单个页面（如「关于我」） | 有导航的多页站（博客、文档站） |
| **核心操作** | 根目录建`about.md`，顶部加 Front Matter | 规划目录结构、配`_config.yml`、建导航 |
| **维护** | 简单，页面多了会散乱 | 结构清晰、易扩展 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方法一 · 单页</span><h3>建 about.md：三行 Front Matter 是关键</h3></div><div style="padding:14px 16px"><div style="margin:14px 0">--- layout: page title: &quot;关于我&quot; --- # 欢迎来到我的小站 这是我的个人介绍，使用 Markdown 语法非常方便！ - 爱好：阅读、编程 - 技能：Markdown</div><p style="margin:0">提交 push 后，Pages 自动检测并重部署，几分钟后访问<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">用户名.github.io/仓库名/about.html</code>。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方法二 · 多页</span><h3>Jekyll 目录结构 + jekyll-relative-links</h3></div><div style="padding:14px 16px"><div style="margin:14px 0">你的仓库根目录/ ├── _config.yml<span># 网站配置</span>├── index.md<span># 首页</span>├── about.md<span># 关于页</span>└── _posts/<span># 文章目录</span>├── 2024-10-02-welcome.md └── 2024-10-03-update.md</div><div style="margin:14px 0"><span># _config.yml</span>title: 我的网站标题 theme: jekyll-theme-cayman plugins: - jekyll-relative-links relative_links: enabled: true collections: true include: - README.md</div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:14px"><h5>三条经验</h5><ul><li><b>实时更新</b>：push md 后 Pages 后台自动构建；若没及时生效，Settings → Pages 里点<b>Clear cache and rebuild site</b>。</li><li><b>链接用相对路径</b>：<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">[关于](./about.md)</code>最可靠，<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">jekyll-relative-links</code>插件会自动转成可点链接。</li><li><b>文章命名</b>：<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">_posts</code>里固定<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">年-月-日-标题.md</code>，Front Matter 写<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">layout: post / title / date</code>。</li></ul></div></div></div>

<details><summary>00152 里的另一条路线：浏览器端 Markdown 编辑器<span>marked.js</span></summary><div><p>除了走 Jekyll，源笔记还给过一个「编辑器 + 实时预览」方案：用<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">marked.min.js</code>在前端解析 Markdown，左编辑右预览、自动保存。这适合做一个纯浏览器内的写作页；但要在 GitHub Pages 上长期保留内容，仍需把 md 文件提交进仓库——那就是上面方法一/二的事。</p></div></details>

## 05 · 仓库能放什么、放多大，与首页关联（00144）

子网页多了以后，仓库里能塞什么、单个文件多大、怎么在首页挂导航——00144 给了明确的容量红线和关联手法。

| 维度 | 限制 / 建议（照录） |
|---|---|
| **单个文件** | 普通文件**严格限制 100MB 以内**；超过 50MB 会收到警告；超过 100MB 无法推送。大二进制走**Git LFS**。 |
| **仓库总体** | 官方建议保持**1GB 以下**；硬上限 100GB，达到 75GB 会收到警告。 |
| **Pages 站点** | 源仓库建议不超过 1GB，发布后站点不超过 1GB，另有月度带宽限制；只支持静态文件，不支持服务器端处理（如 .ejs）与数据库。 |
| **敏感信息** | 代码里不要含密码、API 密钥。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00144 · 首页挂导航</span><h3>子网页部署好后，在首页加「我的项目」导航</h3></div><div style="padding:14px 16px"><p style="margin-bottom:10px">在首页个人简介区下方或页脚上方，插一个导航卡片，把每个子网页链接进去：</p><div style="margin:14px 0">&lt;section class=&quot;card&quot;&gt; &lt;h2 class=&quot;card-title&quot;&gt;🌐 我的项目&lt;/h2&gt; &lt;div class=&quot;demand-list&quot;&gt; &lt;li&gt;&lt;a href=&quot;https://用户名.github.io/仓库1/&quot; target=&quot;_blank&quot;&gt;📦 项目一介绍&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;a href=&quot;https://用户名.github.io/仓库2/&quot; target=&quot;_blank&quot;&gt;🎨 项目二展示&lt;/a&gt;&lt;/li&gt; &lt;/div&gt; &lt;/section&gt;</div><p style="margin:12px 0 0">00144 还示范了在「主要采购品类」后加一个<b>供应商信息登记表按钮</b>（链接到在线表单收集潜在供应商基本信息），本质就是一张挂外链的卡片按钮——子网页、表单、Markdown 页都能用同一套路往首页聚合。</p></div></div>
