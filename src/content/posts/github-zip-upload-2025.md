---
title: "GitHub ZIP 解压上传与构建 404 排错"
description: "ZIP 不能在线解压、Git/网页端上传、PaperMod 子模块、Hugo Actions 自动构建与远程主题 404 排错。"
pubDatetime: 2025-10-07
category: "建站与技术"
kind: "手册"
tags: ["ZIP 解压", "Git LFS", "PaperMod 子模块", "远程主题 404"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00177-2025-10-06 GitHub ZIP 文件解压方法总结00179-2025-10-06 PaperMod 主题 ZIP 上传教程00180-2025-10-06 解压文件上传 GitHub 指南00181-2025-10-06 GitHub Pages 构建失败：远程主题 404 错误

## 01 · GitHub 不能在线解压 ZIP：三条路（00177）

「上传了一个 zip 到库里怎么解压」——直接在仓库里在线解压是**不可能的**，GitHub 没这功能。按场景选下面一条。

| 方法 | 适用 | 怎么做 |
|---|---|---|
| **本地解压** | 个人查看/改文件 | 仓库里 Download 下来 → 本地解压 →（可选）再 git push 回去。 |
| **GitHub Actions** | CI/CD 自动处理 | 写`.github/workflows/unzip.yml`，push 含 zip 的提交自动解压。 |
| **前端 JSZip** | Web 应用内浏览器解压 | 引入 JSZip，用户选文件后在浏览器读解压，不经仓库。 |

> **给普通用户的结论**：快速查看就**下载到本地解压**最简单；要自动化才上 Actions；要网页里在线解压才用 JSZip。

## 02 · 解压后怎么上传：Git 命令行 vs 网页端（00180）

解压出来一堆文件和文件夹，往哪传？两条路，按是否要版本控制选。

| 对比 | Git 命令行（推荐） | GitHub 网页端 |
|---|---|---|
| **适合** | 要版本控制、频繁更新、文件较大 | 快速、一次性、文件较小 |
| **版本管理** | 完整支持 | 仅初始提交 |
| **单文件上限** | 网页端 25MB；**>100MB 用 Git LFS** | 网页端 ≤ 25MB |

> **00180 实录排错**
> - **文件夹拖不进网页**：浏览器安全限制/文件夹过大——改用 Git 命令行（最可靠）、GitHub Desktop 图形界面、逐子文件夹上传，或重新压缩成 ZIP 再传。
> - **push 被拒**（failed to push some refs）：远程有本地没有的更新，先`git pull origin main --rebase`再 push。
> - **认证**：GitHub 已不支持账户密码，用**个人访问令牌（PAT，勾 repo 权限）**当密码。

## 03 · PaperMod 主题：ZIP 还是子模块装（00177 / 00179）

PaperMod 文件夹很大，要么下 ZIP，要么用 git 拉。网页端没法本地部署时，源笔记直接让你写`.gitmodules`声明子模块。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">ZIP 方式</h3><ol style="margin:0;padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:6px">从<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">releases</code>下载 Source code (zip)。</li><li style="margin-bottom:6px">解压 → 把文件夹<b>重命名为 PaperMod</b>。</li><li>整体放进<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">themes/</code>，确保文件<b>直接在 themes/PaperMod 下、不嵌套一层</b>。</li></ol></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">子模块 / 克隆</h3><div style="margin:14px 0"><span># .gitmodules（网页端直接建文件）</span>[submodule &quot;themes/PaperMod&quot;] path = themes/PaperMod url = https://github.com/adityatelange/hugo-PaperMod.git branch = &quot;master&quot;</div><p style="font-size:13.5px;color:inherit;line-height:1.72">或本地<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">git clone … themes/PaperMod --depth=1</code>。记得 Hugo 用<b>扩展版</b>，配置<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">theme: &quot;PaperMod&quot;</code>。</p></div></div>

## 04 · Hugo + PaperMod 不本地部署：Actions 自动构建（00177）

用户「是新手、不要本地部署」，于是全程在网页端用 GitHub Actions 自动跑 Hugo 构建。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00177 · 两个仓库 + 一个工作流</span><h3>源码仓库与托管仓库分离</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0;margin:0 0 14px"><table><thead><tr><th style="width:180px">项</th><th>说明</th></tr></thead><tbody><tr><td><b>源码仓库</b></td><td>放 Hugo 源文件、主题、配置、文章（即用已建好的<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">blog</code>）。</td></tr><tr><td><b>托管仓库</b></td><td>必须叫<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">&lt;用户名&gt;.github.io</code>，存构建产物。</td></tr><tr><td><b>工作流</b></td><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">.github/workflows/deploy.yml</code>：checkout(submodules) → setup Hugo →<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">hugo --minify</code>→ upload artifact(./public) → deploy to Pages。</td></tr><tr><td><b>Pages 源</b></td><td>托管仓库 Settings → Pages → Source 选<b>GitHub Actions</b>。</td></tr><tr><td><b>发文章</b></td><td>在<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">content/posts/</code>新建 md 并 push，Actions 自动构建发布。</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>关键点</b>：文章头里<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">draft: false</code>才会发布（默认 true 的草稿不构建）；<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">baseURL</code>要替换成你的<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">https://用户名.github.io/</code>。</div></div></div>

## 05 · Pages 构建失败：远程主题 404 怎么排（00181）

00181 给的真实构建日志：远程主题`chirpythemes/chirpy@v6.0.0`在下载 zip 时**404 Not Found**，构建挂掉。

| 排查动作 | 说明 |
|---|---|
| **验证链接** | 浏览器直接打开报错那个 codeload URL，也 404 就坐实主题资源不存在。 |
| **核对仓库与版本** | 确认仓库名/owner 对不对；releases/标签里`v6.0.0`是否真存在——常是版本号拼错。 |
| **目录结构兼容** | 主题资源得放在`assets/_layouts/_includes/_sass`标准目录，否则被忽略。 |
| **退一步** | 用默认分支替代版本：`remote_theme: chirpythemes/chirpy`；或 Fork 主题本地化后自建。 |
