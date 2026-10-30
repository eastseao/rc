<div align="center">

# GERVAS · AI × Tools × Design × Life

> 我喜欢研究新技术，也喜欢做一些东西。写下来，做出来，然后继续探索。

[![站点](https://img.shields.io/badge/站点-eastseao.github.io%2Frc-1c1b1a?style=flat-square&logo=github)](https://eastseao.github.io/rc/)
[![作品](https://img.shields.io/badge/作品-810%20篇-9a3412?style=flat-square)](https://eastseao.github.io/rc/#works)
[![部署](https://img.shields.io/badge/部署-GitHub%20Pages-c96442?style=flat-square)](https://eastseao.github.io/rc/)
[![技术](https://img.shields.io/badge/技术-纯静态·无构建-6d6a63?style=flat-square)](#站点结构)

**在线访问：https://eastseao.github.io/rc/**（原自定义域名已过期，不再使用）

</div>

---

## 站点结构

| 路径 | 说明 |
|---|---|
| `index.html` | 首页**薄壳，手写维护**：碑（巨字首屏）+ 最新一篇 + 精选六篇 + 档案入口 + 页脚。不含数据，样式自包含（不依赖 `theme.css`）。 |
| `archive.html` | **全部作品检索页**：搜索 + 九类筛选 + 按年分组列表，同样只读 `manifest.js`，支持 `?cat=分类` 直入。 |
| `manifest.js` | **作品数据产物**（生成物，约 321 KB）：`window.WORKS`，首页与档案页通过 `<script src="manifest.js">` 读取 |
| `_pages_registry.js` | **作品登记表（数据源）**：815 篇元数据，仅供生成脚本使用，不被页面直接加载 |
| `pages/` | 作品正文（历史子页，815 篇，全部开源、数据可复现） |
| `tools/` | 工具子页 |
| `assets/works/` | 首页用的子页截图（1280×800 无头 Chrome 实拍，压成 960 宽 JPEG） |
| `assets/fonts/` | 首页自托管的 Work Sans（latin，约 86 KB），避开 Google Fonts 在国内的不可达 |
| `theme.css` · `STYLE-GUIDE.md` | 子页样式与页面规范 |

### 首页（2026-10-30 重构：碑与档案）

首页只回答「这是谁、有多少、从哪进」，全量检索交给 `archive.html`——上一版把 815 篇列表塞进首页，双栏 14px 密排，是「乱」的结构性根源。

1. **首屏（碑）**：GERVAS 巨字 25.2vw 一行顶满视口，只留三处信息——左上自述与「打开档案」、右上导航、底部「杭州 · 自 2023 年 10 月」与「815 篇 · 21 个工具 · 九类」。手机端顺序重排：碑先立，导航、自述、按钮依次随后，底部 4:5 截图出血。
2. **最新一篇**：左方图、右文字，标题固定两行，双动作「读这一篇 / 换一篇看」（后者从全部作品里随机跳）。
3. **精选六篇**：按最新发布取前六篇，左列六行大字作品名（右侧分类与日期各一行），右列一张示例截图；**指向某一行，右图就换成那一篇**（窄屏没有悬停，改为滚过即换）。
4. **档案入口**：深一档纸色；左标题 + 说明 + 按钮 + 九类分类（带篇数，直链 `archive.html?cat=分类`），右一张竖版截图。
5. **页脚**：反色收尾，四列信息 + 杭州时间，GERVAS 字标顶满收底，与首屏成括号。

`archive.html` 是检索页（按工具页的标准做，不做门面）：搜索框（标题 + 摘要 + 标签）、九类筛选、按年分组单栏列表，初始 50 条，「再显示 50 篇」追加；`?cat=` 参数可直接进分类。

排版约束：**五个字号，五个用途，一个不多** —— 363（首屏与页脚巨字）/ 101（精选作品名）/ 46（区块标题）/ 20（正文）/ 16（标注）。一底（石灰纸 `#e6e1d6`）一墨（`#1b1917`）一色（暖赭 `#a16207`，与 815 个子页同一支）；Work Sans 只管西文与数字，中文走系统栈；无细线、无阴影、无渐变、无等宽字体、无图标卡。

## 更新作品

新增 / 修改子页后更新首页：

1. 编辑 `_pages_registry.js`：新增或修改条目（字段：`title` / `desc` / `date` / `category` / `url` / `kind` / `tags`）
2. 运行 `node _build_home.js` 重新生成 `manifest.js`

然后 `git add manifest.js _pages_registry.js` → commit → push，GitHub Pages 自动重建。

> `index.html` 与 `archive.html` 都不需要重新生成 —— 两者都不依赖 `_pages_registry.js`，也不内联数据。

## 免维护设计（V2 方案）

```
_pages_registry.js  ──(node _build_home.js)──>  manifest.js  ──(<script src>)──>  index.html / archive.html
      手改（唯一数据源）                            自动生成          手写薄壳，不含数据
```

三个要点：

1. **产物是 `manifest.js` 而非 `.json`** —— 页面用 `<script src>` 加载而非 `fetch()`，因为 `file://` 协议下 `fetch` 会被 CORS 拦掉，本地直接双击打开也能正常渲染。
2. **`index.html` 与 `archive.html` 都是手写薄壳** —— 改版式直接编辑即可，不需要跑构建脚本，也不会有 34 万字符的 diff。
3. **压缩字段映射** —— 产物用短键 `t`(title) / `c`(category) / `d`(date) / `u`(url) / `k`(kind) / `g`(tags) / `desc`，与模板里的渲染逻辑对应。

构建脚本自带校验：作品条数与 `url` 计数必须一致、registry 不能为空、产物中不得出现已失效域名 `gervas.wang`、站外 `url` 会打WARN。

## 维护工具（均为仓库本地脚本，不入库）

| 工具 | 作用 |
|---|---|
| `_build_home.js` | 读 `_pages_registry.js` → 生成 `manifest.js`（含安全校验） |
| `_extract_pages.js` | 从旧版式源（含 `const PAGES = [...]` 的旧首页）批量刷新登记表：`node _extract_pages.js [旧首页路径]`，默认读 `_backup/index.homepage-20261009-old.html` |
| `_home_template.html` | **已废弃** —— 首页改为手写薄壳，不再由模板生成 |

## 说明

- 全部页面开源、数据可复现，欢迎自取
- 历史作品正文位于 `pages/` 等目录，旧链接（`pages/*.html`）保持可访问
- 检索集中在 `archive.html`：搜索匹配 标题 + 摘要 + 标签，九类筛选，按年分组，初始 50 条、每次再加 50 条
- `manifest.js` 体积说明：desc 字段占全字段约 75%，因搜索依赖摘要而无法裁剪，故产物约 321 KB；换来的收益是改作品时不再重新生成 34 万字符的 HTML