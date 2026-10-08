---
title: "首页头像点击「关于」页面开发"
description: "Jekyll Chirpy 首页左上角头像点击进入「关于」页面的需求整理与实现，含侧边栏折叠、主题切换与 Front Matter。"
pubDatetime: 2025-10-07
category: "建站与技术"
kind: "长文"
tags: ["Jekyll Chirpy", "头像关于页", "侧边栏折叠", "主题切换", "Front Matter"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00182-2025-10-06 需求整理：首页左上角头像点击进入「关于」（初版方案，含主题初始化、布局、文章系统、媒体页、访客统计与完整首页代码）00184-2025-10-07 同题迭代：定站名为「海上生明月」，侧边栏改为左侧折叠栏并重排导航顺序

## 01 · 需求规格与整体布局（00182 / 00184）

用户硬性前提：**从零开始、所有文件由代码生成、全程只能在网页端操作**（本地不装环境）。技术选型固定为 Jekyll + Chirpy 主题，GitHub 用户名 seamoonappear，00184 轮把站名定为「海上生明月」，并把布局从「顶部导航 + 侧边头像」改为**左侧折叠栏**。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00184 · 2025-10-07</span><h3>左侧折叠栏的自上而下顺序（改版定稿）</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:90px">顺序</th><th style="width:170px">区块</th><th>内容要点</th></tr></thead><tbody><tr><td>1</td><td><b>头像</b></td><td>左上角头像，点击进入「关于我」页面；头像旁挂微信 / QQ / 微博分享图标，以及黑 / 灰背景的风格切换按钮。</td></tr><tr><td>2</td><td>一句话简介</td><td>作者 bio。</td></tr><tr><td>3</td><td>所在位置</td><td>地理位置显示。</td></tr><tr><td>4</td><td>导航菜单</td><td>首页、Blog、媒体、归档、标签、分类、关于我、访问统计。</td></tr><tr><td>5</td><td>访客统计</td><td>侧边栏底部挂访问量统计。</td></tr></tbody></table></div><p style="margin-bottom:0">顶部一级导航均匀排列「文章 / 媒体」，二级导航在点开一级页面后才出现（文章页下挂归档、标签、职场、笔记、知识库、百科、情感）。</p></div></div>

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">首页与文章列表</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>首页列表</dt><dd>每篇文章显示标题、日期、标签；支持文章置顶；列表右侧显示热门标签。</dd><dt>文章页布局</dt><dd>左侧文章正文，右侧热门标签 + 分类列表；每篇文章底部有评价系统，需填昵称才能留言。</dd><dt>分类体系</dt><dd>职场、流程图、笔记、知识库、百科、情感、其他。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">媒体页面与文章更新</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>媒体二级导航</dt><dd>书籍、影视、视频（嵌入媒体）、音乐、驻足点、随手拍、其他爱好；点击二级导航切换对应内容。</dd><dt>文章更新</dt><dd>通过 Front Matter + Markdown 文件管理；支持网页端上传 Markdown，不依赖本地部署。</dd></dl></div></div>

## 02 · 头像点击与侧边栏实现（00182）

「头像点击进关于」的核心就是把头像包成一个指向`/about/`的链接；社交分享与主题切换按钮并排放在头像旁边。Chirpy 用`_includes/sidebar.html`定制侧边栏。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00182 · 2025-10-06</span><h3>侧边栏结构：头像链接 + 社交分享 + 主题切换</h3></div><div style="padding:14px 16px"><p>&lt;div class=&quot;profile-wrapper&quot;&gt; &lt;!-- 头像：点击进入关于我 --&gt; &lt;a href=&quot;/about/&quot; class=&quot;profile-avatar&quot;&gt; &lt;img src=&quot;{{ site.author.avatar | relative_url }}&quot; alt=&quot;{{ site.author.name }}&quot;&gt; &lt;/a&gt; &lt;!-- 社交分享图标 --&gt; &lt;div class=&quot;social-share&quot;&gt; &lt;a href=&quot;javascript:void(0)&quot; onclick=&quot;shareWechat()&quot; title=&quot;微信&quot;&gt; &lt;i class=&quot;fab fa-weixin&quot;&gt;&lt;/i&gt; &lt;/a&gt; &lt;a href=&quot;https://connect.qq.com/widget/sharewebsite/index.html?url={{ site.url }}&quot; title=&quot;QQ&quot; target=&quot;_blank&quot;&gt; &lt;i class=&quot;fab fa-qq&quot;&gt;&lt;/i&gt; &lt;/a&gt; &lt;a href=&quot;http://service.weibo.com/share/share.php?url={{ site.url }}&amp;title={{ site.title }}&quot; title=&quot;微博&quot; target=&quot;_blank&quot;&gt; &lt;i class=&quot;fab fa-weibo&quot;&gt;&lt;/i&gt; &lt;/a&gt; &lt;/div&gt; &lt;!-- 主题切换按钮 --&gt; &lt;button id=&quot;theme-toggle&quot; class=&quot;btn btn-sm btn-theme-toggle&quot; title=&quot;切换主题&quot;&gt; &lt;i class=&quot;fas fa-palette&quot;&gt;&lt;/i&gt; &lt;/button&gt; &lt;/div&gt;</p><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>实现要点</h5><ul><li>头像本身即<code>&lt;a href=&quot;/about/&quot;&gt;</code>，无需额外 JS 跳转；Chirpy 原生支持<code>/about/</code>页面。</li><li>微信分享没有网页端直链，需准备二维码图，点击后弹出「请使用微信扫描分享」。</li><li>QQ 走<code>connect.qq.com/widget/sharewebsite</code>，微博走<code>service.weibo.com/share/share.php</code>，均带当前页 url 与 title。</li></ul></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00182 · 2025-10-06</span><h3>明暗主题切换：localStorage + data-mode</h3></div><div style="padding:14px 16px"><p>主题切换按钮写在<code>assets/js/theme-toggle.js</code>：读取 localStorage 里的 theme，默认 light；点击在 light / dark 间切换，把结果写到<code>&lt;html data-mode&gt;</code>并持久化，刷新不丢。</p><p>class ThemeToggle { constructor() { this.theme = localStorage.getItem('theme') || 'light'; this.init(); } init() { this.applyTheme(this.theme); this.createToggleButton(); } applyTheme(theme) { document.documentElement.setAttribute('data-mode', theme); localStorage.setItem('theme', theme); } createToggleButton() { const btn = document.getElementById('theme-toggle'); if (btn) { btn.addEventListener('click', () =&gt; { this.theme = this.theme === 'light' ? 'dark' : 'light'; this.applyTheme(this.theme); }); } } } document.addEventListener('DOMContentLoaded', () =&gt; new ThemeToggle());</p></div></div>

## 03 · 导航菜单与文章系统（00182）

导航在`_data/navigation.yml`里配置一级 + 二级菜单；文章用 Front Matter + Markdown 管理，首页列表取标题 / 日期 / 标签并支持置顶，文章页左正文右侧栏。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00182 · 2025-10-06</span><h3>导航菜单配置（_data/navigation.yml）</h3></div><div style="padding:14px 16px"><p>header: - title: &quot;首页&quot; url: &quot;/&quot; - title: &quot;文章&quot; url: &quot;/posts/&quot; children: - title: &quot;归档&quot; url: &quot;/archives/&quot; - title: &quot;标签&quot; url: &quot;/tags/&quot; - title: &quot;职场&quot; url: &quot;/categories/职场/&quot; - title: &quot;笔记&quot; url: &quot;/categories/笔记/&quot; - title: &quot;知识库&quot; url: &quot;/categories/知识库/&quot; - title: &quot;百科&quot; url: &quot;/categories/百科/&quot; - title: &quot;情感&quot; url: &quot;/categories/情感/&quot; - title: &quot;媒体&quot; url: &quot;/media/&quot; children: - title: &quot;书籍&quot; url: &quot;/media/books/&quot; - title: &quot;影视&quot; url: &quot;/media/movies/&quot; - title: &quot;视频&quot; url: &quot;/media/videos/&quot; - title: &quot;音乐&quot; url: &quot;/media/music/&quot; - title: &quot;驻足点&quot; url: &quot;/media/travel/&quot; - title: &quot;随手拍&quot; url: &quot;/media/photos/&quot; - title: &quot;其他爱好&quot; url: &quot;/media/hobbies/&quot; - title: &quot;关于我&quot; url: &quot;/about/&quot;</p><p style="margin-bottom:0">二级导航只在点开一级页面后显示；00184 改版后侧边栏顺序为首页 → Blog → 媒体 → 归档 → 标签 → 分类 → 关于我 → 访问统计。</p></div></div>

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">文章 Front Matter 模板</h3><p style="margin-bottom:0">--- title: 文章标题 date: 2025-10-06 21:47 categories: 职场 tags: [标签一, 标签二] pin: true # 置顶 ---</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">网页端写作流程</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>新建文章</dt><dd>在仓库<code>_posts/</code>新建 Markdown，文件名<code>YYYY-MM-DD-标题.md</code>，按模板填 Front Matter。</dd><dt>上传方式</dt><dd>全程网页端操作，GitHub 网页新建 / 上传文件，GitHub Actions 自动构建部署。</dd><dt>热门标签</dt><dd>首页列表右侧由标签聚合页自动生成高频标签云。</dd></dl></div></div>

## 04 · Media 页面与访客统计（00182）

Media 页面用二级导航切换书籍 / 影视 / 视频 / 音乐 / 驻足点 / 随手拍 / 其他爱好，视频类页面嵌入媒体播放器；访客统计挂在侧边栏底部，用第三方统计脚本接入。

| 功能 | 实现方式（照录方案） |
|---|---|
| 媒体二级导航 | 七个子页面各自独立，点击二级导航显示对应内容；视频页面内嵌播放器 iframe。 |
| 评论 / 留言 | 使用 Disqus，在`_config.yml`填`disqus.shortname`；留言需填写昵称。 |
| 访客统计 | 侧边栏底部接入统计脚本（百度统计 / Google Analytics 二选一），在`_config.yml`填对应 ID。 |
| 社交链接 | `_data/contact.yml`配置 GitHub、邮箱、微信二维码、QQ、微博等链接与图标。 |

## 05 · 技术栈与部署发布（00182）

整套方案的前提是「纯网页端、不本地部署」，因此建仓、改配置、写文章全部在 GitHub 网页完成，构建交给 GitHub Actions。

| 步骤 | 操作 |
|---|---|
| Fork 主题 | 访问 cotes2020/jekyll-theme-chirpy，点 Fork，仓库重命名为`seamoonappear.github.io`。 |
| 基础配置 | 改`_config.yml`：title、url`https://seamoonappear.github.io`、author.name / avatar / bio / email、lang zh-CN、timezone Asia/Shanghai。 |
| 插件与构建 | 启用 jekyll-paginate、jekyll-seo-tag 等插件；GitHub Pages 用 Actions 构建部署。 |
| 上线 | 推送后 Actions 自动构建，访问 seamoonappear.github.io 即为「海上生明月」。 |

> **注意事项（照录）**
> - 所有文件由代码生成，全程网页端操作，不本地安装 Ruby / Jekyll 环境。
> - Disqus、百度 / Google 统计需先去对应官网注册拿 shortname / ID，再填回配置。
> - 头像与社交二维码需先放到`assets/img/`，配置里用相对路径引用。
