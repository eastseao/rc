---
title: "Chirpy 导航栏·归档·社交分享·图标"
description: "归档改时间轴四法、share.yml 国内平台配置、侧边栏社交图标对照、navigation/locale 与 YAML 排错。"
pubDatetime: 2025-10-11
category: "建站与技术"
kind: "长文"
tags: ["导航栏", "归档", "社交分享", "图标", "share.yml"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00192-2025-10-09 修改Chirpy主题导航栏标题（2.3KB，远程主题下改名四法）00199-2025-10-10 Jekyll Chirpy主题导航栏归档改时间轴（5.2KB，时间轴页面与 Liquid 分组）00216-2025-10-11 Jekyll Chirpy国内社交平台分享配置（93KB 完整读，含 share.yml / navigation.yml / locale.yml / YAML 报错）00217-2025-10-11 Jekyll Chirpy主题社交图标配置指南（22KB，侧边栏 social 与图标对照）

## 01 · 把导航栏「归档」改成「时间轴」：四种做法（00192）

用户用的是**remote_theme 远程主题**，改不到主题源码。00192 给了四种从「最推荐」到「最后手段」的做法，按优先级试。

| 做法 | 改哪里 | 评价 |
|---|---|---|
| **① 改 _config.yml（推荐）** | 在 tabs 下直接写中文键值 | 最符合 Jekyll 主题设计，主题更新不冲突 |
| **② _data/locale.yml 覆盖** | 建 _data/locale.yml，按语言写 tabs 文案 | 支持多语言，改字不动主配置 |
| **③ 自定义 JS 替换** | _includes/custom-head.html 里用 JS 找文字替换 | 兜底方案，主题更新后可能失效 |
| **④ Fork 主题改源码** | Fork 后改主题文件文字，Gemfile 指向自己 fork | 最彻底但要自己维护主题更新 |

做法一：_config.yml（照录）

```
tabs:
  home: 首页
  archives: 时间轴  # 将"归档"改为"时间轴"
  categories: 分类
  tags: 标签
  about: 关于
```

做法二：_data/locale.yml（照录）

```
# 中文配置
zh-CN:
  tabs:
    archives: 时间轴
    home: 首页
    categories: 分类
    tags: 标签

# 英文配置（如果需要）
en:
  tabs:
    archives: Timeline
```

做法三：_includes/custom-head.html（照录）

```html
<script>
document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('a');
  links.forEach(link => {
    if (link.textContent.trim() === '归档') {
      link.textContent = '时间轴';
    }
  });
});
</script>
```

> **建议**
> - 优先用做法一或做法二，它们不侵入主题源码，主题升级时不会被覆盖或冲突。
> - 改完跑bundle exec jekyll serve本地看导航栏文字是否已变。

## 02 · 真做一个「时间轴」页面（00199）

光把导航改名还不够——点进去还是原来的归档页。00199 的做法是**新建一个 timeline 页面**，用 Chirpy 的 archive 布局，再用 Liquid 按年分组渲染文章。

timeline.md 的 Front Matter

```
---
layout: archive  # 或者你希望使用的其他布局，如 'page'
title: "时间轴"   # 这里设置你希望在导航栏和页面顶部显示的文字
permalink: /timeline/  # 这个链接最好记一下，后面配置导航栏可能会用到
---
```

按年分组的 Liquid 模板（照录）

```html
<div class="timeline">
  {% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
  {% for year in posts_by_year %}
    <div class="timeline-year">{{ year.name }}</div>
    <ul class="timeline-posts">
      {% for post in year.items %}
        <li>
          <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </li>
      {% endfor %}
    </ul>
  {% endfor %}
</div>
```

如果教程类文章想**自定义顺序而非按发布日期**，可在文章 Front Matter 加order字段，页面里用sort: "order"排：

文章里加 order / 页面里按 order 排序

```
---
layout: post
title: "你的文章标题"
order: 1   # 顺序号
---

{% assign sorted_posts = site.posts | sort: "order" %}
{% for post in sorted_posts %}
  <!-- 显示每篇文章 -->
{% endfor %}
```

> **接入导航栏**
> - _config.yml 的 tabs（或 _data/navigation.yml）里把原来的「归档」项换成时间轴：name: 时间轴 / path: /timeline/。
> - 具体配置项名（tabs 还是 header_pages）因 Chirpy 版本而异，以你所用版本为准。
> - 不需要原归档页时可从项目与导航配置里移除；时间轴样式按需再加 CSS。

## 03 · 文章底部分享按钮：_data/share.yml 换国内平台（00216）

Chirpy 文章底部的分享按钮由_data/share.yml控制，原版只有 Twitter / Facebook / Telegram。00216 给出去掉国外平台、只留国内平台的完整版本。

_data/share.yml 国内版（照录，已去国外平台）

```
# 文章底部的分享选项
# 图标来自 <https://fontawesome.com/>

platforms:
  # 微博
  - type: 微博
    icon: "fab fa-weibo"
    link: "https://service.weibo.com/share/share.php?title=TITLE&url=URL"

  # QQ空间
  - type: QQ空间
    icon: "fab fa-qq"
    link: "https://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=URL&title=TITLE"

  # 微信 (通过二维码分享)
  - type: 微信
    icon: "fab fa-weixin"
    link: "javascript:void(0)"  # 通常需要配合JavaScript生成二维码

  # 豆瓣
  - type: 豆瓣
    icon: "fab fa-douban"
    link: "https://www.douban.com/share/service?href=URL&name=TITLE"

  # 知乎
  - type: 知乎
    icon: "fab fa-zhihu"
    link: "https://www.zhihu.com/question/19554212/answer/"

  # 钉钉
  - type: 钉钉
    icon: "fab fa-dingding"
    link: "https://im.dingtalk.com/action/createtodo?title=TITLE&url=URL"

  # 百度贴吧
  - type: 贴吧
    icon: "fab fa-baidu"
    link: "http://tieba.baidu.com/f/commit/share/openShareApi?url=URL&title=TITLE"

  # 快手
  - type: 快手
    icon: "fas fa-video"  # 暂未找到官方图标，使用通用视频图标
    link: "https://www.kuaishou.com/"

  # B站
  - type: B站
    icon: "fab fa-bilibili"
    link: "https://t.bilibili.com/"

  # 小红书
  - type: 小红书
    icon: "fas fa-book"  # 暂未找到官方图标，使用书籍图标替代
    link: "https://www.xiaohongshu.com/"

  # 今日头条
  - type: 今日头条
    icon: "fas fa-newspaper"
    link: "https://www.toutiao.com/"

  # QQ
  - type: QQ
    icon: "fab fa-qq"
    link: "https://connect.qq.com/widget/shareqq/index.html?url=URL&title=TITLE"
```

> **使用纪律**
> - **TITLE 与 URL 是占位符**：Chirpy 会在渲染时把当前文章标题与地址替换进去，不要自己填死。
> - 建议按需精简到最常用的 5–8 个：微博、QQ空间、微信、豆瓣、QQ 足够。
> - 微信分享需额外 JavaScript 生成二维码；部分国内平台没有官方分享接口，链接可能要后续微调。
> - 图标用 Font Awesome，确保主题已引入图标库。

## 04 · 侧边栏社交图标：social 怎么配才显示（00217 / 00216）

侧边栏头像下方的社交图标由 _config.yml 的social.links控制。Chirpy 会按链接域名自动匹配 Font Awesome 品牌图标，不需要手动指定。00217 给了国内平台链接格式与图标对照。

_config.yml 里的 social.links（国内平台版，照录）

```
social:
  name: 王维
  email: # 留空或填写您的邮箱
  links:
    # 开发者平台
    - https://github.com/seamoonappear
    - https://gitee.com/你的码云用户名

    # 技术社区
    - https://juejin.cn/user/你的掘金ID
    - https://blog.csdn.net/你的CSDN用户名
    - https://www.zhihu.com/people/你的知乎ID

    # 内容平台
    - https://www.xiaohongshu.com/user/profile/你的小红书ID
    - https://www.douyin.com/user/你的抖音号

    # 其他平台
    - https://space.bilibili.com/你的B站ID
    - https://www.yuque.com/你的语雀用户名

    # RSS订阅
    - rss: /feed.xml
```

| 平台 | Font Awesome 图标类名 | 说明 |
|---|---|---|
| GitHub | fab fa-github | 开发者必备 |
| 码云 Gitee | fab fa-git-alt | 无官方品牌图标，用 git-alt 替代 |
| 知乎 | fab fa-zhihu | 有官方品牌图标 |
| B站 | fab fa-bilibili | 有官方品牌图标 |
| 微博 | fab fa-weibo | 有官方品牌图标 |
| 微信 | fab fa-weixin | 有官方品牌图标 |
| 掘金 | fas fa-gem | 无官方图标，常用替代 |
| CSDN | fas fa-code | 无官方图标，常用替代 |
| 抖音 | fab fa-tiktok | 沿用 TikTok 图标 |
| 小红书 | fab fa-weixin | 无官方图标，临时替代 |
| RSS | fas fa-rss | 主题内置，保留即可 |

> **图标不显示时的排查顺序**
> - 核对链接是完整 URL（https:// 开头），占位符已换成真实用户名。
> - 键名/域名与主题约定一致；掘金、CSDN、小红书这类无官方图标，主题会回退到默认链接图标。
> - 清缓存重建（bundle exec jekyll build）再硬刷新。
> - 实在不行看主题 _includes/social.html 的生成逻辑，或用 _data/contact.yml 自定义图标。

## 05 · 导航/多语言数据文件：navigation.yml 与 locale.yml（00216）

00216 后半段的真实故障是：自建了 _data/navigation.yml 与 _data/locale.yml，结果 GitHub Actions 报Psych::SyntaxError: could not find expected ':'。这一节把两个文件的正确写法与该报错的修法照录。

<details open><summary>_data/navigation.yml 修正版（照录）<span>00216</span></summary><div><pre>- title: 首页 url: / - title: 分类 url: /categories/ - title: 标签 url: /tags/ - title: 归档 url: /archives/ - title: 媒体 url: /media/ - title: 关于 url: /about/</pre><p style="margin-top:10px">每个导航项保持相同格式，冒号后留一个空格；不需要的项直接删行；调整数组顺序即调整导航显示顺序。</p></div></details>

<details><summary>_data/locale.yml（en + zh-CN，已加 media、去繁体）<span>00216</span></summary><div><pre># _data/locale.yml # English (default) en: post: share: &quot;Share&quot; updated: &quot;Updated&quot; read_time: unit: &quot;min&quot; prompt: &quot;read&quot; tabs: home: &quot;Home&quot; categories: &quot;Categories&quot; tags: &quot;Tags&quot; archives: &quot;Archives&quot; media: &quot;Media&quot; search: hint: &quot;Search&quot; cancel: &quot;Cancel&quot; no_results: &quot;No results found.&quot; panel: toc: &quot;Contents&quot; overview: &quot;Overview&quot; footer: copyright: &quot;Copyright&quot; powered: &quot;Powered by&quot; notification: update_found: &quot;A new version of content is available.&quot; update: &quot;Update&quot; # 中文简体 zh-CN: post: share: &quot;分享&quot; updated: &quot;更新于&quot; read_time: unit: &quot;分钟&quot; prompt: &quot;阅读&quot; tabs: home: &quot;首页&quot; categories: &quot;分类&quot; tags: &quot;标签&quot; archives: &quot;时间轴&quot; media: &quot;媒体&quot; search: hint: &quot;搜索&quot; cancel: &quot;取消&quot; no_results: &quot;没有找到结果。&quot; panel: toc: &quot;目录&quot; overview: &quot;概览&quot; footer: copyright: &quot;版权&quot; powered: &quot;由&quot; notification: update_found: &quot;内容有新版本可用。&quot; update: &quot;更新&quot;</pre></div></details>

真实报错与修法

```
Psych::SyntaxError: (_data/locale.yml): could not find expected ':'
  while scanning a simple key at line 9 column 5
```

| 报错点 | 原因 | 修法 |
|---|---|---|
| 缺冒号 | key value写成了无冒号 | 改成key: value |
| 冒号后无空格 | key:value | 冒号后必须留一个空格 |
| 缩进混用 Tab/空格 | YAML 依赖严格缩进，Tab 与空格混用 | 统一用空格，同层缩进量一致 |
| 多层结构错位 | 嵌套字典子级缩进没比父级多两格 | 子级比父级多缩进 2 空格 |

> **顺带：Ruby 3.3.9 兼容性**
> - 00216 还遇到 Bundler 在 Ruby 3.3.9 下构建失败（exit code 1）。原笔记建议工作流里把ruby-version降到3.2、runs-on固定ubuntu-22.04，Gemfile 里ruby "~> 3.2.0"。
> - 修完 YAML 后可用在线 yaml 校验器或ruby -ryaml -e "YAML.load_file('_data/locale.yml')"本地验证再提交。
