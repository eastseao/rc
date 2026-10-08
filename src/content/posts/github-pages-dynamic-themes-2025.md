---
title: "GitHub Pages 动态博客方案与官方主题"
description: "静态生成器方案对比、Beautiful Jekyll 远程主题、baseurl/tabs 坑、官方主题使用指南与功能拓展清单。"
pubDatetime: 2025-10-14
category: "建站与技术"
kind: "长文"
tags: ["静态生成器", "remote_theme", "Beautiful Jekyll", "baseurl"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00158-2025-10-02 GitHub 搭建动态博客方案推荐00195-2025-10-09 GitHub 静态网页功能拓展清单00233-2025-10-13 GitHub 个人博客推荐与技术方案分析00247-2025-10-14 GitHub Pages 官方主题及使用指南

## 01 · 需求：手机上就能更新的 md 动态博客（00158 / 00233）

原始诉求很明确：在 GitHub 上建一个**易维护的动态个人博客，文章主要用 md 格式，关键是手机上就能更新内容**。要的是框架、结构、语言。00233 顺手列了一批做得好的 GitHub 个人博客作参考。

| 参考博客 | 技术方案 | 特点 |
|---|---|---|
| **Yash Goel** | 纯 HTML + CSS | 极致简洁、无 JS，专注内容展示。 |
| **Nicholas Clooney** | Eleventy | 前端技术向，自动化图片处理、主题切换。 |
| **daijiale** | Hexo | 稳定运行多年，展示 Hexo 的长期可靠性。 |
| **LeuisKen** | GitHub Issues | 直接用 Issues 写文章，极简管理。 |
| **Tech-shrimp** | Gmeek（基于 Jekyll） | 超轻量，也支持 Issues 写作。 |
| **Hux** | Jekyll | 成熟热门的 Jekyll 主题，很多人基于它。 |

> **选型口径（源笔记原话）**：侧重写作体验选 Jekyll 或基于 Issues 的方案；热衷前端折腾选 Eleventy 或纯手工；求快速稳定就选成熟 Jekyll/Hexo 主题。仓库命名搜`username.github.io`、`jekyll blog stars:>100`能挖更多案例。

## 02 · GitHub Pages + 静态网站生成器（基础通用方案）（00158）

源笔记给新手详细展开了这条「基础通用方案」：写 md → 生成器转 HTML → GitHub Pages 托管，免服务器、免数据库。关键落地是把博客放进**已有个人主页仓库的 blog 子文件夹**，在 blog 下建 Jekyll 项目。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">方案组成</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>静态托管</dt><dd>GitHub Pages，直接从仓库出静态站点。</dd><dt>生成器</dt><dd>Jekyll（Pages 原生支持）/ Hexo / Eleventy 等，把 _posts 里的 md 渲染成 HTML。</dd><dt>写作语言</dt><dd>Markdown；界面用 HTML + CSS。</dd><dt>手机更新</dt><dd>手机浏览器直接编辑仓库里的 md，push 后 Pages 自动重建——这正是「手机就能更新」的落点。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">子文件夹结构</h3><div style="margin:14px 0">your-repo/ ├── index.html<span># 个人主页（根）</span>└── blog/<span># 博客放这里</span>├── _config.yml ├── index.md └── _posts/</div></div></div>

> **00158 实录：「用了你上面的代码，博客首页现在什么都没有」**
> - 在已有主页的库里加 blog 子目录、又套一层 Jekyll，`baseurl`/ 路径没对上时，首页会整片空白。
> - 排错动作：重新出 blog 文件夹及其子文件夹的完整文件代码；用户名占位符（gervasw）统一替换真实值。

## 03 · 官方主题与第三方主题：Beautiful Jekyll 怎么用（00247）

GitHub 自带一个「主题选择器」；除此之外第三方 Jekyll 主题更丰富。00247 重点把 Beautiful Jekyll 讲透。

| 主题 | 特点 | 启用方式 |
|---|---|---|
| **官方主题选择器** | 仓库 Settings → Pages → Choose/Change theme → 预览 → Select theme，自动应用到 Markdown。 | 网页点选。 |
| **Leap Month** | 专为 Pages 定制，**中文排版优化**、移动端改进。 | `remote_theme: qyxf/leap-month` |
| **Minimal Light** | 简洁学术主页模板、自动暗黑模式。 | `remote_theme: yaoyao-liu/minimal-light` |
| **Beautiful Jekyll** | Dean Attali 开发，开箱即用、响应式、内置评论/分析/社交图标。 | Fork 到`用户名.github.io`，或`remote_theme: daattali/beautiful-jekyll` |

> **高频坑：remote_theme 地址写错**
> - 错：`mmistakes/beautiful-jekyll@master`（这个组合根本不存在）。
> - 对：`daattali/beautiful-jekyll`；建议锁版本`@5.0.0`，避免主题自更新把站点搞坏。

## 04 · baseurl 与 tabs 子目录：链接前缀的坑（00247 / 00158）

当仓库名不是「用户名.github.io」、而是一个普通仓库（如 blog），站点就挂在子路径下，所有 URL 都得带前缀。这是 00247 反复修的配置点。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00247 · 真实配置（用户 seamoonappear / 仓库 blog）</span><h3>子路径部署的完整 _config.yml</h3></div><div style="padding:14px 16px"><div style="margin:14px 0">url: &quot;https://seamoonappear.github.io&quot; baseurl: &quot;/blog&quot;<span># 仓库名是 blog，不是 用户名.github.io</span>nav: - title: &quot;首页&quot; url: / - title: &quot;博客&quot; url: /blog/tabs/blog/ - title: &quot;消费&quot; url: /blog/tabs/media/ - title: &quot;照片&quot; url: /blog/tabs/photo/ - title: &quot;关于我&quot; url: /blog/tabs/about/</div><div style="overflow-x:auto;margin:16px 0;margin:14px 0 0"><table><thead><tr><th style="width:160px">要点</th><th>说明</th></tr></thead><tbody><tr><td><b>子路径</b></td><td>站点地址 =<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">https://seamoonappear.github.io/blog</code>，所有链接带<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">/blog</code>前缀。</td></tr><tr><td><b>tabs 目录</b></td><td>子页面统一放<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">tabs/</code>；每个页面文件里的<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">permalink</code>必须与导航 URL 完全一致。</td></tr><tr><td><b>首页独立</b></td><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">index.md</code>留在根目录，不放进 tabs。</td></tr><tr><td><b>404 排查</b></td><td>出 404 先看 Pages 构建日志，确认文件路径与 permalink。</td></tr></tbody></table></div></div></div>

## 05 · 静态网页功能拓展清单（00195）

00195 给了一张 GitHub 静态网页能加什么的清单，五大类；并针对「日常用笔记本、Word/Excel/PDF 多」的办公场景给了一套侧重。

| 拓展方向 | 举例 |
|---|---|
| **内容展示增强** | 项目橱窗（突破置顶 6 仓库）、数据可视化（D3.js）、个人博客（Jekyll + Markdown）。 |
| **交互与 UX** | 评论（Gitalk / Utterances 基于 Issues）、全站搜索（Lunr.js / Algolia）、在线导航、短网址（404.html + routes.json）。 |
| **个性化与品牌** | 自定义主题（Sass）、动态徽章（Shields.io）、贡献面板（Repobeats）。 |
| **性能与 SEO** | 响应式、sitemap.xml、图片压缩 + CDN。 |
| **集成与自动化** | 自定义域名（CNAME）、GitHub Actions 自动部署。 |

> **办公场景侧重（00195 第二段）**：PDF 互转/编辑/批量、个人模板库（把常用报告合同做成在线模板一键调用）、在线预览与轻量编辑（mammoth.js）、跨设备同步与个人办公导航。新手从导航页或模板库起步，有经验再上评论/自动化。
