# GERVAS 子页风格设定

> **版本** V1.0 · **生效** 2026-09-21 · **基准页** `pages/sams-onboarding-sop-2026.html` · **适用范围** 全站子页
>
> 可视化版本：`pages/style-guide.html`（同一套内容的可点击版，本身就是规范的第一份示范）

这是 gervas.wang 全部子页的**唯一风格基准**。它把「供应商产品入驻山姆会员店全流程作业手册」页实际在跑的那套骨架、组件与 token 逐条固化下来 —— 新做子页照抄即可，不必重新发明一套视觉，也不要各自微调。

写新页的顺序：**按第 03 节抄骨架 → 按第 04 节挑组件 → 在第 06 节的清单上过一遍。**

---

## 目录

| 节 | 内容 |
|---|---|
| [00](#00-使用方式) | 使用方式 · 三条红线 · 文件落位 |
| [01](#01-设计原则--三层版心) | 设计原则 · 三层版心 |
| [02](#02-设计-token) | 设计 token（配色 / 形状 / 字体 / 别名层 / 体例变量） |
| [03](#03-页面骨架) | 页面骨架 · 四段式 · 逐层取值 |
| [04](#04-组件清单) | 组件清单（布局 / 内容 / 表格 / 交互 / 重型组件） |
| [05](#05-间距刻度与响应式断点) | 间距刻度 · 响应式断点 · 已知冗余 |
| [06](#06-新建子页清单) | 新建子页清单 · 登记上线 · 交付自检 |

---

## 00 使用方式

### 三条红线

| # | 红线 | 内容 |
|---|---|---|
| 1 | **单一色源** | 配色只在仓库根目录的 `theme.css` 改。子页一律 `<link>` 它，不再自带 `:root` 配色、不写死色值。改一次，十几个页面同时生效。 |
| 2 | **单一版心源** | 宽度只有三个变量：外壳 `--maxw`、正文列 `--maxw-read`、长段落 `--maxw-text`。子页禁止再写 `max-width:1180px` 这类硬编码，否则又会退化成「一页一个宽度」。 |
| 3 | **注释里的星号斜杠** | `theme.css` 的注释里禁止 `*` 紧邻 `/` —— 会被浏览器当成注释结束符，吃掉后面整个 `:root`，全站瞬间褪色。写变量通配请用「两点」或逐条列举。 |

### 文件落位

| 文件 | 职责 |
|---|---|
| `theme.css` | 仓库根目录。**全站唯一的**配色 / 字体 / 圆角 / 阴影 / 版心来源。子页用 `<link rel="stylesheet" href="../theme.css">` 引入。 |
| `pages/*.html` | 全部子页平铺在这个目录下，不建子目录。 |
| `STYLE-GUIDE.md` | 本文件，规范正文（权威来源）。 |
| `pages/style-guide.html` | 规范的可视化版。它遵守自己写的每一条规则，因此可以直接另存为模板。 |
| `index.html` | 首页。新增子页只需在脚本里的 `PAGES` 数组加一条记录，列表、统计、分类与「最近更新」会自动跟上。 |

---

## 01 设计原则 · 三层版心

整套风格只有两条全局原则：**颜色收在一个文件里**，**宽度收在三个变量里**。其中版心三层最容易被改坏 —— 三层职责一旦混用，页面就会出现「顶栏撑得很宽、正文却挤在中间」这种畸形。

### 1.1 三层示意

```
┌─ --maxw · none ───────── 外壳：顶栏 / 页脚 / 通栏分带 ────────────┐
│                                                                  │
│   ┌─ --maxw-read · 1440px ── 正文列 ─────────────────────┐        │
│   │  表格 / 卡片 / 网格 / 代码块 / 配图                    │        │
│   │                                                      │        │
│   │   ┌─ --maxw-text · 940px ─ 长段落 ─┐                 │        │
│   │   │  约 55 字/行 @17px              │                 │        │
│   │   └─────────────────────────────────┘                 │        │
│   └──────────────────────────────────────────────────────┘        │
└──────────────────────────────────────────────────────────────────┘
```

示意比例按 1920 视口推算：正文列占外壳内容宽 82%，长段落占正文列 65%。

### 1.2 三层职责表

| token | 值 | 职责 | 谁在吃它 |
|---|---|---|---|
| `--maxw` | `none` | **外壳**：通栏到屏幕两边 | 顶栏 `.s-bar-in`、页脚 `.s-foot-in`、免责 `.s-disc`。不设上限，靠各页自己的 `padding`（桌面 32px / 窄屏 18px）留呼吸位。 |
| `--maxw-read` | `1440px` | **正文列** | 页头 `.s-head`、主体 `.s-body`、白底正文卡 `.s-main`。表格、卡片、网格、代码块、配图都按它的内容宽（1370px）排。 |
| `--maxw-text` | `940px` | **长段落行宽** | 所有连续中文正文。由全局兜底规则 `p{max-width:var(--maxw-text)}` 自动生效，作者不用管。 |

### 1.3 全局段落兜底的四条规矩

`theme.css` 里那条 `p{ max-width:var(--maxw-text) }` 只约束**纯文字段落** —— 表格、卡片、代码、网格照吃满 `--maxw-read`。

**要这样做**

- 连续正文写成裸 `<p>`，它会自动吃到 940px 行宽。
- 要更窄时，在**类选择器**上覆盖：`p.lede{max-width:var(--maxw-text)}`。
- 一个块既要通栏、里面又含长段落时，**拆成两层**：外壳 `<div class="s-disc">` 套内层 `<p>`。

**不要这样做**

- 不要给全局 `p` 补 `margin-inline:auto` —— 段落会居中，与左对齐的标题、表格错位。
- 不要把外壳的 `max-width` 写在段落所在的**同一个元素**上：它既当容器又当文本，会被撑成通栏。这是页面出现超宽板块的头号原因，写新页时特别留意。
- 不要写 `max-width:940px` 字面值，写 `var(--maxw-text)`。

> **为什么外壳不封顶**：早期 `--maxw` 是 1180px，正文列却被各页写死成 772 / 790 / 820 / 840 / 860 / 920 / 1160 八个值，而顶栏又撑到 1400 —— 左右各空 314px 白白浪费，这才是「页面太窄」的真凶。现在外壳通栏、正文列统一 1440，视觉密度靠 `padding` 与行宽控制。

---

## 02 设计 token

token 分三层理解：

- **核心层** —— 配色 / 形状 / 字体 / 版心。定义在 `theme.css` 第 1 节，改这里全站生效。
- **别名层** —— 把各子页历史变量名归一到核心层，让老页面的组件 CSS 一行不改也能换肤。
- **体例层** —— 各页自带的五阶段色与字号间距刻度，**不进** `theme.css`。

### 2.1 配色

#### 背景层

| token | 值 | 用途 |
|---|---|---|
| `--bg` | `#f7f8fa` | 页面底色 |
| `--band` | `#eef1f5` | 表头 / 分带 / 页脚 |
| `--surface` | `#ffffff` | 卡片面 |
| `--card` | `#ffffff` | 卡片面（同 `--surface`） |
| `--panel` | `#ffffff` | 面板（同 `--surface`） |
| `--code` | `#f1f5f9` | 代码块底 |

#### 文字层

| token | 值 | 用途 |
|---|---|---|
| `--ink` | `#0f172a` | 标题 / 主文字 |
| `--ink-2` | `#334155` | 正文 / 次强 |
| `--ink-3` | `#64748b` | 弱文字 |
| `--muted` | `#64748b` | 说明文字 |
| `--muted-2` | `#8494a8` | 最弱 / mono 注释 |

#### 描边层

| token | 值 | 用途 |
|---|---|---|
| `--line` | `#dfe6ef` | 常规描边 / 分隔线 |
| `--line-2` | `#c3ceda` | 强描边 |
| `--border` | `#dfe6ef` | 同 `--line` |

#### 主色 · 青

| token | 值 | 用途 |
|---|---|---|
| `--accent` | `#0d9488` | 主色 / 眉标 / 选中态 |
| `--accent-ink` | `#0f766e` | 主色深（正文可读） |
| `--accent-soft` | `#e3f5f2` | 主色浅底 |

#### 语义色

| token | 值 | 用途 |
|---|---|---|
| `--warn` / `--warn-soft` | `#b45309` / `#fdf3e3` | 注意、口径说明 |
| `--danger` / `--danger-soft` | `#b91c1c` / `#fdeceb` | 红线、拒收、风险 |
| `--ok` / `--ok-soft` | `#047857` / `#e6f4ef` | 正向、达标 |
| `--info` / `--info-soft` | `#475569` / `#eef1f5` | 中性提示 |

> 语义色一律**成对使用**：深色给文字与图标，浅色给底。单独用浅色当文字、或深色当大面积底，都会掉出这套色阶的对比度。

### 2.2 形状与投影

| token | 值 | 用在哪 |
|---|---|---|
| `--radius` | `8px` | 面板、卡片、表格外框、节点、白底正文卡 |
| `--radius-sm` | `5px` | 小标签、按钮、手风琴、阶段带、导航项 |
| `--shadow` | `0 1px 2px rgba(15,23,42,.05), 0 10px 26px -16px rgba(15,23,42,.2)` | 常规浮起 |
| `--shadow-hover` | `0 2px 6px rgba(15,23,42,.07), 0 18px 40px -18px rgba(13,148,136,.28)` | hover 浮起（带一层青调） |

### 2.3 字体

| token | 值 | 用途 |
|---|---|---|
| `--sans` | `"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",system-ui,sans-serif` | 正文与标题。中文落到各系统的默认黑体，西文落到 Segoe UI。 |
| `--mono` | `"JetBrains Mono","Cascadia Mono",Consolas,"SFMono-Regular",Menlo,monospace` | 等宽场景：眉标、章节编号、表头、版本 meta、卡片标签、键值名的 `dt`、单位与数字。 |

**等宽字体的使用判据**

- 该用 `--mono`：标识性文字（眉标、编号、标签、版本号、日期）、表头 `th`、键值名 `dt`、数字与单位并列的地方。**它是「标记」，不是「正文」**，字号一律比同级正文小 1—3px。
- 不要用 `--mono`：成段的说明文字、表格单元格里的正文、任何超过一行的连续中文 —— 中文等宽读起来非常累。

> **零 webfont**：字体栈只走系统字体，不引 CDN、不加载字体文件。JetBrains Mono 缺失时自动退回 Cascadia Mono 或 Consolas，观感基本一致。这是全站「零构建、零外部依赖」的一部分。

### 2.4 别名层（37 个）

早期各子页各自定义过一套变量名（`--primary`、`--brand`、`--text`、`--r` …）。别名层把它们全部指向核心层，于是**子页只要删掉自己 `:root` 里的同名定义**，组件 CSS 一行都不用改就完成了换肤。

| 别名 | 指向 | 别名 | 指向 |
|---|---|---|---|
| `--primary` | `--accent` | `--red` | `--danger` |
| `--primary-dark` | `--accent-ink` | `--redsoft` | `--danger-soft` |
| `--primary-light` | `--accent-soft` | `--redline` | `#f3c6c4` |
| `--brand` | `--accent` | `--green` | `--ok` |
| `--brand2` | `--accent-ink` | `--oksoft` | `--ok-soft` |
| `--brand-2` | `--accent-ink` | `--safe` | `--ok` |
| `--brandsoft` | `--accent-soft` | `--amber` | `--warn` |
| `--brandline` | `#5eead4` | `--amber-bg` | `--warn-soft` |
| `--accent-dark` | `--accent-ink` | `--amber-line` | `#fcd9a8` |
| `--accent-deep` | `--accent-ink` | `--warnsoft` | `--warn-soft` |
| `--text` | `--ink` | `--warnline` | `#f3ddb4` |
| `--paper` | `--surface` | `--slate` | `--info` |
| `--ink2` | `--ink-2` | `--slate-bg` | `--info-soft` |
| `--ink3` | `--ink-3` | `--slate-line` | `--line-2` |
| `--ink-soft` | `--ink-2` | `--purple` | `#6d5ce7` |
| `--card2` | `--band` | `--r` | `--radius` |
| `--hairline` | `1px solid var(--line)` | `--r2` | `--radius-sm` |
| `--line2` | `--line-2` | `--sh` | `--shadow` |
| `--sh2` | `--shadow-hover` | | |

**规则**

- 子页要换肤时，**只删自己 `:root` 里的同名定义**，组件 CSS 一个字都不用动。
- 新写组件时直接用核心层名（`--accent` / `--ink-2` / `--radius`），不要再新增别名。
- 不要在子页 `:root` 里重新定义别名指向别的值 —— 会形成第二套色源。
- 不要把语义色与体例变量挂进别名层：`--up` / `--down` / `--lvl-a` / `--sc` 这类**不属收编范围**，归各页自己管。
- 不要删别名 —— 老页面可能还在用，删了会静默掉色。

### 2.5 体例变量（各页 `:root` 自带）

新页开工时把下面这一段整体抄走即可 —— 基准页与本文件的取值完全一致。

#### 五阶段语义色

| token | 实色 | 浅底 | 阶段 |
|---|---|---|---|
| `--s1` / `--s1s` | `#0d9488` | `#ccfbf1` | 一 · 立项与准入 |
| `--s2` / `--s2s` | `#2563eb` | `#dbeafe` | 二 · 选品与共创 |
| `--s3` / `--s3s` | `#7c3aed` | `#ede9fe` | 三 · 合规与审核 |
| `--s4` / `--s4s` | `#ea580c` | `#ffedd5` | 四 · 系统与生产准备 |
| `--s5` / `--s5s` | `#db2777` | `#fce7f3` | 五 · 交付与上架 |

#### 板块主题色开关

```css
/* 放在样式表最后，确保优先级 */
.st1{--sc:var(--s1);--scs:var(--s1s)}
.st2{--sc:var(--s2);--scs:var(--s2s)}
.st3{--sc:var(--s3);--scs:var(--s3s)}
.st4{--sc:var(--s4);--scs:var(--s4s)}
.st5{--sc:var(--s5);--scs:var(--s5s)}
.strd{--sc:var(--danger);--scs:var(--danger-soft)}
```

| 项 | 说明 |
|---|---|
| `--sc` | 板块主题色（实色）。默认 `var(--accent)` 青绿。 |
| `--scs` | 板块主题色的浅底版本。默认 `var(--accent-soft)`。 |
| 怎么用 | 给 `<section>` 或任意容器加一个 `.st1`—`.st5` / `.strd`，容器内所有引用 `var(--sc)` / `var(--scs)` 的组件立即整体换色。 |
| 谁跟着换 | `.sec-h .idx`、`details.acc`、`.dept`、`.card-h`；节点图里的 `.fstage` / `.fnode` / `.conn` 也吃 `--sc`。 |
| 谁不跟着换 | `.rl`（红线卡）固定用 `--danger`，`.srcnote` / `.warnbox` 固定用 `--warn` —— 语义色不该被板块色覆盖。 |

#### 字号刻度

| token | 值 | 典型用途 |
|---|---|---|
| `--fz-xs` | `12px` | 极弱注释、图表脚注 |
| `--fz-sm` | `13px` | 表格单元格、清单条目、卡片正文 |
| `--fz` | `14px` | 章节导语 `.lede` |
| `--fz-md` | `15px` | 强调正文（红线卡的 `.mid`） |
| `--fz-lg` | `17px` | 章节内的二级标题 `.sec-h h2` |
| `--fz-xl` | `21px` | 卡片标题上限 |
| `--fz-2xl` | `29px` | 大数字、封面级标题 |

另有三个**不在刻度里、但固定使用**的字号：**body 基线 14.5px**、**章节标题 `h2` 19px**、**页面主标题 `clamp(23px,2.9vw,32px)`**。这三个值请直接照抄，不要改成刻度里的近似值。

#### 间距刻度

| token | 值 | 用途 |
|---|---|---|
| `--sp1` | `4px` | 行内微间距 |
| `--sp2` | `8px` | 图标与文字、标签之间的间距 |
| `--sp3` | `12px` | 小节内元素间距 |
| `--sp4` | `16px` | 卡片内分组间距 |
| `--sp5` | `22px` | 块与块之间 |
| `--sp6` | `30px` | 大分区间距 |
| `--sp7` | `42px` | 章节之间的呼吸 |

> **现状提醒**：这七个刻度目前**已定义但基本没有消费者** —— 既有组件的间距写的是字面 px（完整清单见 [05 节](#05-间距刻度与响应式断点)）。新写组件时优先引用刻度，逐步把字面值收编回来。

#### 布局尺度

| token | 值 | 说明 |
|---|---|---|
| `--bar-h` | `50px` | 顶栏高度。同时决定 `section` 的 `scroll-margin-top`（锚点跳转不被顶栏压住）与节点图粘性侧栏的 `top`。 |
| `--side-ink` | `#94a3b8` | 顶栏链接的默认色与品牌副标色。 |
| `--side-ink-hi` | `#5eead4` | 预留的顶栏高亮色（当前未启用）。 |
| `--side-hi` | `rgba(13,148,136,.18)` | 顶栏链接 hover 与选中态的底色。 |
| ~~`--sidew`~~ | ~~`250px`~~ | **已废弃** —— 深色侧栏并入顶栏后无消费者，可安全删除。 |
| ~~`--side-bg`~~ | ~~`#141c2b`~~ | 同上 |
| ~~`--side-mut`~~ | ~~`#5b6b80`~~ | 同上 |

---

## 03 页面骨架

四段式：**墨黑顶栏 → 页头 → 白底正文卡 → 分带页脚**，左下角再挂一个返回首页浮钮。下面这份是可直接另存为新页的最小骨架。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="data:image/svg+xml,...">
<title>页面标题</title>
<meta name="description" content="一句话摘要">
<link rel="stylesheet" href="../theme.css">   <!-- ① 必须在自身 <style> 之前 -->
<style>
/* ② 只写本页专属的体例变量与组件，不写配色 */
:root{
  --s1:#0d9488; --s2:#2563eb; --s3:#7c3aed; --s4:#ea580c; --s5:#db2777;
  --s1s:#ccfbf1; --s2s:#dbeafe; --s3s:#ede9fe; --s4s:#ffedd5; --s5s:#fce7f3;
  --fz-xs:12px; --fz-sm:13px; --fz:14px; --fz-md:15px;
  --fz-lg:17px; --fz-xl:21px; --fz-2xl:29px;
  --sp1:4px; --sp2:8px; --sp3:12px; --sp4:16px; --sp5:22px; --sp6:30px; --sp7:42px;
  --bar-h:50px;
  --side-ink:#94a3b8; --side-ink-hi:#5eead4; --side-hi:rgba(13,148,136,.18);
  --sc:var(--accent); --scs:var(--accent-soft);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);
     font-size:14.5px;line-height:1.76;-webkit-font-smoothing:antialiased}
/* ③ 只抄你要用的组件 CSS —— 见第 04 节 */
</style>
</head>
<body>

<!-- ══ 1. 顶栏（墨黑 sticky） ══ -->
<header class="s-bar">
  <div class="s-bar-in">
    <span class="s-brand">GERVAS<em>日常 · Agent 作品集</em></span>
    <nav class="s-nav" id="topnav" aria-label="章节导航">
      <a href="#s0" data-sec="s0">00 章节一</a>
      <a href="#s1" data-sec="s1">01 章节二</a>
    </nav>
  </div>
</header>

<!-- ══ 2. 页头 ══ -->
<div class="s-head">
  <span class="s-eyebrow">分类 · 类型</span>
  <h1 class="s-h1">页面主标题</h1>
  <p class="s-lede">一到三句话讲清这页是什么、给谁看。</p>
  <div class="s-meta">
    <span>文档版本 <b>V1.0</b></span>
    <span>编制日期 <b>2026-09-21</b></span>
  </div>
  <div class="s-chips">
    <span class="s-chip">关键词一</span>
    <span class="s-chip">关键词二</span>
  </div>
</div>

<!-- ══ 3. 正文卡 ══ -->
<div class="s-body">
  <main class="s-main">
    <section id="s0">
      <div class="sec-h"><span class="idx st1">01</span><h2>章节标题</h2><span class="hint">副注</span></div>
      <p class="lede">章节导语。</p>
      <!-- 组件放这里 -->
    </section>
  </main>
</div>

<!-- ══ 4. 页脚 ══ -->
<footer class="s-foot">
  <div class="s-foot-in">
    <b>GERVAS</b>
    <span>页面短名 · V1.0</span>
    <span class="sp">Copyright 2026 gervas.wang</span>
  </div>
  <div class="s-disc"><p>免责声明或数据口径说明。</p></div>
</footer>

<a class="g-pill" href="../index.html" title="返回作品集首页">返回首页</a>
</body>
</html>
```

### 3.1 逐层取值

| 层 | 类名 | `max-width` | `padding` | 说明 |
|---|---|---|---|---|
| 顶栏底 | `.s-bar` | — | — | `#0f172a` 墨黑，`position:sticky;top:0`，`z-index:60` |
| 顶栏内层 | `.s-bar-in` | `var(--maxw)` | `0 32px` | 高度 `--bar-h`（50px），flex 居中，gap 12px |
| 页头 | `.s-head` | `var(--maxw-read)` | `44px 32px 0` | 眉标 → h1 → lede → meta → chips，五件套 |
| 主体 | `.s-body` | `var(--maxw-read)` | `26px 32px 50px` | 承接所有 `section` |
| 正文卡 | `.s-main` | `var(--maxw-read)` | `8px 34px 40px` | 白底 + 1px `--line` + 10px 圆角 |
| 页脚底 | `.s-foot` | — | — | `--band` 底 + 1px 上描边 |
| 页脚内层 | `.s-foot-in` | `var(--maxw)` | `26px 32px 10px` | flex wrap；`b` 是 mono 品牌字，`.sp` 把版权推到最右 |
| 免责 | `.s-disc` | `var(--maxw)` | `0 32px 24px` | **外壳层**，内层 `<p>` 吃 940 行宽 |

### 3.2 骨架三处硬性要求

**要这样做**

- `<link rel="stylesheet" href="../theme.css">` 放在本页 `<style>` **之前** —— 基础样式先加载，本页样式才能正确覆盖它。
- 页头五件套顺序固定：眉标 → `<h1>` → `.s-lede` → `.s-meta` → `.s-chips`。缺哪件就删哪件，不要换顺序。
- 章节一律 `<section id="sN">` + `<div class="sec-h">`，顶部描边与锚点偏移由元素选择器统一给。

**不要这样做**

- 不要把 `<link>` 写在 `<style>` 后面 —— 本页样式会被基础样式压回一部分，出问题时极难定位。
- 不要在 `.s-head` 里再包一层 div 做「版心」—— 它本身已经是正文列。
- 不要给每个 `section` 手写 `padding-top` / `border-top` —— 会与统一规则打架。

---

## 04 组件清单

全部是纯 CSS 类，不依赖任何框架与外部库。需要哪组就把对应 CSS 块抄进本页 `<style>`，HTML 按下面的写法组织。表里的取值就是 `theme.css` 与基准页里的实际值。

### 4.1 布局

| 类名 | 用途 | 关键取值 |
|---|---|---|
| `.sec-h` | 章节头容器 | flex + `align-items:baseline`，gap 12px，`margin-bottom:14px`，`flex-wrap:wrap` |
| `.sec-h .idx` | 左侧编号胶囊 | mono 11px 700，字色 `--sc` / 底 `--scs`，padding 3px 10px，圆角 `--radius-sm`；配 `.st1`—`.st5` / `.strd` 换色 |
| `.sec-h h2` | 章节标题 | 19px 700，字距 -.012em，行高 1.4 |
| `.sec-h .hint` | 右侧副注 | mono 11px，`--muted-2`；排不下时靠 `flex-wrap` 落到下一行 |
| `.lede` | 章节导语 | 14px，`--ink-2`，行高 1.78，行宽 `--maxw-text`，`margin-bottom:16px` |
| `.panel` | 通用白卡 | `--card` 底 + 1px `--line` + `--radius` + padding 20px |
| `.grid` | 网格基类 | `display:grid`，gap 14px。必须与 `.g2` / `.g3` 同用 |
| `.g2` / `.g3` | 2 / 3 等分列 | `repeat(n,minmax(0,1fr))`。1100 以下 `.g3` 退 2 列，760 以下两者都退 1 列 |

```html
<section id="s1" class="st1">
  <div class="sec-h">
    <span class="idx st1">01</span>
    <h2>章节标题</h2>
    <span class="hint">副注</span>
  </div>
  <p class="lede">章节导语，连续中文会自动收在 940px 行宽内。</p>

  <div class="grid g2">
    <div class="panel">左卡</div>
    <div class="panel">右卡</div>
  </div>
</section>
```

### 4.2 内容

| 类名 | 用途 | 关键取值 |
|---|---|---|
| `.rl` | 红线卡：硬约束、警示事项 | 边框 `#f3c6c4` + 底 `--danger-soft` + `--radius` + padding `15px 17px`。`h4` mono 11.5px 700 `--danger`；`.mid` 15px 700；`p` 13.5px 行高 1.72 |
| `.srcnote` | 数据口径 / 来源说明条 | `--warn-soft` 底 + `--warnline` 边，padding `14px 16px`，`margin-bottom:16px`；`b` 用 `--warn` |
| `.card` + `.card-h` + `.card-b` | 详情卡，顶部一条 3px 主题色 | `#fbfcfd` 底；`.card-h` padding `14px 18px`、底色 `--scs`、`border-top:3px solid var(--sc)`；`.card-b` padding 18px |
| `.kv` | 键值网格（`dl` + `dt`/`dd`） | 列宽 `104px minmax(0,1fr)`，gap `10px 16px`；`dt` mono 11.5px 700 `--accent-ink`；560 以下退单列 |
| `.warnbox` | 卡内注意事项盒 | `--warn-soft` 底 + `--warnline` 边，padding `14px 16px`；`h5` mono 11.5px 700 `--warn` |
| `.dept` | 部门 / 角色块（左 3px 主题色条） | `padding-left:14px`；`.role` mono 11px `--muted-2`；`.ntag` mono 10.5px 描边胶囊；`.note` 用 `--scs` 底 |
| `.empty` | 空态占位 | padding 26px，居中，13px `--muted` |

```html
<!-- 红线卡：硬约束、不可妥协项 -->
<div class="grid g3">
  <div class="rl">
    <h4>红线 · 类别</h4>
    <div class="mid">一句话结论</div>
    <p>展开说明。</p>
  </div>
</div>

<!-- 数据口径 / 来源说明条 -->
<div class="srcnote"><b>数据口径</b>：数值来自何处、如何推算、不构成何种承诺。</div>

<!-- 详情卡 + 键值网格 + 注意事项盒 -->
<div class="card st1">
  <div class="card-h"><span class="tag">标签</span><h3>卡片标题</h3></div>
  <div class="card-b">
    <dl class="kv">
      <dt>键名</dt><dd>值</dd>
    </dl>
    <div class="warnbox"><h5>注意事项</h5><ul><li>…</li></ul></div>
  </div>
</div>
```

### 4.3 表格

| 选择器 | 用途 | 关键取值 |
|---|---|---|
| `.tblwrap` | 表格外框 | 1px `--line` + `--radius` + `overflow:hidden`，`margin-bottom:20px`；窄屏 760 以下改为横向滚动 |
| `table` | 表格本体 | 100% 宽，`border-collapse:collapse`，13px。窄屏 `min-width:600px` + 12.5px |
| `th` | 表头 | `--band` 底，`#475569` 字，mono 11px 700，字距 .06em，padding `10px 13px`，下描边 |
| `td` | 单元格 | 13px，`--ink-2`，`vertical-align:top`，padding `10px 13px`，下描边 |
| 条纹 | 偶数行底色 | `tbody tr:nth-child(even) td{background:#fbfcfd}`；末行去描边 |

```html
<div class="tblwrap">
  <table>
    <thead>
      <tr><th style="width:160px">列一</th><th>列二</th></tr>
    </thead>
    <tbody>
      <tr><td><b>强调项</b></td><td>内容</td></tr>
    </tbody>
  </table>
</div>
```

> **列宽只写在表头**：给 `th` 一个固定 `width`，其余列不给宽度自动均分。全部列都写死会让窄屏横滑距离变得很长。

### 4.4 交互

| 类名 | 用途 | 关键取值 / 约束 |
|---|---|---|
| `.tabs` / `.tab` / `.tab.on` / `.tabpane` / `.tabpane.on` | 选项卡切换 | 按钮圆角 `--radius-sm`、padding `7px 14px`；选中态 `--accent-soft` 底 + `--accent` 边 + `--accent-ink` 字。**`.tabpane` 必须与 `.tabs` 同级**，靠 `data-pane` 与 `id` 配对，约 20 行 JS |
| `details.acc` | 手风琴（原生，零 JS） | 左 3px `--sc` 边；`summary` padding `13px 16px`、14.5px 700；`::after` 显示 `+` / `–`；展开时 `summary` 底变 `--scs` |
| `.s-drop` / `.s-dropbtn` / `.s-panel` | 顶栏二级下拉 | 面板 `top:calc(100% + 8px)`、`min-width:214px`、圆角 10px、阴影 `0 20px 44px -18px rgba(15,23,42,.42)`；`hover` 展开只在 `(hover:hover) and (min-width:901px)` 生效 |
| `.g-pill` | 返回首页浮钮 | 定义在 `theme.css`，子页直接用。fixed、右下 18px / 20px、`#0f172a` 底、mono 12px、`z-index:9999`。**必须贴底**，贴顶会被墨黑顶栏压住 |

```html
<!-- 选项卡：.tabs 与 .tabpane 必须是同级兄弟 -->
<div class="tabs">
  <div class="tab on" data-pane="p1">第一页</div>
  <div class="tab" data-pane="p2">第二页</div>
</div>
<div class="tabpane on" id="p1">…</div>
<div class="tabpane" id="p2">…</div>

<!-- 手风琴：原生 details，不需要一行 JS -->
<details class="acc st2" open>
  <summary>分组标题<span class="cnt">6 条</span></summary>
  <div class="body"><ul><li>…</li></ul></div>
</details>
```

> **页面内可以有多组选项卡**：切换脚本是按 `.tab` 的父容器分组的，所以同一个页面放两三组互不干扰。但同一个父容器里只能有一组。

### 4.5 重型组件 · 全流程节点图

只在长流程页用，别默认带上。

| 项 | 说明 |
|---|---|
| 现成实现 | 完整版 `pages/sams-onboarding-sop-2026.html`（阶段色带 + 蛇形节点流 + 右侧粘性详情卡）；轻量版 `pages/sams-onboarding-flow-2026.html`。要做流程类页面时直接拿其中一个改，不要从零写。 |
| 结构 | `.flow-layout`（flex，gap 20px）= 左 `.flow > #flowStage` + 右 `.detail`（`flex:0 0 340px`，粘性）。节点流内部是 `.fstage`（阶段色带）→ `.frow`（一行节点）→ `.fnode` / `.conn` / `.wrap-break` / `.wrap-turn`。 |
| 尺度变量 | `--nw:150px`（节点最小宽，实际 `flex:1 1 var(--nw)` 会伸展填满整行，`max-width:260px` 封顶）、`--ngap:8px`、`--nconn:16px`。JS 与 CSS 共用这三个值，改一处必须两边同步。 |
| 列数公式 | 一行 k 个节点 = 2k−1 个 flex 项、2k−2 个 gap → `k ≤ (行宽 + conn + 2·gap) / (nw + conn + 2·gap)`。 |

**五条必须遵守的实现约束**

1. **「行宽」是 `.frow` 的宽度，不是 `#flowStage.clientWidth`。** 两者之间隔着 `.fstage` 的 `padding` + `border`（实测 28px），不减掉就会算多一列，而后端放不下 → JS 以为 4 列、DOM 却排成 3+1。要用 `framePad()` 实读，不要写死 28。
2. **`.frow{justify-content:center}` 必须无条件。** 满行时节点靠 `flex:1` 伸展刚好铺满，居中不产生位移；只有末行不满（阶段节点数 % 列数 ≠ 0）时才起作用，把余下的 1—2 个节点居中，正好落在居中下箭头正下方。绑进媒体查询就会让孤节点贴左边缘、箭头留在中间。
3. **首屏 `clientWidth` 会量成 0。** 必须有 `lastCols` 缓存（列数没变就不重建 DOM，避免闪屏）+ `window.load` / `document.fonts.ready` 两次重排纠正。
4. **侧栏 340px 与单栏断点 1270 是反推出来的常数。** 两栏时 `#flowStage = 视口 − 543`；4 列要求 `.frow ≥ 696px` → `#flowStage ≥ 724` → 视口 ≥ 1267。改侧栏宽度或 `--nw` 都必须重算，否则 1267—1280 这一段会掉回 3 列。
5. **列数不取「最大放得下」，取「排出来不参差」。** `chooseCols()` 按「总行数×3 + 各阶段末行空槽总数」打分取最小 —— 只看空槽会让窄屏一路塌成 1 列，只看行数会选出刚好放下但参差的列数。

---

## 05 间距刻度与响应式断点

### 5.1 组件间距现状

间距刻度在 [2.5](#25-体例变量各页-root-自带) 列过，这里补上**组件实际在用的字面值** —— 新写组件时照着这套节奏走，视觉密度就不会跑偏。

| 位置 | 值 | 备注 |
|---|---|---|
| 页面主标题 `.s-h1` | `clamp(23px,2.9vw,32px)` | 唯一使用 `clamp()` 的地方 |
| 页头上留白 `.s-head` | `44px` | 窄屏 640 以下降到 `30px 18px 0` |
| 正文卡内边距 `.s-main` | `8px 34px 40px` | 窄屏 900 以下 `8px 18px 30px` |
| 章节上间距 `section` | `28px` | 首节 `22px`，并去掉顶部描边 |
| 章节头下间距 `.sec-h` | `14px` | 与 `.lede` 的 16px 同属「标题—正文」节奏 |
| 导语下间距 `.lede` | `16px` | — |
| 面板内边距 `.panel` | `20px` | 网格里的卡片一律 20px |
| 网格间隙 `.grid` | `14px` | 与 `.sec-h` 的下间距同值 |
| 红线卡内边距 `.rl` | `15px 17px` | 比面板略紧，因为它是提示而非内容 |
| 表格外框下间距 `.tblwrap` | `20px` | 紧邻下一个区块时用内联 `style="margin-bottom:0"` 归零 |
| 单元格内边距 `th,td` | `10px 13px` | 窄屏 760 以下 `9px 11px` |
| 详情卡内边距 | `.card-h` `14px 18px` / `.card-b` `18px` | — |
| 键值间隙 `.kv` | 列 `104px + 1fr`，gap `10px 16px` | 560 以下退单列 |

### 5.2 响应式断点

七档，全部 `max-width`，桌面优先。

| 断点 | 触发条件 | 归属 | 动作 |
|---|---|---|---|
| **1270px** | ① 节点图放不下「节点流 + 340px 粘性侧栏」两栏；② 首页顶栏分类 chip 自然宽约 1189px、超过视口 | 重型组件 / 骨架 | ① `.flow-layout` 转纵向，`.detail` 退回节点图下方（节点流仍是 4 个一行）；② 首页 `#catnav` 开横向滚动（隐藏滚动条） |
| **1100px** | 三列卡排不下 | 布局 | `.g3` → 2 列 |
| **900px** | 顶栏项目排不下 | 骨架 | `.s-main` 内边距收窄；`.s-nav` 开横向滚动（隐藏滚动条）；下拉面板改 `position:fixed` 相对视口定位 |
| **760px** | 宽表被压成「一字一列」 | 组件 | `.tblwrap` 横向滚动 + `table{min-width:600px;font-size:12.5px}`；同时 `.g3`/`.g2` → 1 列 |
| **640px** | 小屏 | 骨架 | 品牌副标隐藏；导航项收紧到 `5px 8px`；`.s-head` 与各内层 `padding-inline` → `18px` |
| **600px** | — | **冗余** | 又写了一遍 `.s-brand em{display:none}`，与 640 那条完全重复 |
| **560px** | 键值两列排不下 | 组件 | `.kv` → 单列，`dt` 补上间距 |

> **断点只用 max-width**：全站七档。写新组件时优先复用这七个数，不要新造 `1024px`、`768px` 这类数 —— 断点一多，测试档位就爆炸。

### 5.3 已知冗余与待清理

1. **体例变量三个死值**：`--sidew:250px` / `--side-bg:#141c2b` / `--side-mut:#5b6b80`。深色侧栏并入顶栏后已无任何消费者，可整条删除（`--side-ink` / `--side-ink-hi` / `--side-hi` 仍在顶栏使用，保留）。
2. **重复的 600px 档**：`.s-brand em{display:none}` 在 640 与 600 各写了一次 —— 删掉 600 那一档。
3. **间距刻度未被引用**：`--sp1`—`--sp7` 已定义，但既有组件的间距写的是字面值（见上方现状表）。建议新组件优先引用，逐步收编。
4. **七个长页各有一条死规则**：`.layout{grid-template-columns:250px minmax(0,1fr) 218px;…}` 被同文件末尾的 `.layout{display:block}` 完全覆盖。因为 `--maxw` 现在是 `none`，只改里面的值不安全，应整条删除。涉及：`skill`、`skill-spec`、`skill-diy`、`el-nino-2027-impact`、`pet-bottle-cost-2026`、`sams-plant-based-puree-2026`、`ebook-treasure-chest`。
5. **两条山姆页面职责重叠**：`sams-onboarding-flow-2026`（轻量流程概览）与 `sams-onboarding-sop-2026`（完整作业手册）。旧页去留待定 —— 留的话应明确「概览 / 手册」的分工，不留就整页删除并同步删掉首页登记。

---

## 06 新建子页清单

### 6.1 必须做

1. **引 `theme.css`**，且放在本页 `<style>` 之前。
2. **走四段骨架**：`.s-bar` → `.s-head` → `.s-body`/`.s-main` → `.s-foot`。
3. **抄一份 `:root`**：五阶段色、字号刻度、间距刻度、`--bar-h`、`--side-ink` 三项、`--sc`·`--scs`。数值不要改。
4. **章节用 `<section id="sN">` + `.sec-h`**，编号胶囊配 `.st1`—`.st5` 轮转。
5. **连续正文写裸 `<p>`**，行宽交给全局兜底规则。
6. **颜色一律引用变量**（写成 `var(--accent)` 这样），不写字面十六进制值。
7. **页尾挂 `.g-pill`** 返回首页，并在 `index.html` 的 `PAGES` 里登记一条。

### 6.2 禁止做

1. **不自带配色**：不要在本页 `:root` 里写十六进制色值。
2. **不硬编码正文列宽度**：`max-width:1180px` 这类一律换成 `var(--maxw-read)`。
3. **不给 `p` 加 `margin-inline:auto`** —— 段落会与左对齐的标题错位。
4. **不在 `theme.css` 注释里写 `*` 紧邻 `/`**。
5. **不给 `.s-nav` 加 `overflow-x:auto`** —— 它是全站 379 个子页共用的组件，桌面档会把下拉面板裁掉；它只在 900 断点里开。
   **唯一例外**：首页 `#catnav`（该 id 全站仅 index.html 使用，内部只有 `<a>`、无下拉面板；搜索面板是 `position:fixed` 挂在 `body` 上）在 `≤1270` 档开了横向滚动 —— 因为分类增至 8 个后 chip 自然宽约 1189px 会撑破 1024 档。**新写页面若要类似兜底，必须用页面专属 id，不得改 `.s-nav` 类。**
6. **不引 CDN、webfont、外部 JS 或图标字体** —— 全站零构建、零外部依赖，图标一律内联 SVG。
7. **不把 `.s-disc` 当段落用**：必须是 `<div class="s-disc"><p>…</p></div>`。

### 6.3 在首页登记

往 `index.html` 脚本里的 `PAGES` 数组加一条：

```js
{
  title: "页面标题",
  desc: "一到两句话摘要，会显示在首页卡片上。",
  kind: "手册",          // 手册 / 长文 / 工具 / 仪表盘 / 收藏
  url: "pages/新页.html",
  date: "2026-09-21",    // 决定列表排序与页脚「最近更新」
  category: "包装包材",   // 包装包材 / 采购与供应链 / 产品与渠道 / 本草与健康 / 建站与技术 / AI与Agent / 写作与创作 / 生活杂记
  tags: ["关键词一", "关键词二", "关键词三"]
}
```

> **`PAGES` 是唯一数据源**：加一条记录，列表、分类筛选、统计计数与页脚「最近更新」会自动跟上。头像类配图走可选的 `image` / `imageAlt` 字段，精选头条加 `feature:true`。

### 6.4 交付前自检

| 序 | 检查项 | 通过标准 |
|---|---|---|
| 1 | **四档宽度无横滑** | 1920 / 1280 / 800 / 420 四档下，页面都不出现横向滚动条 |
| 2 | **行宽分层正确** | 长段落不超 940px；表格与卡片吃满正文列（1440 内） |
| 3 | **主色唯一** | 全页主色为青 `#0d9488`，没有残留的旧蓝或旧红 |
| 4 | **顶栏行为** | 吸顶正常，滚动时当前章节高亮；窄屏横滑不裁下拉面板 |
| 5 | **浮钮位置** | `.g-pill` 贴屏幕右下，不遮顶栏、不压页脚文字 |

---

本文件描述的是当前已上线的状态。规范随站点演进而更新，取值一律以 `theme.css` 与基准页的实际写法为准。
