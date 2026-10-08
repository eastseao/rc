---
title: "Jekyll 主题推荐与 Chirpy 入门"
description: "Jekyll 主题选型表、四条搭建路径、chirpy-starter 四步、_config 片段照录与三类起步报错。"
pubDatetime: 2025-10-25
category: "建站与技术"
kind: "手册"
tags: ["Jekyll", "Chirpy", "主题选型", "chirpy-starter"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00196-2025-10-09 推荐Jekyll主题搭建个人网站（162KB，含 Minimal Mistakes 全流程与配置）00318-2025-10-25 使用Chirpy主题创建GitHub博客（63KB，含 chirpy-starter 与三段 _config.yml）00319-2025-10-25 我的jekyll-theme-chirpy 7.4.0，请提供各（仅一句提问，AI 未作答，并入源说明）

## 01 · 先选型：六款口碑 Jekyll 主题（00196）

原笔记按「开发者中口碑不错」的口径列了六款主题，各自定位不同：要**现代技术博客**选 Chirpy，要**高度自定义**选 Minimal Mistakes，要**学术简历风**选 Minimal Light。

| 主题名称 | 主要特点 | 适用场景 |
|---|---|---|
| **Minimal Light** | 设计简洁优雅、支持暗黑模式、搜索引擎优化、移动端适配 | 学术个人主页、在线简历 |
| **Chirpy** | 功能丰富（评论、搜索、分类标签）、界面现代、文档详尽 | 技术博客、个人日志 |
| **Minimal Mistakes** | 可高度自定义、响应式设计、布局多样 | 多功能网站（博客、作品集等） |
| **Mr. Green** | 支持多语言、功能丰富（颜色方案切换、联系表单等）、SEO 友好 | 多语言博客、团队官网 |
| **Slate** | 设计优雅直观、集成 Google Analytics、响应式设计 | 个人博客、项目展示 |
| **jekyll-theme-YC** | 代码高亮、夜间模式、文章搜索、复制版权声明 | 技术博客、阅读类网站 |

原笔记给的三条通用建议：

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>先试演示</dt><dd>挑选主题时务必亲身体验主题的在线演示，看设计与功能是否符合预期和品味。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>善用文档</dt><dd>遇到问题多查主题自带文档，或到 GitHub 仓库的 Issues 里找解决方案，开发者社区通常很活跃。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>自定义域名</dt><dd>使用 GitHub Pages 时可配置自定义域名，让个人网站看起来更专业。</dd></dl></div></div>

## 02 · 纯网页就能完成的四条搭建路径（00196）

用户最关心「能不能只在网页上操作、不装本地环境」。原笔记给出的答案：可以，核心依赖 GitHub Pages 的自动构建。四条路径按上手速度从快到慢排列。

| 路径 | 主要特点 | 怎么用网页完成 |
|---|---|---|
| **GitHub Pages 官方主题** | GitHub 内置，开箱即用，配置简单，无需本地环境 | 仓库 Settings → Pages → Choose a theme 直接选取。 |
| **remote_theme 引用** | 可用更多现代 Jekyll 主题，主题更新自动同步 | 在 _config.yml 加一行remote_theme: 作者/仓库。 |
| **Use this template 模板** | 一键复制完整仓库，起点高，自定义空间大 | 点绿色按钮「Use this template」→ Create a new repository，命名为 用户名.github.io。 |
| **Fork 仓库** | 没有模板按钮时的等价替代，得到完整副本 | 右上角 Fork → 改仓库名为 用户名.github.io → Rename。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">路径二与路径三怎么选</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>模板法</dt><dd>上手最快，自带完整目录结构；但主题更新需手动合并同步。推荐给想快速拥有完整网站的新手。</dd><dt>远程主题法</dt><dd>只改 _config.yml 一行，主题更新自动同步；但自定义灵活性中等。推荐给想在现有仓库上快速换主题的人。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">纯网页操作的通用规则</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.8"><li>仓库名必须是<b>用户名.github.io</b>（项目页则为 用户名.github.io/仓库名，需配 baseurl）。</li><li>文章用 Markdown 写，放<b>_posts</b>目录，文件名遵循<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">YYYY-MM-DD-title.md</span>。</li><li>所有改动都用网页端 Commit 保存，无需本地环境。</li><li>部分主题允许在线改<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">_sass/_variables.scss</span>调颜色字体。</li></ul></div></div>

##### 红线 · 仓库名与公开度

仓库必须命名为 用户名.github.io，且必须 Public

这是 GitHub Pages 的硬性规定：仓库名决定了能否通过 https://用户名.github.io 直接访问；私有仓库无法使用免费的 GitHub Pages。若用项目仓库名（如 boke），则访问地址变为 https://用户名.github.io/boke，且 _config.yml 里必须配 baseurl: "/boke"、头像等资源路径也要带 /boke 前缀。

## 03 · Chirpy 从模板到上线：四步走（00318）

00318 的完整叙事是：直接用**cotes2020/chirpy-starter**官方模板（专为网页端快速部署设计），不需要在主仓库里找 Use this template，也不需要 Fork。四步走完整覆盖。

| 步骤 | 动作 | 关键配置/注意 |
|---|---|---|
| **第一步** | 访问 github.com/cotes2020/chirpy-starter，点**Use this template → Create a new repository**。 | Owner 选自己账号；Repository name 必须是 用户名.github.io；保持 Public。 |
| **第二步** | 编辑**_config.yml**：填 title、tagline、description、url、username。 | timezone 填 Asia/Shanghai；# 后是注释不生效，只改冒号后的值。 |
| **第三步** | 仓库**Settings → Pages → Build and deployment**，Source 选**GitHub Actions**。 | 等几分钟构建；首次构建约 5–10 分钟，先看到示例页属正常，刷新即可。 |
| **第四步** | 进**_posts**目录，Create new file，命名2025-10-25-标题.md。 | 先写 Front Matter（title/date/categories/tags），再写 Markdown 正文。 |

第一篇文章的 Front Matter 与正文（照录）

```
---
title: "欢迎来到我的地平线博客"
date: 2025-10-25 15:00:00 +0800
categories: [随笔]
tags: [欢迎]
---

这是我的第一篇博客文章！

## 你好，世界！

很高兴能在这里与你分享我的所思所想。

- 这是列表项
- **这是加粗的文字**
```

> **关于「没看到 Use this template 按钮」**
> - 原笔记的兜底方案是直接**Fork**官方仓库 cotes2020/jekyll-theme-chirpy，再到 Settings 把仓库 Rename 为 用户名.github.io。
> - 再不行：从 Releases 页面下载源码压缩包，手动新建同名仓库后整包上传。
> - 若不想用模板/Fork，也可以一个文件一个文件手建（_config.yml、Gemfile、_tabs/about.md、_tabs/archives.md、_data/contact.yml、index.html），但学习成本高，原笔记不推荐新手走这条。

## 04 · _config.yml 关键配置片段照录（00318 / 00196）

00318 给了三段逐步叠加的 _config.yml：基础版、加 Cusdis 评论+头像版、以及带上海时区的基础版。00196 另给了 Minimal Mistakes 路线的完整配置。这里只摘**与起步直接相关**的片段，原文照录。

<details open><summary>Chirpy 基础配置（中文 + 上海时区 + Cusdis）<span>00318</span></summary><div><p>用户给的硬要求：上海时区、中文、Cusdis app_id。原文照录如下，直接整段替换 _config.yml 即可。</p><pre># 站点设置 lang: zh-CN title: &quot;地平线&quot; tagline: &quot;一个分享知识与思考的地方&quot; description: &quot;seamoonappear 的个人博客&quot; keywords: &quot;博客, 技术, 思考, 分享&quot; url: &quot;https://seamoonappear.github.io&quot; # 作者信息 author: &quot;seamoonappear&quot; twitter: username: &quot;&quot; # 构建设置 theme: jekyll-theme-chirpy plugins: - jekyll-sitemap - jekyll-seo-tag - jekyll-feed # 国际化 timezone: Asia/Shanghai # 评论系统 - Cusdis comments: active: &quot;cusdis&quot; cusdis: app_id: &quot;a507d22b-3586-405c-a6b5-50563ba8eb75&quot; host: &quot;https://cusdis.com&quot; lang: &quot;zh-cn&quot; # 其他设置 paginate: 10 paginate_path: /page/:num/ permalink: /posts/:title/ feed: path: atom.xml posts_limit: 20</pre><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>照录提醒</b>：提交后需到 Cusdis 官网确认域名已正确配置；时区 Asia/Shanghai 后所有时间显示用北京时间；zh-CN 后界面默认中文。</div></div></details>

<details><summary>Chirpy 侧边栏头像 + Cusdis 完整段（00318）<span>00318</span></summary><div><pre># 侧边栏头像 - 使用你提供的路径 avatar: /assets/img/avatar.jpg # =============================================== # 评论系统 - Cusdis配置 # =============================================== comments: active: cusdis # 启用cusdis评论系统 cusdis: app_id: &quot;a507d22b-3586-405c-a6b5-50563ba8eb75&quot; # 你提供的app_id</pre><p>前提：头像图片须先上传到仓库的<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">/assets/img/</span>目录并命名 avatar.jpg，建议正方形比例，显示效果最佳。</p></div></details>

<details><summary>Minimal Mistakes 路线的 _config.yml（00196）<span>00196</span></summary><div><pre># 站点基本设置 title: &quot;海月の港湾&quot; name: &quot;海月&quot; description: &quot;记录技术与生活的点点滴滴&quot; locale: &quot;zh-CN&quot; url: &quot;https://seamoonappear.github.io&quot; baseurl: &quot;/boke&quot; # 项目仓库名时必须填；用户名.github.io 仓库则留空 # 主题设置 remote_theme: mmistakes/minimal-mistakes minimal_mistakes_skin: &quot;default&quot; # 可选 default/air/aqua/contrast/dark/dirt/neon/mint search: true # 移除 Follow 按钮 follow: button: false # 默认 Front Matter（适用于所有帖子） defaults: - scope: path: &quot;&quot; type: posts values: layout: single author_profile: true read_time: true comments: true share: true related: true toc: true # 插件 plugins: - jekyll-include-cache sitemap: true</pre><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:12px"><h5>两处易踩</h5><ul><li>baseurl：仓库名是 用户名.github.io 时留空；是 boke 这类项目名时填<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">/boke</span>，且头像路径要写成<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">/boke/assets/images/bio-photo.jpg</span>。</li><li>Follow 按钮：只隐藏按钮用<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">follow: button: false</span>；<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">author_profile: false</span>会把整块作者信息栏都藏掉，别混用。</li></ul></div></div></details>

<details><summary>GitHub Actions 部署工作流（00196）<span>00196</span></summary><div><p>文件路径<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">.github/workflows/jekyll-gh-pages.yml</span>。含依赖缓存与 production 构建环境。</p><pre>name: &quot;Deploy Jekyll site to GitHub Pages&quot; on: push: branches: [&quot;main&quot;] pull_request: workflow_dispatch: permissions: contents: read pages: write id-token: write jobs: build: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - uses: ruby/setup-ruby@v1 with: ruby-version: '3.3' bundler-cache: true cache-version: 1 - uses: actions/configure-pages@v4 - run: bundle install - name: Build with Jekyll run: bundle exec jekyll build --future --unpublished --verbose env: JEKYLL_ENV: production - uses: actions/upload-pages-artifact@v3 with: path: ./_site deploy: environment: name: github-pages url: ${{ steps.deployment.outputs.page_url }} runs-on: ubuntu-latest needs: build steps: - id: deployment uses: actions/deploy-pages@v4</pre></div></details>

## 05 · 起步期三类构建报错与修复（00318）

00318 末尾连续三次 GitHub Actions 构建失败，都是「_config.yml 里声明了插件、Gemfile 里却没写对应 gem」这一类问题。按报错信息逐条对照修复。

| 报错关键信息 | 根因 | 修复动作 |
|---|---|---|
| **cannot load such file -- jekyll-feed**<br> | _config.yml 的 plugins 列了 jekyll-feed，但 Gemfile 里没声明该 gem。 | Gemfile 补gem "jekyll-feed"；或直接用gem "github-pages", group: :jekyll_plugins一把带上常用插件。 |
| **The jekyll-theme-chirpy theme could not be found.** | _config.yml 写了 theme: jekyll-theme-chirpy，但 Bundler 在 Gem 路径里找不到主题 gem。 | Gemfile 补gem "jekyll-theme-chirpy", "~> 7.0"（版本按实际，不确定就不锁版本让 Bundler 自选）。 |
| **bundler: command not found: htmlproofer**<br> | 构建本身已 done in 0.935s，是后续 htmlproofer 这步找不到命令。 | Gemfile 补gem "htmlproofer"；并检查 .github/workflows 里调用 htmlproofer 的命令与参数是否正确。 |

修好后的 Gemfile 骨架（照录）

```
source "https://rubygems.org"

gem "jekyll", "~> 4.4.1"
gem "jekyll-theme-chirpy", "~> 7.0"  # 按实际主题版本调整

# _config.yml 的 plugins 里提到的插件，这里一并声明
gem "jekyll-sitemap"
gem "jekyll-seo-tag"
gem "jekyll-feed"

# 想省心就换成下面这一行，由 GitHub Pages 管依赖版本：
# gem "github-pages", group: :jekyll_plugins
```

> **三条附加纪律（照录原笔记）**
> - 不要提交 _site 目录：.gitignore 必须包含 _site，由构建流程生成，手动提交会导致冲突。
> - Gemfile.lock 建议一并提交，锁定依赖确切版本，保证构建环境一致。
> - 首页若仍显示主题预置页：确认根目录 index.md/index.html 的 Front Matter 里写了layout: home，且 _config.yml 没有用 index:/home: 强制指向别处；改完等 Actions 重建。
