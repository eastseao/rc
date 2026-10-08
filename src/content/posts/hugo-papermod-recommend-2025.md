---
title: "Hugo 手机建站·PaperMod 主题·国内站点推荐"
description: "手机搭建 Hugo 个人网站需求梳理、PaperMod 主题 ZIP 上传、国内 GitHub Pages 个人网站推荐与建站论坛。"
pubDatetime: 2025-10-08
category: "建站与技术"
kind: "长文"
tags: ["Hugo", "PaperMod", "Codespaces", "GitHub Actions", "建站社区"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00178-2025-10-06 手机搭建Hugo个人网站需求梳理00186-2025-10-08 推荐国内GitHub Pages个人网站00156-2025-10-02 推荐个人网站设计建站论坛

## 01 · 手机搭建 Hugo：需求与挑战梳理（00178）

GitHub 用户名`hdbuyer`，想搭`hugo-theme-den`主题的个人站，是新手、**只希望靠手机操作**。难点在于 Hugo 传统上强依赖电脑命令行，得用云环境绕过去。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00178 · 2025-10-06</span><h3>四步任务与应对策略</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:130px">步骤</th><th>核心任务</th><th>挑战与对策</th></tr></thead><tbody><tr><td><b>环境准备</b></td><td>装 Hugo、建站点、初始化 Git</td><td>手机跑不了命令行 → 用手机浏览器开云环境（GitHub Codespaces / GitPod）。</td></tr><tr><td><b>主题配置</b></td><td>获取并应用 hugo-theme-den</td><td>主题靠 Git 拉取 → 云环境里用 git submodule；参考主题作者示例配置。</td></tr><tr><td><b>内容管理</b></td><td>写文章、管结构</td><td>手机写 Markdown 不便 → 云环境 Web 编辑器 + GitHub 手机 App 微调。</td></tr><tr><td><b>部署发布</b></td><td>让站公开可访问</td><td>推到 GitHub，用 GitHub Actions 自动构建部署到 Pages。</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>核心思路（照录）</b>：用云开发环境替代电脑完成命令行与初始搭建，之后靠 GitHub 手机 App 做内容维护。备选——先用电脑把 Hugo 环境与主题初始搭好推上去，之后全靠手机 App 管内容。</div></div></div>

## 02 · Codespaces 四步操作与关键代码（00178）

手机浏览器开 GitHub Codespaces 当作云端 VS Code，分四步：建仓库与环境 → 拉主题配配置 → 写文章预览 → Actions 部署。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00178 · 2025-10-06</span><h3>关键命令与配置</h3></div><div style="padding:14px 16px"><p>① 建站点 + 拉主题为子模块 + 复制示例配置：</p><pre>hugo new site . --force git submodule add https://github.com/iswbm/hugo-theme-den.git themes/hugo-theme-den cp -r themes/hugo-theme-den/exampleSite/* .</pre><p>改<code>config.toml</code>三项：</p><pre>baseURL = &quot;https://hdbuyer.github.io/&quot; title = &quot;hdbuyer的个人网站&quot; theme = &quot;hugo-theme-den&quot;</pre><p>② 建文章并本地预览（<code>-D</code>含草稿，<code>--bind</code>允许外部访问）：</p><pre>hugo new posts/my-first-post.md hugo server -D --bind 0.0.0.0</pre><p>③ 在<code>.github/workflows/hugo.yml</code>放标准 Hugo 部署工作流（push 到 main → checkout 含子模块 → setup-hugo →<code>hugo --minify</code>→ deploy 到 gh-pages）。</p><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>三个必须记住的点</h5><ul><li>部署要 Personal Access Token（勾<b>repo</b>权限），存到仓库 Secrets 名为<code>PERSONAL_TOKEN</code>。</li><li>推代码：<code>git add .</code>→ 配 user.name/email →<code>commit</code>→<code>push</code>。</li><li>最后到 Settings → Pages，Source 选<b>GitHub Actions</b>；访问<code>https://hdbuyer.github.io</code>。</li></ul></div></div></div>

## 03 · 国内优秀个人站参考与找主题（00186）

想「推荐基于 GitHub Pages、并标注主题的国内个人站」。笔记坦言搜索结果里的站点多未明确说明技术栈，更多当作设计与内容的典范。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00186 · 2025-10-08</span><h3>六位国内开发者个人站</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">开发者</th><th>网站</th></tr></thead><tbody><tr><td>阮一峰</td><td>ruanyf.github.io</td></tr><tr><td>张鑫旭</td><td>www.zhangxinxu.com</td></tr><tr><td>大漠（W3CPlus）</td><td>www.w3cplus.com</td></tr><tr><td>颜海镜</td><td>yanhaijing.com</td></tr><tr><td>杜瑶</td><td>doyoe.com</td></tr><tr><td>BYVoid（郭家宝）</td><td>www.byvoid.com</td></tr></tbody></table></div><p style="font-size:13.5px;color:inherit">注意：这些站风格各异、很多年就开始维护，<b>不一定都用 GitHub Pages</b>，主要供借鉴设计思路与内容规划。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00186 · 2025-10-08</span><h3>自己找同类站与主题的方法</h3></div><div style="padding:14px 16px"><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>搜仓库</dt><dd>GitHub 搜<code>username.github.io</code>，看 README /<code>_config.yml</code>里写的主题。</dd><dt>看主题仓库</dt><dd>热门 Jekyll 主题仓库 README 的 Wiki / Live Demo 通常列了使用者：Minimal Mistakes（功能全）、Chirpy（设计精美）、al-folio（学术）。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>主题站</dt><dd>jekyllthemes.io 汇集大量 Jekyll 主题，多带实时预览与使用说明。</dd></dl></div></div></div></div>

## 04 · 建站能用的论坛与社区（00156）

设计个人网站时去哪问、去哪找灵感：分「技术问答社区」与「开源论坛软件」两类。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00156 · 2025-10-02</span><h3>技术问答与社区</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:160px">平台</th><th>特点</th></tr></thead><tbody><tr><td>Stack Overflow</td><td>全球编程问答，前端问题基本都有答案。</td></tr><tr><td>Reddit（r/webdev 等）</td><td>信息更新快，看行业动态、聊工具。</td></tr><tr><td>DEV Community</td><td>开发者博客/教程，内容质量高。</td></tr><tr><td>掘金</td><td>国内活跃前端社区，技术文章丰富。</td></tr><tr><td>CSDN</td><td>中国最大 IT 社区之一，覆盖广。</td></tr><tr><td>SegmentFault 思否</td><td>中文技术问答，问答质量高。</td></tr></tbody></table></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00156 · 2025-10-02</span><h3>开源论坛软件（想自己搭社区时用）</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:160px">软件</th><th>特点</th></tr></thead><tbody><tr><td>Discourse</td><td>功能全面的现代论坛软件，第三方集成丰富。</td></tr><tr><td>NodeBB</td><td>基于 Node.js，实时交互、速度快。</td></tr><tr><td>Discuz!</td><td>国内经典论坛系统，用户群庞大。</td></tr><tr><td>Vanilla</td><td>开源免费，主题与插件机制灵活。</td></tr><tr><td>Homeland</td><td>开源社区系统，响应式 + Markdown，对 SEO 友好。</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>用法建议</b>：新手或遇具体 bug 先上 Stack Overflow / CSDN；想学系统知识、找灵感多逛掘金 / DEV / Reddit；想给网站加论坛功能再上 Discourse / NodeBB / Discuz!。提问前先搜，绝大多数基础问题已有答案。</div></div></div>
