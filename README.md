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
| `index.html` | 首页**薄壳**：页头 + 十篇目录 + 入口 + 页脚。列表由 `_build_index.js` 从 `manifest.js` 生成，样式自包含（不依赖 `theme.css`）。 |
| `archive.html` | **全部作品检索页**：搜索 + 九类筛选 + 按年分组列表，同样只读 `manifest.js`，支持 `?cat=分类` 直入。 |
| `manifest.js` | **作品数据产物**（生成物，约 321 KB）：`window.WORKS`，首页与档案页通过 `<script src="manifest.js">` 读取 |
| `_pages_registry.js` | **作品登记表（数据源）**：815 篇元数据，仅供生成脚本使用，不被页面直接加载 |
| `pages/` | 作品正文（历史子页，815 篇，全部开源、数据可复现） |
| `tools/` | 工具子页 |
| `assets/works/` | 首页用的子页截图（1280×800 无头 Chrome 实拍，压成 960 宽 JPEG） |
| `assets/fonts/` | 首页自托管的 Work Sans（latin，约 86 KB），避开 Google Fonts 在国内的不可达 |
| `theme.css` · `STYLE-GUIDE.md` | 子页样式与页面规范 |

### 首页（2026-10-30 第三版：一张目录）

前三版都在同一种思路里打转（巨字碑 → 拆两页 → 删顶部），反馈始终是「乱」。根子在**一页里有五套版式**：碑、图文左右、巨名带标注带图、双列分类、反色页脚，每滚一屏人眼都要重新学一遍规则。

这一版只留**一种版式**：一列目录。整页三段。

1. **页头**：一行。左「815 篇 · 21 个工具 · 九类」（`h1`），右「档案 / GitHub」。
2. **目录**：最近十篇，按发布日期倒排。每行 = 208px 截图 + 标题 + 日期，全部对齐到两条竖线（图列、文字列），日期跟在标题下方而不是甩到右边缘——甩到右边会把一行撕成三段。
3. **入口 + 页脚**：「全部 815 篇 →」在列表末尾、与标题列对齐；页脚一行，`GERVAS` 与「杭州 · 自 2023 年 10 月」两端。

手机端：图 96px（4:3）、标题 17px 最多三行、日期 14px，行距 15px。

排版约束：**两个字级** —— 条目名 `clamp(19px,1.7vw,24px)`，其余一律 16px（日期 14px）。一底（石灰纸 `#e6e1d6`）一墨（`#1b1917`）一色（暖赭 `#a16207`）；无细线、无阴影、无渐变、无反色区。

**这一版删掉的东西**：GERVAS 巨字与首屏自述、最新一篇区块、精选六篇区块、九类分类目录、反色页脚与页脚巨字。它们每一个单独看都成立，同时出现就是五个首页。

首页列表由根目录 `_build_index.js` 生成（读 `manifest.js`，取最新十篇，写回 `index.html`）；首页仍是手写薄壳，样式自包含，不依赖 `theme.css`。

`archive.html` 是检索页（按工具页的标准做，不做门面）：搜索框（标题 + 摘要 + 标签）、九类筛选、按年分组单栏列表，初始 50 条，「再显示 50 篇」追加；`?cat=` 参数可直接进分类。

## 更新作品

新增 / 修改子页后更新首页：

1. 编辑 `_pages_registry.js`：新增或修改条目（字段：`title` / `desc` / `date` / `category` / `url` / `kind` / `tags`）
2. 运行 `node _build_home.js` 重新生成 `manifest.js`
3. 若要把新篇放进首页目录，把它的截图放进 `assets/works/<slug>.jpg`，再跑 `node _build_index.js` 重出 `index.html`

然后 `git add manifest.js _pages_registry.js index.html assets/works` → commit → push，GitHub Pages 自动重建。
没有截图的条目会被 `_build_index.js` 跳过（它只列有图的篇）。

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