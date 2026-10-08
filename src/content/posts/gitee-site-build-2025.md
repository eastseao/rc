---
title: "Gitee / 码云建站指南"
description: "Gitee Pages 免费国内加速、网页端五步建博客、Vue dist/Hexo 进阶、手动更新与移动端 APP 下载。"
pubDatetime: 2025-10-13
category: "建站与技术"
kind: "手册"
tags: ["Gitee Pages", "网页端建仓", "手动更新", "移动端 APP"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00163-2025-10-03 使用 Gitee 创建个人网站指南00235-2025-10-13 用码云搭建个人网站指南00236-2025-10-13 Gitee 移动端应用下载指南

## 01 · 能不能用 Gitee 建站？三条路（00163 / 00235）

可以。Gitee 提供**Gitee Pages**托管静态站，免费、国内平台访问快，适合个人站/博客/作品展示。按技术基础有三条路。

| 方法 | 适合谁 | 做法 |
|---|---|---|
| **直接上传 HTML** | 新手、想快速体验 | 写好 HTML/CSS/JS 传上去即可，最简单。 |
| **部署 Vue/React** | 有前端基础 | 项目打包出`dist`，Pages 部署目录指向它。 |
| **Hexo 静态博客** | 爱写作、想博客功能丰富 | md 写作自动生成站，主题多，适合技术博客。 |

> **一句话定位**：Gitee 建站是「免费、快速、对新手友好」的选择；但据源笔记，Gitee Pages**似乎不支持直接绑定个人域名**，有自定义域名强需求时应考虑 GitHub Pages。

## 02 · 只用网页端、不用命令行建一个博客（00235）

00235 最实用的一段：**「我只能通过网页端操作」**。全程在线建仓、在线建文件、在线开 Pages。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00235 · 五步流程</span><h3>从零到上线</h3></div><div style="padding:14px 16px"><ol style="margin:0;padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:9px"><b>建仓库</b>：gitee.com 登录 → 右上「+」→「新建仓库」；名称如<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">my-blog</code>、可见性选<b>公开</b>、<b>不勾选</b>「用 Readme 初始化」。</li><li style="margin-bottom:9px"><b>建首页</b>：仓库里「新建文件」→ 文件名<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">index.html</code>→ 粘贴一段博客首页模板（header + 若干<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">.post</code>文章卡片）→ 提交。</li><li style="margin-bottom:9px"><b>建文章页</b>：再「新建文件」→<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">post1.html</code>→ 写正文 → 提交。</li><li style="margin-bottom:9px"><b>开 Pages</b>：仓库主页导航「服务」→「Gitee Pages」→ 点绿色「启动」→ 等一两分钟出绿色横幅 + 访问地址。</li><li><b>访问</b>：地址形如<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">https://你的用户名.gitee.io/my-blog</code>。</li></ol></div></div>

> **后续发文章**：复制 post1.html 的结构新建 post2.html，再在 index.html 里复制一份`.post`模块改标题/链接/摘要。

## 03 · 进阶：Vue 打包 dist 与 Hexo（00235）

熟悉流程后，想把现代前端项目或 Hexo 博客搬上来。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">Vue / React 项目</h3><p style="font-size:13.5px;color:inherit;line-height:1.72">项目里<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">npm run build</code>打包，根目录生成<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">dist</code>；开 Pages 时把<b>部署目录指定为 dist</b>即可。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">Hexo 博客</h3><div style="margin:14px 0">npm install -g hexo-cli hexo init myblog hexo new &quot;文章标题&quot; hexo g -d</div><p style="font-size:13.5px;color:inherit;line-height:1.72">前置：装好 Node.js 与 Git；<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">hexo g -d</code>一键生成并部署到码云仓库。</p></div></div>

## 04 · 运维要点：手动更新、相对路径、实名认证（00163 / 00235）

Gitee Pages 和 GitHub Pages 最大的行为差异——**不会自动重新部署**。这是源笔记反复强调的坑。

| 事项 | 说明 |
|---|---|
| **手动更新** | 每次上传/改完文件，都要手动进「服务 → Gitee Pages」点**「更新」/「重新部署」**才生效，不会自动重建。 |
| **实名认证** | 首次开启 Pages 服务可能需要**实名认证**。 |
| **样式丢失** | 部署后 CSS 丢了，尤其站不在根目录时，先查资源引用是不是**相对路径**。 |
| **自定义域名** | 00235 提到可在 Pages 设置填自定义域名并配 CNAME；00163 则说似乎不支持直接绑定——以实际后台为准。 |

## 05 · Gitee 有 APP 吗？（00236）

有，但主要管代码、不适合建站。下表是源笔记整理的两平台客户端。

| 平台 | 应用 | 获取 | 备注 |
|---|---|---|---|
| **iOS** | Giteer For Gitee | App Store 搜「Giteer For Gitee」 | 付费第三方客户端（$1.99），针对 Gitee 优化。 |
| **Android** | Gitee 手机客户端 | Google Play / 应用宝搜「Gitee」 | 官方或官方授权安卓客户端。 |

> **移动端的边界（源笔记原话）**
> - APP 主要功能：查看仓库、管理 Issues、处理 Pull Request、关注项目动态。
> - **上传大量代码、建仓库、跑复杂 Git 指令**这类重活在手机端受限——建站与维护还是桌面端高效。
