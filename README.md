<div align="center">

# 日常 · Agent 作品集

日常由 **Agent（WorkBuddy）** 生成的研究报告、行业分析与工具网页合集，按主题归档、随产出持续增补。

[![站点](https://img.shields.io/website?url=https%3A%2F%2Fgervas.wang&up_message=在线&down_message=离线&style=flat-square)](https://gervas.wang/)
[![部署](https://img.shields.io/badge/部署-GitHub%20Pages-1c1b1a?style=flat-square&logo=github)](https://gervas.wang/)
[![域名](https://img.shields.io/badge/域名-gervas.wang-a2431f?style=flat-square)](https://gervas.wang/)
[![技术](https://img.shields.io/badge/技术-纯静态·无构建-6d6a63?style=flat-square)](#目录结构)
[![登记](https://img.shields.io/badge/首页登记-7%20页%20%2B%201%20外链-c96442?style=flat-square)](#站点一览)

**[🌐 在线访问：gervas.wang](https://gervas.wang/)** · 备用地址 [eastseao.github.io/rc](https://eastseao.github.io/rc/)

</div>

---

## 站点一览

首页卡片由 `index.html` 内的 `PAGES` 数组驱动，按日期倒序排列。当前 7 个本地页面 + 1 个外链：

| # | 页面 | 说明 | 访问 |
|---|------|------|------|
| 1 | 山姆饮品类 · 植物基原浆市场调研 | 山姆在售植物基原浆饮品 12 款 SKU 深度拆解、价格带分布、代工厂谱系、五大趋势与选品机会 | [pages/sams-plant-based-puree-2026.html](https://gervas.wang/pages/sams-plant-based-puree-2026.html) |
| 2 | SKILL 介绍 · Agent Skills 概念手册 | 33 节概念手册：定义、渐进式披露、与 Prompt/Tool/MCP/Workflow 的区别、架构与生命周期 | [pages/skill.html](https://gervas.wang/pages/skill.html) |
| 3 | 生产级 Agent Skill 架构规范 | 工程层规范 35 节：标准模型 14 模块、Contract/Schema、Decision Rules、Registry/Router/Runtime、Capability OS | [pages/skill-spec.html](https://gervas.wang/pages/skill-spec.html) |
| 4 | 如何制作适合自己的 Skill | 七步法实操指南 13 节：选任务、挖方法、立规则、契约、案例训练、自评闭环、三个母 Skill | [pages/skill-diy.html](https://gervas.wang/pages/skill-diy.html) |
| 5 | AI Agent 提效培训 · WorkBuddy 专题 | 面向食品生产企业的培训课件：概念科普、技术预备、主流智能体盘点、七大业务场景实战 | [pages/ai-agent-training.html](https://gervas.wang/pages/ai-agent-training.html) |
| 6 | 超强厄尔尼诺 · 2027 全维度影响分析 | 气候研判报告：事件定性、全球与中国影响、农业能源生态卫生金融基建、风险矩阵与应对 | [pages/el-nino-2027-impact.html](https://gervas.wang/pages/el-nino-2027-impact.html) |
| 7 | Prompt 库 | 个人 Prompt 收藏管理器：搜索、分类、收藏、一键复制，数据存 GitHub 可追溯 | [pages/prompt.html](https://gervas.wang/pages/prompt.html) |
| — | 地平线 · 个人博客（外链，置于卡片末位） | 个人博客独立站（[eastseao/horizon](https://github.com/eastseao/horizon)，Jekyll 构建）：影评、随笔与生活记录 | [eastseao.github.io/horizon](https://eastseao.github.io/horizon/) |

> 仓库中另有未在首页列出的存档页面：`pages/el-nino-a-share-2026.html`（厄尔尼诺 · A 股板块分析）、`pages/zhihu-juzi.html`（知乎句子十年金句集）、`pages/yijing.html`（每日卜卦 · 六十四卦），可直接输入地址访问。

顶栏右侧「**地平线 · 个人博客站 ↗**」为博客常驻入口。

---

## 目录结构

```text
rc/
├── index.html                  # 首页：PAGES 登记表驱动的卡片目录（搜索 / 分类 / 统计 / 标签筛选）
├── CNAME                       # 自定义域名 gervas.wang（GitHub Pages 要求保留在根）
├── README.md                   # 本文件
├── assets/                     # 首页头像等公共静态资源
│
└── pages/                      # 全部子页面与数据文件
    ├── sams-plant-based-puree-2026.html
    ├── skill.html              # SKILL 系列 ① 概念手册（33 节）
    ├── skill-spec.html         # SKILL 系列 ② 生产级架构规范（35 节）
    ├── skill-diy.html          # SKILL 系列 ③ 制作适合自己的 Skill（七步法 13 节）
    ├── el-nino-2027-impact.html
    ├── el-nino-a-share-2026.html   # 存档
    ├── ai-agent-training.html
    ├── zhihu-juzi.html             # 存档
    ├── yijing.html                 # 存档
    ├── prompt.html                 # Prompt 库（搜索 / 分类 / 收藏 / GitHub 写入）
    └── prompts.json                # Prompt 库数据文件
```

**根目录只保留三件东西**：`index.html`（首页入口）、`CNAME`（Pages 域名绑定，平台机制要求必须留在根）、`README.md`（仓库说明）。`dictn/` 是独立的离线子项目，不参与 Pages 构建。

---

## 设计系统：docs-page 美学

全部 docs 类子页（SKILL 系列 / 山姆调研 / 厄尔尼诺等）共享同一套视觉规范：

| Token | 值 | 用途 |
|-------|------|------|
| `--bg` | `#faf9f7` | 暖纸背景 |
| `--ink` | `#1c1b1a` | 正文墨色 |
| `--accent` | `#c96442` | 陶土红单 accent（链接 / 强调 / hover） |
| `--mono` | JetBrains Mono / Cascadia Mono | 元数据 / 编号 / eyebrow / 按钮 |
| `--sans` | Segoe UI / PingFang SC / Microsoft YaHei | 正文 |
| 布局 | 三栏 250px / 772px / 218px | sticky 侧栏 + 主区 + sticky 右 TOC |
| 边框 | `1px solid var(--border)` hairline | 无圆角无阴影，靠分隔留白 |

首页（`index.html`）和 Prompt 库采用同套 token，首页额外用 hairline 横条做统计、轻量 grid 卡片陈列。

### 移动端适配

- 断点 `@media (max-width:1120px)`：右 TOC 隐藏，主区扩宽。
- 断点 `@media (max-width:900px)`：侧栏/抽屉切换为 `<details>` 折叠，主区 padding 收紧。
- 断点 `@media (max-width:640px)`（**首页搜索框紧凑化**）：`.search{padding:6px 11px}`、svg 14×14、input font-size 13px、`.cat{padding:4px 10px;font-size:11.5px}`；统计数字 / 标题字号同步下调。
- 断点 `@media (max-width:420px)`：统计 4 格改为竖排。

---

## 技术要点

- **PAGES 登记表驱动首页** —— `index.html` 内的 `PAGES` 数组是唯一需要维护的数据源：分类筛选、关键词搜索、统计数字、标签筛选、卡片渲染全部自动完成。增删页面只需在数组里加一条记录。
- **Prompt 库 GitHub 同步** —— `pages/prompt.html` 数据源为 [`pages/prompts.json`](pages/prompts.json)；在页内配置 Fine-grained Token 后，添加 / 编辑 / 删除 / 收藏会以独立提交直接写回本仓库。`FILE` 常量在 `pages/prompt.html` 第 370 行，路径与实际文件位置一致才能读 / 写成功。
- **三栏 docs 视觉** —— SKILL 系列等长文采用 sticky 左导航 + 主区 + sticky 右 TOC + 顶部进度条 + scrollspy，章节带 + 阅读地图。
- **自定义域名** —— 仓库根目录 [`CNAME`](CNAME) 绑定 `gervas.wang`，推送 `main` 分支后 GitHub Pages 自动构建发布。
- **零依赖** —— 所有页面纯 HTML + CSS + 少量原生 JS，无构建工具、无打包、无第三方 CDN。

---

## 如何新增一个子网页

1. 生成 HTML 文件，**放入 `pages/` 子目录**（建议语义化命名，如 `topic-2026-09-10.html`）。
2. 子页内所有指向首页的链接写成 `../index.html`（在 `pages/` 子目录下相对于根）。
3. 在 `index.html` 的 `PAGES` 数组中新增一条记录（`url` 字段必须带 `pages/` 前缀）：

```js
{
  title: "页面标题",
  desc: "一句话描述（显示在卡片上）",
  url: "pages/your-page.html",       // 注意 pages/ 前缀
  date: "2026-09-10",                // 日期决定首页排序
  category: "金融分析",               // 分类，用于顶部筛选
  tags: ["标签一", "标签二"]           // 标签
}
```

4. 推送后首页自动完成分类统计、搜索与卡片渲染，无需改动其他代码。

> `gradient` / `glyph` 字段为历史遗留数据，已不再渲染，可省略。

---

## Prompt 库的写入

浏览与搜索无需任何配置；添加 / 编辑 / 删除 / 收藏需要 GitHub 写入权限：

1. 打开 [github.com/settings/personal-access-tokens/new](https://github.com/settings/personal-access-tokens/new)；
2. Repository access → Only select repositories → **rc**；
3. Permissions → Contents → **Read and write**；
4. 在 Prompt 库页面右上角 ⚙ 粘贴令牌保存——令牌只存在当前浏览器，不会上传到任何服务器。

> 数据文件路径已迁移到 `pages/prompts.json`（2026-09-10 起），打开页面会自动读取该路径。如遇"找不到 prompts.json"报错，刷新一次即可。

---

## 本地预览与部署

- **本地预览**：双击 `index.html` 即可（Prompt 库的 GitHub 同步功能需联网）；或起一个静态服务器：

  ```bash
  python -m http.server 8000
  # 访问 http://localhost:8000
  ```

- **部署**：推送 `main` 分支后，GitHub Pages 自动构建并发布到 [gervas.wang](https://gervas.wang/)（构建约 1–2 分钟生效）。`CNAME` 文件承载域名绑定，**勿删**。

---

## 维护

- 站点由 **Agent（WorkBuddy）** 生成与维护，人工仅做内容审校与登记表调整。
- 所有子页面"返回首页"链接统一为 `../index.html`。
- `dictn/` 是独立的离线子项目，不参与 Pages 构建。