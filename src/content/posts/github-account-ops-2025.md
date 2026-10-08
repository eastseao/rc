---
title: "GitHub 账户操作·登录·回退·改名·解析"
description: "Desktop 切换账户、git reset/revert 回退、手机登录被 APP 劫持、仓库数量限制、改用户名连锁反应与腾讯云 DNSPod 解析。"
pubDatetime: 2026-04-20
category: "建站与技术"
kind: "手册"
tags: ["Desktop 切换", "git reset revert", "仓库限制", "改用户名", "DNSPod 解析"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00212-2025-10-10 GitHub Desktop 登录与切换账户教程00215-2025-10-11 GitHub 代码回退方法总结00372-2025-11-01 手机登录 GitHub 网页版方法00381-2025-11-01 GitHub 账户仓库数量及限制说明00412-2025-11-10 GitHub 网页解析至腾讯云教程00979-2026-04-20 修改 GitHub 用户名指南

## 01 · GitHub Desktop 登录与切换账户（00212）

登录和切换的核心路径都是同一个：**File → Options → Accounts**（Mac 上是 GitHub Desktop → Preferences）。

| 动作 | 步骤 |
|---|---|
| **登录** | 主界面 → File → Options → Accounts → GitHub.com 区域点**Sign in**→ 输用户名密码（可能跳浏览器授权）。 |
| **切换** | 同一 Accounts 选项卡 → 点当前账户旁**Sign out**→ 确认 → 再 Sign in 新账户；也可**Add Account**后 Set as active。 |

> **切换账户两个坑（源笔记原话）**
> - 切了 Desktop 账户，**旧本地仓库仍关联旧账户**——因为提交者信息由本地`user.name / user.email`决定，要去仓库单独改。
> - 注销前先把未提交的工作保存/提交，避免丢数据。

## 02 · 代码回退：reset 与 revert 怎么选（00215）

回退有两种思路：**彻底回退**移除提交、**安全撤销**新增一个抵消提交。先`git log --oneline`找到目标提交的哈希。

| 方法 | 命令 | 适用 | 对历史 |
|---|---|---|---|
| **彻底回退** | `git reset --hard <hash>` | 未推远程，或确定要覆盖远程历史 | 移除/丢弃提交，需`push -f` |
| **安全撤销** | `git revert <hash>` | 已推远程、团队协作 | 新增一个撤销提交，保留完整历史，普通 push 即可 |

> **网页版路径**：仓库 →**Commits**选项卡 → 找到那条提交 → 右侧**…**→**Revert this commit**→ 建个 PR 合并（底层就是 revert）。怕丢改动可先`git stash`暂存。

## 03 · 手机登录网页总跳 GitHub APP，怎么办（00372）

手机装了 GitHub APP，浏览器登 github.com 时被系统自动拉去 APP——要绕开 APP 关联，让浏览器登录。

| 方案 | 做法 |
|---|---|
| **一、浏览器登录选项（最推荐）** | APP 登录页找**Sign in with browser**（在浏览器中登录）。 |
| **二、清除默认打开设置** | 安卓：设置 → 应用 → GitHub →「打开默认链接」→ 清除默认；iOS：设置 → GitHub → 关「允许连接到 App」。 |
| **三、桌面版网站** | 浏览器菜单开「桌面版网页 / 电脑版网站」，服务器识别为电脑请求，不触发跳转。 |
| **四、临时卸载** | 仍不行就临时卸载 APP，登完网页再装回。 |

## 04 · 一个账户能建多少仓库？免费账户限制（00381）

仓库数量**没有硬性上限**（公共、私有都不限制）。真正卡你的是下面这些免费账户限制。

| 限制项 | 免费账户 |
|---|---|
| **仓库数量** | 公共 / 私有均无数量限制。 |
| **私有仓库协作者** | 最多**3 人**。 |
| **单文件大小** | 通常 ≤**100MB**，超过用 Git LFS。 |
| **仓库总容量** | 建议每个仓库 ≤**1GB**，过大收性能警告。 |
| **API 请求** | 已认证请求每小时最多**5000**次。 |

> **仓库能干嘛**（00381 全景）：代码托管与版本控制、Issues 与 Project 看板、Wiki、GitHub Actions 自动化、GitHub Pages 静态站、Releases 软件分发、Fork 参与开源。个人从版本控制 + Issues + Pages 起步即可。

## 05 · 改 GitHub 用户名的连锁反应与待办（00979）

改名入口是**Settings → Account → Change username**，但它不是换个名字那么简单，有一串连锁反应。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00979 · 改名前提醒 + 改名后待办</span><h3>别只改个名</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0;margin:0 0 14px"><table><thead><tr><th style="width:160px">改名前</th><th>后果</th></tr></thead><tbody><tr><td><b>旧名冻结</b></td><td>旧用户名<b>90 天</b>内谁都不能再用（含你自己）。</td></tr><tr><td><b>部分链接不重定向</b></td><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">@旧名</code>提及、旧资料页链接、旧 gist 链接不自动跳转。</td></tr><tr><td><b>重定向会被覆盖</b></td><td>仓库链接会自动重定向到新名；但若旧名被他人注册并建同名仓库，重定向被覆盖失效。</td></tr></tbody></table></div><div style="margin:14px 0"><span># 改名后最关键：更新本地仓库远程地址</span>git remote -v git remote set-url origin https://github.com/新用户名/仓库名.git<span># 再查 git config user.name 是否要改；</span><span># 并更新 CI/CD、环境变量、配置文件里引用旧用户名的地方</span></div><p style="margin:14px 0 0"><b>三条待办</b>：① 检查并更新个人网站/社媒上的 GitHub 链接、通知协作者；② 本地仓库<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">git remote set-url</code>改地址；③ 检查 Actions、环境变量等引用旧用户名的配置。</p></div></div>

## 06 · GitHub 网页解析到腾讯云（DNSPod）（00412）

把腾讯云买的域名指向 GitHub Pages，分两步：**① 仓库里配 GitHub Pages**，**② 腾讯云 DNSPod 里加解析记录**。访问域名时由 DNSPod 解析到 GitHub 的服务器。

| 阶段 | 步骤 |
|---|---|
| **① 查 IP** | 命令行`nslookup <你的用户名>.github.io`，记下 4 个 GitHub Pages 服务器 IP（务必用自己查到的，可能更新）。 |
| **② 建 CNAME 文件** | 仓库根目录（Pages 用的分支）建**无后缀**的`CNAME`文件，内容写你的域名（如`blog.example.com`），提交。 |
| **③ Settings 确认** | 仓库**Settings → Pages → Custom domain**，应看到刚写的域名，点**Save**确认。 |
| **④ DNSPod 加记录** | 腾讯云控制台搜**DNSPod → 域名解析列表 → 选域名 → 添加记录**，按下表加记录。 |

<table><thead><tr><th>主机记录</th><th>类型</th><th>记录值</th><th>说明</th></tr></thead><tbody><tr><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">www</code></td><td><b>CNAME</b></td><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">mygithubname.github.io.</code></td><td>官方推荐；<b>末尾必须有句点「.」</b>；IP 变了不用改</td></tr><tr><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">@</code></td><td><b>A</b></td><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">185.199.108.153</code></td><td rowspan="4" style="vertical-align:middle">根域名<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">example.com</code>用 4 条 A 记录各填一个 IP，做负载均衡；CNAME 不能用于根域名</td></tr><tr><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">@</code></td><td><b>A</b></td><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">185.199.109.153</code></td></tr><tr><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">@</code></td><td><b>A</b></td><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">185.199.110.153</code></td></tr><tr><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">@</code></td><td><b>A</b></td><td><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">185.199.111.153</code></td></tr></tbody></table>

> **常见问题（00412 原话）**
> - **访问不了**：先`ping`看域名解析到哪个 IP，再查 Pages 设置和 CNAME 文件。
> - **样式丢失**：网页里 CSS/JS/图片链接要用相对路径或正确域名。
