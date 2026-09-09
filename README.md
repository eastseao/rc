<div align="center">

# 日常 · Agent 作品集

日常由 **Agent（WorkBuddy）** 生成的研究报告、行业分析与工具网页合集，按主题归档、随产出持续增补。

[![站点](https://img.shields.io/website?url=https%3A%2F%2Fgervas.wang&up_message=在线&down_message=离线&style=flat-square)](https://gervas.wang/)
[![部署](https://img.shields.io/badge/部署-GitHub%20Pages-1c1b1a?style=flat-square&logo=github)](https://gervas.wang/)
[![域名](https://img.shields.io/badge/域名-gervas.wang-a2431f?style=flat-square)](https://gervas.wang/)
[![技术](https://img.shields.io/badge/技术-纯静态·无构建-6d6a63?style=flat-square)](#目录结构)
[![登记](https://img.shields.io/badge/首页登记-6%20页%20%2B%201%20外链-c96442?style=flat-square)](#站点一览)

**[🌐 在线访问：gervas.wang](https://gervas.wang/)** · 备用地址 [eastseao.github.io/rc](https://eastseao.github.io/rc/)

</div>

---

## 站点一览

首页卡片由下方「登记表」驱动，当前收录：

| # | 页面 | 说明 | 访问 |
|---|------|------|------|
| 1 | SKILL 介绍 · Agent Skills 概念手册 | 33 节概念手册：定义、渐进式披露、与 Prompt/Tool/MCP/Workflow 的区别、架构与生命周期 | [skill.html](https://gervas.wang/skill.html) |
| 2 | 生产级 Agent Skill 架构规范 | 工程层规范 35 节：标准模型 14 模块、Contract/Schema、Decision Rules、Registry/Router/Runtime、Capability OS | [skill-spec.html](https://gervas.wang/skill-spec.html) |
| 3 | 如何制作适合自己的 Skill | 七步法实操指南 13 节：选任务、挖方法、立规则、契约、案例训练、自评闭环、三个母 Skill | [skill-diy.html](https://gervas.wang/skill-diy.html) |
| 4 | AI Agent 提效培训 · WorkBuddy 专题 | 面向食品生产企业的培训课件：概念科普、技术预备、主流智能体盘点、七大业务场景实战 | [ai-agent-training.html](https://gervas.wang/ai-agent-training.html) |
| 5 | 超强厄尔尼诺 · 2027 全维度影响分析 | 气候研判报告：事件定性、全球与中国影响、农业能源生态卫生金融基建、风险矩阵与应对 | [el-nino-2027-impact.html](https://gervas.wang/el-nino-2027-impact.html) |
| 6 | Prompt 库 | 个人 Prompt 收藏管理器：搜索、分类、收藏、一键复制，数据存 GitHub 可追溯 | [prompt.html](https://gervas.wang/prompt.html) |
| — | 地平线 · 个人博客（外链，置于卡片末位） | 个人博客独立站（[eastseao/horizon](https://github.com/eastseao/horizon)，Jekyll 构建）：影评、随笔与生活记录 | [eastseao.github.io/horizon](https://eastseao.github.io/horizon/) |

> 仓库中另有未在首页列出的存档页面：`el-nino-a-share-2026.html`（厄尔尼诺 · A 股板块分析）、`zhihu-juzi.html`（知乎句子十年金句集）、`yijing.html`（每日卜卦 · 六十四卦），可直接输入地址访问。

顶栏右侧「**地平线 · 个人博客站 ↗**」为博客常驻入口。

---

## 技术要点

- **三栏 docs 视觉体系** —— SKILL 系列三篇采用统一规范：暖纸底色 + 陶土红单 accent + mono 元数据 + 1px hairline，左侧章节导航、右侧本页目录（sticky 悬浮）、章节带 + 阅读地图，滚动进度与 scrollspy 联动。
- **PAGES 登记表驱动首页** —— `index.html` 内的 `PAGES` 数组是唯一需要维护的数据源：分类筛选、关键词搜索、统计数字、卡片渲染全部自动完成。
- **Prompt 库 GitHub 同步** —— `prompt.html` 的数据源为 [`prompts.json`](prompts.json)；在页内配置 Fine-grained Token 后，添加 / 编辑 / 删除 / 收藏会以独立提交直接写回本仓库。
- **自定义域名** —— 仓库根目录 [`CNAME`](CNAME) 绑定 `gervas.wang`，推送 `main` 分支后 GitHub Pages 自动构建发布。

---

## 目录结构

```text
rc/
├── index.html                  # 首页：PAGES 登记表驱动的卡片目录（搜索 / 分类 / 统计）
├── CNAME                       # 自定义域名 gervas.wang
│
├── skill.html                  # SKILL 系列 ① 概念手册（33 节）
├── skill-spec.html             # SKILL 系列 ② 生产级架构规范（35 节）
├── skill-diy.html              # SKILL 系列 ③ 制作适合自己的 Skill（七步法 13 节）
│
├── el-nino-2027-impact.html    # 超强厄尔尼诺 · 2027 全维度影响分析
├── el-nino-a-share-2026.html   # 厄尔尼诺 · A 股受益板块分析（存档）
├── ai-agent-training.html      # AI Agent 提效培训课件
├── zhihu-juzi.html             # 知乎句子十年 · 金句集（存档）
├── yijing.html                 # 每日卜卦 · 六十四卦（存档）
│
├── prompt.html                 # Prompt 库（搜索 / 分类 / 收藏 / GitHub 写入）
├── prompts.json                # Prompt 库数据文件
└── README.md
```

---

## 如何新增一个子网页

1. 生成 HTML 文件放入仓库根目录（建议语义化命名，如 `topic-2026-09-08.html`）。
2. 在 `index.html` 的 `PAGES` 数组中新增一条记录：

```js
{
  title: "页面标题",
  desc: "一句话描述（显示在卡片上）",
  url: "your-page.html",
  date: "2026-09-08",              // 日期决定首页排序
  category: "金融分析",             // 分类，用于顶部筛选
  tags: ["标签一", "标签二"]         // 标签
}
```

3. 推送后首页自动完成分类统计、搜索与卡片渲染，无需改动其他代码。

> 卡片为纯文字排版：分类标签在卡体首行，无缩略图。`gradient` / `glyph` 字段为历史遗留数据，已不再渲染，可省略。

---

## Prompt 库的写入

浏览与搜索无需任何配置；添加 / 编辑 / 删除 / 收藏需要 GitHub 写入权限：

1. 打开 [github.com/settings/personal-access-tokens/new](https://github.com/settings/personal-access-tokens/new)；
2. Repository access → Only select repositories → **rc**；
3. Permissions → Contents → **Read and write**；
4. 在 Prompt 库页面右上角 ⚙ 粘贴令牌保存——令牌只存在当前浏览器，不会上传到任何服务器。

---

## 本地预览与部署

- **本地预览**：双击 `index.html` 即可（Prompt 库的 GitHub 同步功能需联网）；或起一个静态服务器：

  ```bash
  python -m http.server 8000
  # 访问 http://localhost:8000
  ```

- **部署**：推送 `main` 分支后，GitHub Pages 自动构建并发布到 [gervas.wang](https://gervas.wang/)（构建约 1–2 分钟生效）。`CNAME` 文件承载域名绑定，勿删。

---

## 维护

- 站点由 **Agent（WorkBuddy）** 生成与维护，人工仅做内容审校与登记表调整。
- 所有子页面返回首页的链接统一指向 `index.html`。
