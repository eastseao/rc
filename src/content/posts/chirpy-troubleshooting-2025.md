---
title: "Chirpy 排错：首页空白·构建错误·侧边栏"
description: "三类症状对号入座、Invalid date/vendor exclude、缺插件 gem、首页空白二分定位与侧边栏响应式排查。"
pubDatetime: 2025-10-25
category: "建站与技术"
kind: "手册"
tags: ["排错", "GitHub Actions", "Invalid date", "Gemfile", "首页空白", "侧边栏"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00305-2025-10-24 GitHub Pages Jekyll Chirpy 首页显示问题排查（27KB，theme→remote_theme、Starter 模板、Actions 权限）00306-2025-10-24 Jekyll 构建错误解决方案（7KB，Invalid date + exclude vendor）00308-2025-10-24 Jekyll 构建失败解决方案（20KB，jekyll-include-cache 缺失，纯网页操作法）00309-2025-10-24 Jekyll 构建错误：无效日期格式（89KB，vendor exclude / Gemfile 语法 / 重复字段 / kramdown-parser-gfm / remote-theme version）00316-2025-10-25 Jekyll 首页空白问题排查与修复（32KB，Gemfile 重复声明 + 二分定位法）00322-2025-10-25 Chirpy 主题侧边栏无法显示排查指南（36KB，响应式/配置/自定义 CSS）

## 01 · 先对号入座：三类症状与通用排查路径（00305 / 00316 / 00322）

排错前先分清你面对的是哪一类症状，再进对应小节。别一上来就改配置——多数「首页空白」其实是构建失败、或纯前端资源加载问题。

| 症状 | 典型表现 | 先去哪节 |
|---|---|---|
| **首页只显示一行字** | 页面上只有--- layout: home # Index page ---之类的原始文本，没有主题样式 | 04 首页空白 |
| **Actions 红叉** | 仓库 Actions 里bundle exec jekyll build报错退出 1，线上站不更新 | 02 / 03 构建错误 |
| **首页一片空白** | 能访问但什么都不渲染，或构建绿了仍空白 | 04 首页空白 |
| **侧边栏/目录不显示** | 文章页或首页没有左侧栏，宽屏也没有 | 05 侧边栏 |

任何症状先做这三步通用检查

| 步 | 动作 | 看什么 |
|---|---|---|
| 1 | 开 F12 → Console / Network | 红字 JS 报错、CSS/JS 404 |
| 2 | 仓库 Actions 最新一次运行 | 是不是红叉、报错原文是哪一句 |
| 3 | 改完_config.yml后重启jekyll serve | 配置改动必须重启才生效 |

## 02 · 构建错误一：Invalid date 与 vendor 目录误处理（00306 / 00309）

报错长这样：Invalid date '<%= Time.now.strftime(...) %>'，路径指向vendor/bundle/ruby/.../jekyll-3.10.0/lib/site_template/_posts/0000-00-00-welcome-to-jekyll.markdown.erb。原因是 Jekyll 把装在 vendor 里的 jekyll gem 自带模板文件当成文章处理了——那文件里的日期是 ERB 模板语法，不是真日期。

主修法：_config.yml 里把 vendor 整个排除（照录）

```
exclude:
  - vendor
  - Gemfile
  - Gemfile.lock
```

更完整的排除清单（00309 给出的版本）

```
exclude:
  - "*.gem"
  - "*.gemspec"
  - vendor
  - vendor/bundle
  - .bundle
  - docs
  - tools
  - README.md
  - LICENSE
  - purgecss.js
  - "*.config.js"
  - "package*.json"
```

<details open><summary>同一段日志里还可能藏着的另一个错：Gemfile 语法<span>00309</span></summary><div><ul><li>报错：<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">There was an error parsing Gemfile: syntax error, unexpected end-of-input, expecting end</span>，通常在第 22 行附近。</li><li>真因：那行<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"># bundle lock --add-platform x86_64-linux</span>被误去了注释（丢了<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">#</span>），或前面的<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">group ... do</span>缺<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">end</span>。</li><li>修法：确认注释行以<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">#</span>开头；每个<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">group ... do</span>都有配对的<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">end</span>。</li></ul></div></details>

<details><summary>同一次排查中揪出的 YAML 重复字段<span>00309</span></summary><div><ul><li>同一个文件里写了两行<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">title:</span>（<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">海上升明月</span>与<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">地平线</span>），后者覆盖前者，留一个即可。</li><li><span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">jekyll-archives.permalinks</span>下<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">category: /categories/:name/</span>重复了两遍，删一行。</li><li>已经用<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">remote_theme</span>的，把旧的<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">theme: jekyll-theme-chirpy</span>删掉，避免冲突。</li></ul></div></details>

## 03 · 构建错误二：缺插件 gem（include-cache / parser-gfm / remote-theme）（00308 / 00309）

这类报错都是Dependency Error: Yikes! ... don't have XXX或cannot load such file -- XXX。共同点：光改 _config.yml 不够，Gemfile 与 plugins 两边都要列。

| 报错关键字 | 缺的东西 | 怎么补（两边都要） |
|---|---|---|
| don't have jekyll-include-cache | Chirpy 依赖的 include 缓存插件 | Gemfile 加gem "jekyll-include-cache"；_config.yml 的 plugins 加- jekyll-include-cache |
| don't have kramdown-parser-gfm+ Conversion error | GFM 解析器（写了 GFM 语法的文章转不动） | Gemfile 加gem "kramdown-parser-gfm"；清理 vendor 与 Gemfile.lock 后重装 |
| undefined method 'version' for MockGemspec | jekyll-remote-theme 与 Jekyll 4.3.4 不兼容 | Gemfile 把 jekyll 降到~> 3.10.0，remote-theme 锁~> 0.4.3 |

00308 的纯网页操作法（无本地命令行）：三步

```
1. 仓库根目录新建 Gemfile，写入：
   source "https://rubygems.org"
   gem "jekyll", "~> 4.3.0"
   gem "jekyll-include-cache"

2. _config.yml 的 plugins 列表加一行：
   plugins:
     - jekyll-remote-theme
     - jekyll-archives
     - jekyll-sitemap
     - jekyll-feed
     - jekyll-paginate
     - jekyll-seo-tag
     - jekyll-include-cache      # ← 这行

3. Commit → 看 Actions 绿勾
```

<details><summary>Ruby 3.4+ 的警告与最终推荐 Gemfile<span>00309</span></summary><div><ul><li>日志里<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">base64 / bigdecimal / csv ... will no longer be part of default gems starting Ruby 3.4.0</span>只是警告，不致命；想消音就在 Gemfile 里显式声明<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">gem &quot;csv&quot;</span>、<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">gem &quot;base64&quot;</span>、<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">gem &quot;bigdecimal&quot;</span>、<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">gem &quot;webrick&quot;</span>。</li><li>遇到 MockGemspec version 报错时，最稳的做法是整体降 Jekyll 到 3.10.0——这是 Chirpy 官方测试过的版本，而不是继续在 4.3.4 上打补丁。</li><li>换 Markdown 处理器是兜底：<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">gem &quot;commonmarker&quot;</span>，_config.yml 写<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">markdown: CommonMark</span>。</li></ul></div></details>

## 04 · 首页空白：用二分定位法逐层排除（00305 / 00316 / 00322）

00316 这个案例最有价值：构建绿了首页还是空白，靠「逐层降级测试」最终锁定是 Chirpy 的 CSS/JS 没加载，而不是 Jekyll 本身坏了。下面就是那套二分流程。

| 这一步测什么 | 怎么做 | 能显示 → 说明 / 空白 → 说明 |
|---|---|---|
| **托管本身** | 根目录放一个纯静态index.html（无 Jekyll），提交 | 能显示 → GitHub Pages 托管正常，问题在 Jekyll；仍空白 → 仓库/Pages 设置问题 |
| **Jekyll 基础** | index.md 改用layout: default，写一句测试文字 | 能显示 → Jekyll 构建与 Markdown 正常，问题在 Chirpy 主题；仍空白 → 配置/文件结构问题 |
| **Chirpy home 布局** | 改回layout: home，最小 Chirpy 配置 | 空白 → 问题集中在 Chirpy 的 home 布局与它的 CSS/JS 资源加载 |
| **资源加载** | F12 → Network，看 CSS/JS 是否 404；看生成的_site/index.html是否真的有内容 | 有内容但浏览器空白 = 样式/脚本没加载；文件本身空 = 没生成出来 |

首页空白前的文件结构检查表（00316）

```
.
├── .github/workflows/pages.yml
├── _config.yml
├── index.md                 # 必须 layout: home
├── _posts/                  # 至少一篇文章，否则首页没列表
│   └── 2024-01-01-welcome.md
├── _tabs/
│   ├── archives.md           # layout: archives
│   ├── categories.md         # layout: categories
│   └── tags.md               # layout: tags
└── assets/img/avatar.jpg     # 头像（可暂时去掉 avatar 配置）
```

<details><summary>00316 另一个真实坑：Gemfile 重复声明同一 gem<span>00316</span></summary><div><ul><li>症状：<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">jekyll-paginate</span>在全局写了一次、又在<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">group :jekyll_plugins</span>里写了一次，重复声明导致构建不稳。</li><li>修法：插件只在<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">group :jekyll_plugins</span>组里声明一次，全局别再写。</li><li>00305 强调：新建仓库走<b>Chirpy Starter 模板</b>的<span style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">Use this template</span>，不要 Fork 主仓库；Settings → Pages 的来源选<b>GitHub Actions</b>，别选 Deploy from a branch；Settings → Actions → General 的 Workflow permissions 选<b>Read and write</b>。</li></ul></div></details>

> **从「能工作的静态页」迁移到 Jekyll 的纪律**
> - 静态 index.html 能显示时先提交这个工作状态，再动 Jekyll——出问题能立刻退回去。
> - 迁过去后临时用静态页，记得在_config.yml的exclude里排掉临时index.html，否则两个首页会打架。
> - 一次只加一个功能，加完提交看结果，别一把梭。

## 05 · 侧边栏不显示：先别改代码，先拉宽窗口（00322）

Chirpy 的侧边栏（文章目录/作者栏）是响应式的——窄屏/手机上自动隐藏是**设计行为**，不是 bug。00322 里 Chirpy 7.4 的「侧边栏消失」，第一步就是把浏览器拉宽验证。

| 排查点 | 怎么查 / 修 |
|---|---|
| **窗口宽度** | 先把浏览器窗口拉宽，看侧边栏是否出现；手机/窄屏下不显示是正常的 |
| **配置与重启** | show_sidebar: true改过必须重启jekyll serve才生效；确认文章用的layout本身带侧边栏组件 |
| **F12 Console** | 红字 JS 报错会让控制侧边栏显隐的脚本失效；顺带看 Network 有没有 JS 404 |
| **自定义 CSS 冲突** | 自己加的assets/css/*.scss里有没有display: none/visibility: hidden压到侧边栏；先临时移走自定义样式验证 |
| **主题版本** | Chirpy 7.2.4+ 修过一个侧边栏响应式 bug；版本太旧就升级到最新稳定版 |

<details><summary>00322 给的「强行让侧边栏在桌面端显示」最小 CSS<span>00322</span></summary><div><ul><li>如果拉宽后仍不显示，可先加这段最小化验证（放到自定义样式里）：</li></ul><pre>/* 最小化修复 - 加到现有 CSS */ .sidebar { display: block !important; } @media (max-width: 767px) { .sidebar { display: none !important; } }</pre><ul><li>注意：00322 后续按这段改完配置后反而「首页直接空白了」——这说明大段自定义 SCSS/JS 本身可能引入了新错误。真到那一步，回到第 04 节的二分法，先把自定义文件全部移出，恢复默认主题再说。</li></ul></div></details>
