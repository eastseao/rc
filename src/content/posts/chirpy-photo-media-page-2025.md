---
title: "Chirpy 照片与 Media 页面"
description: "添加 media 页四步、多分类占位符、照片网格页、标签切换相册与空白页排查。"
pubDatetime: 2025-10-12
category: "建站与技术"
kind: "长文"
tags: ["media 页", "照片页", "相册", "lightbox"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00218-2025-10-11 Chirpy主题添加media页面步骤（13KB，四步流程与空白页排查）00223-2025-10-11 导航栏添加照片页面（5.9KB，照片网格页完整代码）00228-2025-10-12 Photo 页面需求整理（30KB，标签切换相册与优化版实现）

## 01 · 四步加一个 media 页面（00218）

00218 的核心结论：Chirpy 里加新页面 =**建一个 md 文件 + 在 navigation.yml 加一行**。路径都要可复制，不要靠猜。

| 步骤 | 关键操作 | 涉及路径 |
|---|---|---|
| **1. 建页面文件** | 根目录新建 Markdown 文件，带 Front Matter | /media.md |
| **2. 配导航栏** | _data/navigation.yml 按格式加 media 链接 | /_data/navigation.yml |
| **3. 写页面内容** | 用 Front Matter + Markdown 写正文 | /media.md |
| **4. 本地测试** | 起 Jekyll 服务预览 | bundle exec jekyll serve |

media.md 最小骨架（照录）

```
---
layout: page   # 必须有，告诉 Jekyll 用 page 布局
title: Media
---

# 欢迎来到我的媒体库

这里可以展示图片、视频或其他媒体内容。
```

navigation.yml 里加一行（照录）

```
# 在 _data/navigation.yml 中添加，注意缩进
- title: "Media"   # 导航栏中显示的名称
  url: /media      # 指向刚创建的 media.md 页面
```

> **资源放哪**
> - 图片视频放/assets/img/或/assets/media/，再用 Markdown/HTML 引用。
> - 页面 md 直接放项目根目录，访问路径才干净（/media）。
> - 改 navigation.yml 前先备份。

## 02 · 多分类占位符内容骨架（00218）

用户要 media 页放「爱好、读过的书、喜欢的电影、音乐、其他」，每类后续再填。00218 给了带占位符的整页骨架——每类一节，先用斜体占位符占住，以后往里填。

media.md 多分类骨架（照录节选）

```
---
layout: page
title: Media
description: "我的媒体库 - 记录我的爱好、阅读和娱乐生活"
---

# 我的媒体库

## 📚 我的爱好
*// 占位符：后续将添加更多爱好相关内容*

## 📖 读过的书
### 正在阅读
- *书籍标题将在这里显示*
### 已读完
- *已读书籍列表将在这里展示*
### 想读清单
- *计划阅读的书籍将列在这里*

## 🎬 喜欢的电影
### 经典收藏 / 近期观看 / 期待上映

## 🎵 音乐
### 最爱歌手/乐队 / 近期循环 / 心情歌单

## 🌟 其他
### 播客推荐 / 游戏收藏 / 其他发现
```

配套建议：给媒体资源建专属子目录，后续填图时路径清晰。

```
assets/
└── media/
    ├── books/      # 书籍封面
    ├── movies/     # 电影海报
    ├── music/      # 专辑封面
    └── hobbies/    # 爱好相关图
```

## 03 · 照片网格页：圆角 + 图注 + 响应式（00223）

00223 给的是一整页可复制代码：photos.md 用 CSS Grid 每行自适应排布，图片统一高度圆角，下方一行图注，手机端自动变窄。核心片段照录。

photos.md 网格与图注（照录节选）

```html
<div class="photos-container">
  <div class="photos-grid">
    <div class="photo-item">
      <img src="/assets/img/photos/photo1.jpg" alt="瞬间1" loading="lazy">
      <div class="photo-caption">晨光微熹 · 2023</div>
    </div>
    <div class="photo-item">
      <img src="/assets/img/photos/photo2.jpg" alt="瞬间2" loading="lazy">
      <div class="photo-caption">山色空蒙 · 2023</div>
    </div>
  </div>
</div>

<style>
.photos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}
.photo-item img {
  width: 100%;
  height: 250px;
  object-fit: cover;          /* 统一裁切，不变形 */
  display: block;
}
@media (max-width: 576px) {
  .photos-grid { grid-template-columns: 1fr; }   /* 手机端单列 */
}
</style>
```

> **接入与组织图片**
> - _config.yml 的 tabs 加：- name: 照片 / path: /photos/。
> - 图片目录：assets/img/photos/photo1.jpg …。
> - 图片命名用语义化文件名（如 2023-10-beijing-sunset.jpg），图片先压缩再上传。
> - 代码里已带loading="lazy"懒加载；想点开大图可后续加灯箱 JS。

## 04 · 可切换标签相册：高亮条 + 点击放大（00228）

00228 的需求更完整：标签栏（风景/人物/生活/猫/随手拍）点击切换图片区，激活标签底部一条高亮条nav-highlight，图片圆角网格，点任意图弹放大层、点任意处关闭。纯原生 JS，不依赖插件。

标签导航与高亮条（照录）

```html
<nav class="photo-nav">
  <div class="nav-container">
    <button class="nav-btn active" data-tab="scenery">风景</button>
    <button class="nav-btn" data-tab="people">人物</button>
    <button class="nav-btn" data-tab="life">生活</button>
    <button class="nav-btn" data-tab="cat">猫</button>
    <button class="nav-btn" data-tab="random">随手拍</button>
    <div class="nav-highlight"></div>
  </div>
</nav>

<style>
.nav-highlight {
  position: absolute;
  bottom: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
  border-radius: 1px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
```

切换标签与移动高亮条的 JS（照录核心）

```
nav.addEventListener('click', (e) => {
  const button = e.target.closest('.nav-btn');
  if (!button) return;
  const targetTab = button.dataset.tab;

  buttons.forEach(b => b.classList.remove('active'));
  button.classList.add('active');

  panes.forEach(p => p.classList.remove('active'));
  const targetPane = document.getElementById(targetTab);
  if (targetPane) targetPane.classList.add('active');

  // 移动高亮条到当前按钮下方
  const rect = button.getBoundingClientRect();
  const containerRect = button.parentElement.getBoundingClientRect();
  highlight.style.width  = rect.width + 'px';
  highlight.style.left   = (rect.left - containerRect.left) + 'px';
});
```

点击放大层（照录）

```html
<div class="photo-modal" id="photoModal">
  <div class="modal-content">
    <img class="modal-image" src="" alt="">
    <div class="modal-info"></div>
    <button class="modal-close" aria-label="关闭">×</button>
  </div>
</div>

<script>
// 点卡片 → 填大图与说明 → 打开模态框
document.querySelectorAll('.photo-card').forEach(card => {
  card.addEventListener('click', () => {
    const img  = card.querySelector('img');
    const info = card.querySelector('.photo-info');
    modalImage.src   = img.src;
    modalInfo.textContent = info.textContent;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  });
});
// 点关闭按钮 / 点遮罩 / 按 Esc 都关
closeBtn.addEventListener('click', closeModal);
modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && modal.classList.contains('active')) closeModal();
});
</script>
```

| 需求点 | 实现要点 |
|---|---|
| 标签切换 | button 带 data-tab，对应同 id 的 .tab-pane，切 active 类 |
| 激活高亮条 | 绝对定位的 .nav-highlight，JS 算按钮位置移动它 |
| 图片网格 | repeat(auto-fill, minmax(280px,1fr))，object-fit:cover 统一高度 |
| 图注固定 | .photo-info 常驻缩略图下方，不点放大也可见 |
| 点击放大 | fixed 全屏遮罩 .photo-modal，点遮罩/关闭/Esc 关闭 |
| 手机端 | 标签栏横向滚动隐藏滚动条；网格 minmax 降到 160px，小屏两列 |

## 05 · 页面点进去一片空白：排查路径（00218）

00218 真实遇到「导航点 media 进一片空白」。按「内容 → 编码 → 本地构建 → 线上日志」从近到远排。

| 排查点 | 怎么查 | 修法 |
|---|---|---|
| **页面文件为空** | 打开 media.md，看有没有 Front Matter 与正文 | 补layout: page与正文内容 |
| **文件带 BOM** | Windows 上 UTF-8 带 BOM 会让 Jekyll 认不出 Front Matter | VS Code 另存为**UTF-8 无 BOM** |
| **导航路径错** | navigation.yml 的 url 与文件名对不上 | 统一url: /media/，Jekyll 自动找 media.md |
| **本地缓存旧** | Jekyll 缓存没清 | bundle exec jekyll clean再 serve |
| **线上构建失败** | 本地好、线上坏，看仓库 Actions 日志 | 按日志修语法；Gemfile 用github-pages对齐依赖 |

> **一句话优先级**
> - 先看 Actions 红不红——红了就别碰文件，先读日志。
> - 绿了还空白，九成是 Front Matter 缺layout或文件带 BOM。
> - 都对了还不显示，硬刷新清 CDN 缓存再看。
