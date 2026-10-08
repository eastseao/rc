---
title: "Chirpy PWA 配置与 Feed 订阅"
description: "PWA 三特征、pwa/manifest 配置、只改两行开关与首页空白排查、jekyll-feed 启用 /feed.xml、阅读器与 RSSHub。"
pubDatetime: 2025-10-25
category: "建站与技术"
kind: "长文"
tags: ["PWA", "manifest", "Service Worker", "RSS", "jekyll-feed"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00237-2025-10-13 渐进式网页应用详解（21KB，PWA 概念与 Chirpy 内置配置）00238-2025-10-13 Jekyll PWA配置与优化建议（6.7KB，pwa 段解析与 manifest 建议）00313-2025-10-24 Jekyll Chirpy主题PWA配置检查（12KB，开关两行 + 首页空白排查）00241-2025-10-14 feed（6.8KB，feed 概念与 jekyll-feed 启用）00325-2025-10-25 如何使用Feed链接订阅信息（11KB，阅读器与国内源）

## 01 · PWA 是什么：三大核心特征（00237）

PWA（渐进式网页应用）是「披着网站外衣的应用程序」——既有网站无需安装、可链接分享、能被搜索的优点，又有原生应用的离线、主屏图标、全屏体验。「渐进式」指对老浏览器可用、对新浏览器逐步解锁更多能力。

| 特征 | 核心技术 | 用户能感知到什么 |
|---|---|---|
| **可靠** | Service Worker（后台脚本，拦截网络请求、缓存资源） | 弱网/离线也能秒开已访问过的页面 |
| **快速** | 应用 Shell 架构（先缓存头部/导航等静态骨架） | 切页面无白屏等待，交互跟手 |
| **吸引人** | Web App Manifest（JSON 描述怎么显示） | 可「安装」到主屏、有图标、可全屏沉浸式 |

对个人博客来说，**核心基础功能收益最大**：可安装、离线访问、快速加载。推送通知 iOS 不支持、硬件访问 API 支持有限，属第三阶段，不必先做。

## 02 · Chirpy 内置 PWA 怎么配（00237 / 00238）

Chirpy 主题本身内置 PWA 支持，不用自己写 sw.js，只要在 _config.yml 开开关、补一份 manifest.json 和图标。

_config.yml 的 pwa 段（照录）

```
pwa:
  enabled: true
  cache:
    enabled: true
    deny_paths:
      # - "/admin/"   # 管理页/接口不缓存
      # - "/api/"

# 或更细的 serviceWorker 配置（按主题版本）
serviceWorker:
  enabled: true
  cache: "networkFirst, cacheFirst"   # 混合策略：页面走网络优先、静态资源走缓存优先
  exclusion:
    - "/404.html"
  preCache:
    - "/"
    - "/assets/css/style.css"
    - "/assets/js/dist/*.js"
  version: "2024.1.0"   # 改这个版本号强制更新缓存
```

assets/manifest.json（照录要点）

```json
{
  "name": "海上升明月",
  "short_name": "Seamoon博客",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#你的主题色",
  "icons": [
    { "src": "/assets/img/favicons/icon-192x192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/assets/img/favicons/icon-512x512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

> **图标与验证**
> - 图标放assets/img/favicons/，至少 192×192 与 512×512；用 Real Favicon Generator / PWA Builder 一键生成。
> - Service Worker 必须 HTTPS——GitHub Pages 自带 HTTPS，满足。
> - 改完用 Chrome DevTools 的 Application 标签看 Manifest / Service Worker，跑 Lighthouse 审计。

## 03 · 只改两行开 PWA，与开启后首页空白的排查（00313）

00313 的真实经历：配置里 PWA 是关的（enabled: false），用户要求只动 PWA 段、别的不改。开了之后首页却一片空白——这正是 PWA 缓存最典型的坑。

开启 PWA 只改这两行

```
pwa:
  enabled: true        # false → true
  cache:
    enabled: true      # false → true
    deny_paths:
      - "/example"
```

| 排查点 | 怎么查 / 修 |
|---|---|
| **资源 404** | F12 → Console 看红错、Network 看哪些 CSS/JS 红了；核对 url/baseurl |
| **PWA 旧缓存** | 先把pwa.enabled改回 false 重建，清浏览器缓存刷新；恢复即说明是缓存问题，再配 deny_paths 或 bump version |
| **构建不完整** | Chirpy 需npm run build，并把 assets/js/dist、_sass/dist 强制 add 提交 |
| **首页 Front Matter** | 根目录 index.md 要有layout: home |

> **为什么内容更新后用户看不到新版**
> - 这正是 PWA 缓存的代价：静态资源被 Service Worker 缓存后，用户拿到的是旧版本。
> - 修法：发版时把serviceWorker.version递增，或在 deny_paths 里排除高频更新路径。

## 04 · 让博客支持 Feed 订阅：jekyll-feed（00241）

网页上那个橙色方块 Feed 图标，代表「订阅本网站更新的通道」。Chirpy 内置了生成能力，只要确认插件开着，就能在 /feed.xml 拿到订阅源。

三步确认 Feed 已启用

```
# 1. Gemfile 里有插件
group :jekyll_plugins do
  gem 'jekyll-feed'
end

# 2. _config.yml 的 plugins 里列上
plugins:
  - jekyll-feed

# 3. 主题 head 模板里有（Chirpy 通常自带，无需手改）
{% feed_meta %}
```

可选的 Feed 自定义

```
feed:
  posts_limit: 10        # Feed 里放最近多少篇
  path: feed.xml          # 想换路径时改这里（默认 /feed.xml）
```

> **验证**
> - 本地bundle exec jekyll serve后访问http://127.0.0.1:4000/feed.xml，看到 XML 文档即成功。
> - 线上订阅地址是https://用户名.github.io/feed.xml。

## 05 · 拿到 Feed 链接后怎么用（00325）

拿到 feed 链接的核心动作：**找一个 RSS 阅读器，把链接粘进去，让更新自动推给你**。像订报纸——报社出新刊自动送报箱，不用每天跑报社。

| 阅读器类型 | 代表 | 特点 |
|---|---|---|
| **在线网页版（推荐新手）** | Feedly、Inoreader、BazQux | 跨平台同步，开箱即用 |
| **本地应用** | Fluent Reader（Win/Mac/Linux）、NetNewsWire（iOS/macOS）、Reeder（Mac） | 数据在本地，免费开源多 |
| **自托管** | Tiny Tiny RSS、yarr | 数据自己掌控，适合折腾 |
| **浏览器扩展** | Feedbro 等 | 轻量，免注册 |

订阅四步

```
1. 注册/登录阅读器（如 Feedly）
2. 点「Add Content / +」
3. 粘贴 feed 链接 → 确认
4. 阅读器自动抓取历史与最新文章
```

> **找源与进阶**
> - 没标 RSS 图标的站，试着在域名后加/feed或/rss。
> - 网站本身不提供 RSS（如部分社媒），用开源的**RSSHub**生成订阅源。
> - 想自动归档：用 IFTTT / Zapier / 集简云 把「有新文章」触发为「保存到笔记」。
> - 有道云笔记官方没有内置 RSS 阅读器，靠上述自动化或「网页剪报」手动保存。
