<div align="center">

# GERVAS · AI × Tools × Design × Life

> 我喜欢研究新技术，也喜欢做一些东西。写下来，做出来，然后继续探索。

[![站点](https://img.shields.io/badge/站点-eastseao.github.io%2Frc-1c1b1a?style=flat-square&logo=github)](https://eastseao.github.io/rc/)
[![作品](https://img.shields.io/badge/作品-810%20篇-9a3412?style=flat-square)](https://eastseao.github.io/rc/#works)
[![部署](https://img.shields.io/badge/部署-GitHub%20Pages-c96442?style=flat-square)](https://eastseao.github.io/rc/)
[![技术](https://img.shields.io/badge/技术-纯静态·无构建-6d6a63?style=flat-square)](#站点结构)

**在线访问：https://eastseao.github.io/rc/**（原 `gervas.wang` 域名已过期，不再使用）

</div>

---

## 站点结构

| 路径 | 说明 |
|---|---|
| `index.html` | 首页：GERVAS 个人主页（Latest / Projects / Explore / Now / About）+ 作品区块 |
| `_pages_registry.js` | **作品登记表（数据源）**：810 篇作品的元数据，首页由此生成 |
| `pages/` | 作品正文（历史子页，810 篇，全部开源、数据可复现） |
| `tools/` · `assets/` | 工具子页与资源文件 |
| `theme.css` · `STYLE-GUIDE.md` | 子页样式与页面规范 |

首页视觉风格参考 [astro-paper](https://github.com/satnaing/astro-paper) 模板；个人主页区块按 GERVAS 版式定制，作品区块展示最新 10 篇并支持搜索、分类筛选浏览全部 810 篇。

## 更新作品

新增 / 修改子页后，更新首页只需两步：

1. 编辑 `_pages_registry.js`：新增或修改条目（字段：`title` / `desc` / `date` / `category` / `url` / `kind` / `tags`）
2. 运行 `node _build_home.js` 重新生成 `index.html`

然后 `git add index.html _pages_registry.js` → commit → push，GitHub Pages 自动重建。

**维护工具**（均为仓库本地脚本，不入库）：

| 工具 | 作用 |
|---|---|
| `_build_home.js` | 读 `_pages_registry.js` → 注入模板 → 生成 `index.html`（写入前自动备份旧首页到 `_backup/`） |
| `_home_template.html` | 首页模板（含 GERVAS 各区块与作品列表渲染逻辑） |
| `_extract_pages.js` | 从旧版式源（含 `const PAGES = [...]` 的旧首页）批量刷新登记表：`node _extract_pages.js [旧首页路径]`，默认读 `_backup/index.homepage-20261009-old.html` |

## 说明

- 全部页面开源、数据可复现，欢迎自取
- 历史作品正文位于 `pages/` 等目录，旧链接（`pages/*.html`）保持可访问
- 首页 Latest 三篇（Agent Skill / Markdown 知识库 / OpenClaw）为占位草稿，正文整理中
