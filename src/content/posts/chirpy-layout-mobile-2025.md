---
title: "Chirpy 布局·手机端·关于我·文章布局"
description: "布局重组、手机端封面左标题右 CSS、CSS 不生效调试、关于我卡片与文章页元信息+Cusdis。"
pubDatetime: 2025-10-25
category: "建站与技术"
kind: "长文"
tags: ["布局", "手机端", "关于我", "文章布局"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00225-2025-10-12 GitHub Pages Jekyll Chirpy页面布局调整（4.9KB，文章合集页+首页个人介绍）00234-2025-10-13 Jekyll Chirpy手机端博客布局调整（24KB，封面图左标题右+CSS 调试）00320-2025-10-25 关于我页面优化与设计（22KB，头像+三卡片+职业理念+滚动动画）00321-2025-10-25 Jekyll博客文章布局优化方案（20KB，文章页模板与 Cusdis 展开）

## 01 · 布局重组：归档/分类/标签合一页，首页放个人介绍（00225）

用户想把导航里的「归档、分类、标签」收进一个文章页，首页单独放个人介绍。00225 的三步走法：**建文章合集页 → 改首页 → 调导航**。

第一步：articles.md 集中调用三块

```
---
layout: page
title: "文章"
---

<h2>文章归档</h2>
{% include archives.html %}

<h2>文章分类</h2>
{% include categories.html %}

<h2>文章标签</h2>
{% include tags.html %}
```

第二步：index.html 换成个人介绍

```
---
layout: home
title: 首页
---

<!-- 这里替换成你的个人介绍，HTML 或 Markdown 均可 -->
```

第三步：_config.yml 的 tabs 指向新页

```
tabs:
  - name: 首页
    path: /
  - name: 文章
    path: /articles.html   # 原归档/分类/标签链接替换为这一条
  - name: 关于
    path: /about.html
```

> **限制与备选**
> - archives.html / categories.html / tags.html这三个 include 要 Chirpy 主题自带，或自己写——参考主题原本那三个页面怎么写。
> - GitHub Pages 插件支持有限，想用 jekyll-archives 之类增强插件得本地构建后推 _site。
> - 实在集成不动，就在文章合集页里放指向原三个独立页的链接，做内容引导也行。

## 02 · 手机端首页：封面图靠左、标题在右、不显示摘要（00234）

00234 的目标效果：手机端每篇文章是「左小封面 + 右标题」一行，不显示摘要。做法是改首页文章循环的 HTML 结构，再加一段只在 ≤768px 生效的 Flex CSS。

首页文章循环（加 mobile-post-layout 类）

```html
{% for post in paginator.posts %}
  <article class="post-entry mobile-post-layout">
    <div class="post-cover">
      <a href="{{ post.url | relative_url }}">
        <img src="{{ post.image }}" alt="{{ post.title }}">
      </a>
    </div>
    <div class="post-content">
      <h3 class="post-title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h3>
      <!-- 摘要 {{ post.excerpt }} 这行删掉或注释掉 -->
    </div>
  </article>
{% endfor %}
```

只在手机端生效的 Flex CSS

```css
@media (max-width: 768px) {
  .post-entry.mobile-post-layout {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 1.5rem;
  }
  .post-entry.mobile-post-layout .post-cover {
    flex-shrink: 0;
    width: 80px;
  }
  .post-entry.mobile-post-layout .post-cover img {
    width: 100%;
    height: auto;
    border-radius: 4px;
  }
  .post-entry.mobile-post-layout .post-content { flex: 1; }
  .post-entry.mobile-post-layout .post-title {
    margin: 0;
    font-size: 1rem;
    line-height: 1.4;
  }
}
```

> **想桌面端也这样？**
> - 把外层@media (max-width: 768px){}去掉即可全端生效。
> - 封面图变量名可能是 image / cover / thumbnail，按你 Front Matter 实际字段调；桌面端想大一点可加@media (min-width:992px){ .post-cover{width:100px} }。

## 03 · CSS 改了不生效：调试与 !important 强化（00234）

00234 真实遇到「上述代码无效」。根因通常是选择器优先级被主题默认样式压住，或类名跟模板对不上。从弱到强四步。

| 步骤 | 做什么 | 目的 |
|---|---|---|
| **1. 看真实 DOM** | 浏览器右键文章项 → 检查，看实际 class 名 | 确认模板里有没有 mobile-post-layout |
| **2. 加测试样式** | .mobile-post-layout{border:3px solid red!important} | 红框出现=CSS 加载了但选择器不对；不出现=CSS 没加载 |
| **3. 提高优先级** | 用#main-wrapper #main .post-entry这种长选择器 + !important | 压过主题默认样式 |
| **4. JS 兜底** | DOMContentLoaded 后直接给 entry.style.display='flex' | CSS 实在压不住时的最后一招 |

强化版选择器（照录核心）

```css
#main-wrapper #main .post-list .post-entry,
#main-wrapper #main .post-item {
  display: flex !important;
  align-items: center !important;
  gap: 15px !important;
  margin-bottom: 1.5rem !important;
  width: 100% !important;
  box-sizing: border-box !important;
}
#main-wrapper #main .post-cover {
  flex-shrink: 0 !important;
  width: 80px !important;
  min-width: 80px !important;
}
#main-wrapper #main .post-content { flex: 1 !important; min-width: 0 !important; }
```

> **自定义 CSS 放哪**
> - Chirpy 通常放/_sass/custom/custom.scss或/assets/css/style.scss。
> - 还不行就把<style>直接内联进模板文件，先确认样式能出来再外移。

## 04 · 关于我页面：头像 + 三卡片 + 职业理念（00320）

00320 把 about.md 从简单自我介绍升级成「头像装饰环 + 职业简介横幅 + 三卡片（职业经历/技能标签/爱好网格）+ 职业理念三列 + 联系按钮」，并用 IntersectionObserver 做卡片入场动画。

| 区块 | 结构 | 视觉要点 |
|---|---|---|
| **头像简介** | 圆形头像 + 渐变装饰环 + 姓名/标签/所在地 + 社交圆钮 | 装饰环 pulse 呼吸动画；hover 头像上浮 |
| **职业简介横幅** | 浅灰底横条，左侧 4px 渐变边 | 关键数字 highlight 变色 |
| **职业经历卡** | 圆形图标 + 公司 + 职位 + 职责列表 | 悬停顶部渐变条 scaleX 展开 |
| **技能卡** | 按「设计/营销/行业」三组，每组一排标签 chip | 标签 hover 反白上浮 |
| **爱好卡** | 2 列图标网格，每项图标+文字 | hover 浅紫底 |
| **职业理念** | 三列（创新/价值/可持续），居中图标+短述 | 标题下居中渐变短线 |

卡片入场动画（IntersectionObserver，照录核心）

```css
const observer = new IntersectionObserver(function(entries) {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('animate-in');
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.card, .philosophy-item').forEach(el => observer.observe(el));
// .card { opacity:0; transform:translateY(20px); transition:.6s }
// .card.animate-in { opacity:1; transform:translateY(0) }
```

> **响应式断点**
> - ≤768px：头部改纵向居中，卡片网格单列，爱好网格单列。
> - ≤480px：头像缩到 120px，卡片内边距收紧。

## 05 · 文章页布局：元信息·封面·热门标签·相关文章·Cusdis 展开（00321）

00321 给的是一个完整文章页模板（layout: default）：封面插图、作者/阅读时间/日期/分类元信息、正文、相关文章、热门标签云、Cusdis 评论完全展开。优化重点是 CSS 变量化与评论区不再出滚动条。

| 区块 | 做法 |
|---|---|
| **封面插图** | {% if page.cover %}时渲染，rounded + shadow，大图加 loading=lazy |
| **文章元信息** | 一行 flex：作者 / 阅读时间（按字数 ÷180 算分钟）/ 发布日期 / last_modified_at / 分类 |
| **热门标签云** | 按文章数排序取前 10，标签后带 (n)，点进 /tags/ |
| **相关文章** | site.related_posts取前 5，箭头列表 |
| **Cusdis 评论** | 容器 height:auto、overflow-y:visible，iframe 最小 400px，不再出内嵌滚动条 |

阅读时间与隐藏邮箱输入框（照录）

```html
{% assign words = content | number_of_words %}
{% if words < 360 %}
  <span>阅读时间: 1分钟</span>
{% else %}
  <span>阅读时间: {{ words | divided_by:180 }}分钟</span>
{% endif %}

/* 隐藏 Cusdis 的邮箱输入框 */
#cusdis_thread .cusdis-input-email-container { display: none !important; }
/* iframe 完全展开 */
#cusdis_thread iframe { height: auto !important; min-height: 400px; }
```

> **评论区高度自动跟随**
> - 用 MutationObserver 监听 #cusdis_thread 的子节点变化，Cusdis 异步渲染后再调一次高度，避免固定高度留白或截断。
> - 窗口 resize 时也重调一次。
> - 评论区 min-height 桌面端 400px、手机端 300px。
