---
title: "Obsidian 自动发布 GitHub Pages 与 Git 同步"
description: "三套发布方案对比、Token/BRAT 装插件、published:true 标记、Obsidian Git 全库同步与价格表。"
pubDatetime: 2026-04-07
category: "建站与技术"
kind: "手册"
tags: ["Obsidian", "GitHub Pages", "发布工作流", "Git 同步"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00206-2025-10-10 Obsidian 自动发布 GitHub Pages 博客方案00209-2025-10-10 GitHub Publisher 选择性发布流程指南00210-2025-10-10 Obsidian Git 全库同步方案00211-2025-10-10 BRAT 安装 GitHub Publisher 流程00327-2025-10-25 Obsidian 安装 Git 插件教程00864-2026-04-07 Obsidian 功能优缺点介绍

## 01 · 三套发布方案，先对号入座（00206 / 00210）

核心区别在于「你对 Git 操作和网站生成流程的参与程度」：全库同步最省心，选择性发布最精细，Hexo 集成自动化最高。

| 方案 | 核心插件 | 做什么 | 优点 / 适合谁 |
|---|---|---|---|
| **方案一 全库同步** | Obsidian Git | 自动把整个笔记库同步到 GitHub（建议私有仓库保护内容）；博客生成另行交给 Hugo / Jekyll 或 GitHub Pages。 | 多设备同步简单；适合先解决笔记备份、博客生成独立的人。 |
| **方案二 选择性发布** | GitHub Publisher | 只把带`published: true`标记的笔记发布到指定仓库；可单篇或批量发布。 | 内容管理灵活；适合精细控制哪些笔记成为公开博客。 |
| **方案三 Hexo 集成** | Hexo Auto Updater | 监控`_posts`文件夹变更，自动提交推送 Hexo 源仓库，触发 GitHub Actions 构建并部署到 Pages。 | 发布流程自动化；适合已经用 Hexo、追求写作到部署全自动的人（配置也最复杂）。 |

> **选法**：只想整库备份或博客流程独立 → Obsidian Git；要控制哪些笔记公开 → GitHub Publisher；已用 Hexo 要全自动 → Hexo Auto Updater。无论哪套，建议根目录建`.gitignore`忽略`.obsidian/`、`.DS_Store`、`Thumbs.db`；大量图片用 Git LFS 管理避免仓库膨胀。

## 02 · 准备：建仓库 + 生成 Personal Access Token（00206 / 00327）

两条路（GitHub Publisher 与 Obsidian Git）都要 GitHub 凭证。先建仓库，再拿令牌。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>建仓库</span><h3>仓库怎么建</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>Pages 仓库</dt><dd>建<code>你的用户名.github.io</code>作为 User 站点；或任意命名仓库，在 Settings → Pages 里开启。博客公开就设为<b>public</b>；笔记整库备份建议设为<b>私有</b>。</dd><dt>本地关联</dt><dd>把远程仓库克隆到本地，或把本地笔记文件夹<code>git init</code>后关联远程。</dd><dt>Git 身份</dt><dd>首次提交前先配全局身份：<code>git config --global user.name '你的用户名'</code>与<code>git config --global user.email '你的邮箱'</code>。</dd></dl></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>Token</span><h3>生成 Personal Access Token（classic）</h3></div><div style="padding:14px 16px"><ol style="padding-left:18px;color:inherit;font-size:13.5px;line-height:1.8"><li>登录 GitHub，点右上角头像 →<b>Settings</b>。</li><li>页面一直<b>滚到最底部左下角</b>，进<b>Developer settings</b>（不在左侧导航显眼处）。</li><li>选<b>Personal access tokens → Tokens (classic)</b>→<b>Generate new token (classic)</b>。</li><li>起个好认的名字（如<code>Obsidian Sync</code>），设过期时间；权限务必勾<b>repo</b>（至少 Contents 读写）。</li><li>生成后<b>立即复制保存</b>——关掉页面就再也看不到，只能重生成。令牌以<code>ghp_</code>开头。</li></ol><div>用户名：你的 GitHub 用户名（不带 @） Password / Token 栏：粘贴上一步的 Personal Access Token（以 ghp_ 开头） ↳ 这里显示 &quot;Password&quot;，但填的是令牌，不是 GitHub 登录密码。</div></div></div>

## 03 · 安装插件：三条路（00206 / 00211 / 00327）

找不到「GitHub Publisher」是最常见的卡点。社区市场、手动、BRAT 三条路，按可用性依次试。

| 安装方式 | 操作 | 适用 |
|---|---|---|
| **社区市场（首选）** | 设置 → 第三方插件，**关闭安全模式**→ 浏览 → 搜`GitHub Publisher`→ 安装 → 启用。 | 网络正常、插件已上架。 |
| **BRAT（最可靠）** | 装`Beta Reviewer's Auto-update Tool`（作者 TfTHacker）→`Ctrl+P`→`BRAT: Add a beta plugin`→ 粘贴`https://github.com/ObsidianPublisher/obsidian-github-publisher`→`Ctrl+R`重载 → 启用。 | 市场搜不到、装测试版。 |
| **手动** | 从 releases 下 zip，解压到`你的库/.obsidian/plugins/obsidian-github-publisher/`，确保含`main.js`、`manifest.json`、`styles.css`，重启后启用。 | BRAT 也失败时。 |

> **Obsidian Git 插件同理**：市场搜全称`Obsidian Git`（不是「Git」）；BRAT 里填`https://github.com/Vinzent03/obsidian-git`。BRAT 需 Obsidian 0.13.8+，GitHub Publisher 需 0.15.0+。

## 04 · GitHub Publisher 配置与发布（00206 / 00209）

配置分两层：插件设置面板填全局规则，每篇笔记的 Frontmatter 决定这篇发不发。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>插件面板</span><h3>必须填的四项 + 发布行为</h3></div><div style="padding:14px 16px"><div>GitHub Username: 你的用户名 GitHub Repository: 你的仓库名（如 username.github.io） GitHub Branch: main（旧仓库可能是 master） GitHub Token: 粘贴 ghp_ 开头的令牌 ☑ Upload images ☑ Upload attachments Image folder: images Attachment folder: attachments ☑ Convert wikilinks to markdown links ☑ Automatically clean the title Frontmatter key to publish: published Value to publish: true</div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>Frontmatter</span><h3>单篇发布标记</h3></div><div style="padding:14px 16px"><p style="margin-bottom:8px">笔记开头 YAML 里写上<code>published: true</code>才会被发布；草稿就写<code>false</code>。</p><div>--- title: &quot;我的第一篇博客文章&quot; date: 2024-01-15 published: true tags: - 教程 - Obsidian ---</div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>发布动作</span><h3>怎么触发发布</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:180px">方式</th><th>命令 / 操作</th></tr></thead><tbody><tr><td><b>单篇发布</b></td><td><code>Ctrl+P</code>→<code>GitHub Publisher: Publish active file</code>；或编辑器右键<code>Publish this file</code>。</td></tr><tr><td><b>批量发布</b></td><td><code>GitHub Publisher: Publish all changed shared files</code>（发布所有<code>published: true</code>且有改动的笔记）。</td></tr><tr><td><b>查看/取消</b></td><td><code>Show shared settings</code>看状态；<code>Unpublish active file</code>或把<code>published</code>改<code>false</code>取消。</td></tr></tbody></table></div><p style="margin-bottom:0">发布后去仓库刷新看文件是否出现；若用 Jekyll 会自动构建，访问<code>https://你的用户名.github.io</code>看效果。</p></div></div>

## 05 · Obsidian Git 全库同步配置（00210 / 00327）

走方案一：装 Obsidian Git 后，把自动提交/拉/推的间隔打开，让它定期帮你备份整个库。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>自动同步</span><h3>核心开关</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>自动提交同步</dt><dd>开<code>Auto commit-and-sync interval(minutes)</code>，设间隔（如 5 / 20 / 30 分钟）；开<code>Auto pull interval</code>。</dd><dt>启动拉取</dt><dd>开<code>Pull updates on startup</code>，每次打开 Obsidian 先拿远程最新。</dd><dt>自动推送</dt><dd>开<code>Auto push</code>，每次提交后自动推到远程。</dd><dt>Git 路径</dt><dd>报「找不到 Git」时，终端<code>where git</code>（Windows）查路径，填进<code>Custom Git binary path</code>。</dd><dt>首次提交</dt><dd>先<code>Ctrl+P</code>跑一次<code>Obsidian Git: Create backup</code>做初始提交，再开自动同步。</dd></dl></div></div>

> **移动端注意**：手机端也要装并配同款插件，多为手动 Pull/Push；不支持 SSH 认证，大库性能差，建议移动端关自动提交改手动。遇 Git 安全目录错误，终端跑`git config --global --add safe.directory "你的笔记库完整路径"`。

## 06 · 排错与验证（00206 / 00211）

这套流程最大的坑是「装了插件却没有命令」。按顺序排。

<details open><summary>命令不出现：先重载，再彻底重装<span>高频</span></summary><div><ul><li><b>第一动作永远是重载</b>：<code>Ctrl+R</code>（Mac<code>Cmd+R</code>）。装插件后、启用后、改配置后都要重载一次。笔记内容自动保存，不会丢。</li><li><b>确认开关是蓝色开启</b>，且在「已安装的插件」列表里找（不要在「浏览」里找），按 G 开头排序。</li><li><b>仍没有命令</b>：<code>BRAT: Remove a beta plugin</code>移除 → 删掉<code>.obsidian/plugins/obsidian-github-publisher</code>残留文件夹 → 完全重启 → 重新 BRAT 添加仓库地址 → 启用 → 再<code>Ctrl+R</code>。</li><li><b>BRAT 命令也不出现</b>：说明 BRAT 本身没加载——确认它已启用、关安全模式、<code>Ctrl+R</code>；必要时备份并删除<code>.obsidian/community-plugins.json</code>与<code>plugins.json</code>后重启。</li></ul></div></details>

<details><summary>加载失败 / 启动即崩：查清单与冲突<span>manifest</span></summary><div><ul><li><b>文件齐全</b>：插件目录必须含<code>main.js</code>、<code>manifest.json</code>、<code>styles.css</code>。</li><li><b>manifest 正常</b>：<code>id</code>应为<code>obsidian-github-publisher</code>，<code>name</code>为<code>GitHub Publisher</code>，<code>minAppVersion</code>不高于你的版本。</li><li><b>版本</b>：设置 → 关于，确认 Obsidian 版本够新（Publisher 需 0.15.0+）。</li><li><b>冲突</b>：除 Publisher 与 BRAT 外禁用其他插件，重载后看命令是否出现；出现则逐个启用定位冲突。</li><li><b>看控制台</b>：<code>Ctrl+Shift+I</code>→ Console 看红色报错。</li></ul></div></details>

<details><summary>发布报错对照表<span>认证/路径</span></summary><div><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:200px">现象</th><th>解决</th></tr></thead><tbody><tr><td><b>Bad credentials</b></td><td>Token 失效或没勾 repo 权限，重生成。</td></tr><tr><td><b>Not Found / 仓库不存在</b></td><td>核对仓库名拼写与访问权限。</td></tr><tr><td><b>笔记没发布</b></td><td>Frontmatter 缺<code>published: true</code>。</td></tr><tr><td><b>图片不显示</b></td><td>勾了 Upload images、图片路径正确、文件别太大。</td></tr></tbody></table></div></div></details>

<details><summary>最终验证清单<span>打勾</span></summary><div><ul><li>插件在已安装列表、开关蓝色、重载后保持蓝色；设置左侧出现插件项。</li><li><code>Ctrl+P</code>输入<code>GitHub Publisher</code>能看到<code>Publish active file</code>/<code>Publish all changed shared files</code>/<code>Unpublish active file</code>/<code>Edit settings</code>/<code>Show shared settings</code>。</li><li>发一篇带<code>published: true</code>的测试笔记，仓库里能看到文件，Pages 能打开。</li></ul></div></details>

## 07 · 顺带：Obsidian 的功能、代价与价格（00864）

选这套工作流前，先知道 Obsidian 本身的长短板和收费——核心功能免费商用也免费。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">优点</h3><p style="font-size:13.5px;color:inherit">本地优先纯 Markdown、数据归你所有；双向链接 + 知识图谱串起知识；超千款社区插件生态；启动搜索都快；核心功能个人完全免费。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">缺点</h3><p style="font-size:13.5px;color:inherit">有学习曲线；无原生实时协作，不适合团队；移动端体验弱（Android 偶有乱插字符、键盘失灵）；高级功能高度依赖插件，存在插件失维风险。</p></div></div>

| 许可证 / 服务 | 价格 | 说明 |
|---|---|---|
| **免费使用** | $0 | 所有核心功能，含商用。 |
| **Catalyst** | $25 一次性 | 抢先体验测试版、社区徽章。 |
| **商业许可证** | $50 / 用户 / 年 | 功能与免费版完全相同，性质是支持性徽章；按席位不按设备。 |
| **Obsidian Sync** | $4 / 用户 / 月（按年） | 跨设备同步、端到端加密、版本历史。 |
| **Obsidian Publish** | $8 / 站点 / 月（按年） | 把笔记库发布为网站（官方付费方案；本页讲的是用 GitHub Publisher 免费替代）。 |
