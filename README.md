# 日常 · Agent 作品集

日常由 **Agent（WorkBuddy）** 生成的研究报告、行业分析与数据可视化网页合集，按主题归档，随产出不断增补。

## 目录结构

```
rc/
├── index.html                  # 首页（聚合导航，数据驱动）
├── dictn/                      # 子网页（子目录形式：迪腾数字包装方案册，左右滑动版，自带 assets）
├── el-nino-a-share-2026.html   # 子网页示例：厄尔尼诺 A股分析
└── README.md
```

## 如何新增一个子网页

1. 生成你的 HTML 文件，放入仓库根目录（建议用语义化命名，如 `xxx-2026-09-08.html`）。
2. 打开 `index.html`，在 `<script>` 里的 `PAGES` 数组中新增一条记录：

```js
{
  title: "页面标题",
  desc: "一句话描述（会显示在卡片上）",
  url: "your-page.html",
  date: "2026-09-08",
  category: "金融分析",            // 分类，用于顶部筛选
  tags: ["厄尔尼诺", "A股"],        // 标签
  gradient: "linear-gradient(135deg,#f6d365,#fda085)",  // 卡片缩略图渐变色
  glyph: "🌊"                       // 缩略图 emoji 图标
}
```

首页会自动完成分类统计、搜索与卡片渲染，无需改动其他代码。

## 部署

推送后，在 GitHub 仓库 **Settings → Pages** 中启用 GitHub Pages（Source 选 `main` 分支根目录），即可通过 `https://eastseao.github.io/rc/` 访问。

## 维护

- 首页为纯静态 HTML + 原生 JS，无构建依赖，直接编辑即可。
- 所有页面返回首页的链接统一指向 `index.html`。
