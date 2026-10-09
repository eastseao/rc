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
| `index.html` | 首页**薄壳，约 12 KB，手写维护**：hero + About + 作品区块。不含任何数据。 |
| `manifest.js` | **作品数据产物**（生成物，约 321 KB）：`window.WORKS`，首页通过 `<script src="manifest.js">` 读取 |
| `_pages_registry.js` | **作品登记表（数据源）**：810 篇元数据，仅供生成脚本使用，不被页面直接加载 |
| `pages/` | 作品正文（历史子页，810 篇，全部开源、数据可复现） |
| `tools/` · `assets/` | 工具子页与资源文件 |
| `theme.css` · `STYLE-GUIDE.md` | 子页样式与页面规范 |

首页视觉风格参考 [astro-paper](https://github.com/satnaing/astro-paper) 模板。首页只有三个区块：**hero**（站名 + 一句话）、**About**（身份 + 仓库链接）、**作品**（最新 10 张卡片 + 搜索 + 9 个分类筛选 + 全部 810 篇归档列表，可分页「显示更多」）。

## 更新作品

新增 / 修改子页后更新首页：

1. 编辑 `_pages_registry.js`：新增或修改条目（字段：`title` / `desc` / `date` / `category` / `url` / `kind` / `tags`）
2. 运行 `node _build_home.js` 重新生成 `manifest.js`

然后 `git add manifest.js _pages_registry.js` → commit → push，GitHub Pages 自动重建。

> `index.html` 本身不需要重新生成 —— 它不依赖 `_pages_registry.js`，也不内联数据。

## 免维护设计（V2 方案）

```
_pages_registry.js  ──(node _build_home.js)──>  manifest.js  ──(<script src>)──>  index.html
      手改（唯一数据源）                            自动生成          手写薄壳，不含数据
```

三个要点：

1. **产物是 `manifest.js` 而非 `.json`** —— 页面用 `<script src>` 加载而非 `fetch()`，因为 `file://` 协议下 `fetch` 会被 CORS 拦掉，本地直接双击打开也能正常渲染。
2. **`index.html` 是手写薄壳** —— 改版式直接编辑即可，不需要跑构建脚本，也不会有 34 万字符的 diff。
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
- 首页作品区块支持搜索（匹配 标题 + 摘要 + 标签）与分类筛选，初始显示前 60 篇
- `manifest.js` 体积说明：desc 字段占全字段约 75%，因搜索依赖摘要而无法裁剪，故产物约 321 KB；换来的收益是改作品时不再重新生成 34 万字符的 HTML