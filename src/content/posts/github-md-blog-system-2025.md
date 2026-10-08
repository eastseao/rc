---
title: "GitHub 推文与 Markdown 博客系统"
description: "推文卡片结构与 postsData 字段、_posts 命名 YYYY-MM-DD-slug、Front Matter 规则、分类标签与 md 生成器子页。"
pubDatetime: 2025-10-04
category: "建站与技术"
kind: "长文"
tags: ["_posts", "Front Matter", "分页", "md 生成器"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00165-2025-10-03 我想在 GitHub 上创建我的 md 推文博客系统（用户名 hdbuyer）00166-2025-10-03 GitHub 推文博客系统设计方案00167-2025-10-04 GitHub 推文博客系统设计与实现00169-2025-10-04 GitHub Markdown 博客系统需求梳理

## 01 · 系统目录结构与导航怎么演进来的（00165 / 00166 / 00167）

用户已建好库、建好`index.html`，要在上面跑一套推文博客。源笔记先给了完整目录结构，再在多轮里把导航、留言板块来回调整。

| 导航迭代 | 源笔记演变 |
|---|---|
| **00165 / 00166 初版** | 左侧**隐藏式（折叠）导航栏**：首页、分类、标签、留言、关于我。 |
| **00166 改版** | 导航栏「还是不好看」→ 换格式 → 要求**去掉留言区域**。 |
| **00167 定稿** | 顶部导航：**首页、分类、标签、关于我**。 |
| **00169 再简** | 顶部导航进一步收成**首页、标签、关于我**，推文放`_posts/`。 |

> **留言板块的去留**：初版要求推文下方留一个**留言板块，留言必须备注网名、所有人留言公开**；到 00166 第二轮就明确「去掉留言区域」。这条线只在早期方案里出现，最终版不带留言。

## 02 · _posts 文件命名与 Front Matter 规则（00165 / 00166）

这是整套系统最硬的规则层。文件名、Front Matter、时间、分类、标签都有约定，首页靠这些自动排序、打标签。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">文件命名</h3><div style="margin:14px 0">YYYY-MM-DD-slug-title.md<span># 示例（全小写、连字符、无空格）</span>2024-03-15-getting-started-with-github-pages.md 2024-03-14-my-first-tweet-blog-post.md</div><ul style="margin:10px 0 0;padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:6px">全小写、用<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">-</code>分词、避免空格与特殊字符。</li><li>日期前缀决定排序——首页按创建时间最新在前。</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">Front Matter（md 最开头的 YAML）</h3><div style="margin:14px 0">--- layout: post title: &quot;文章标题&quot; date: 2024-01-15 09:00:00 +0800 last_modified_at: 2024-01-18 14:30:00 +0800 categories: [技术] tags: [GitHub, 教程] excerpt: &quot;摘要……&quot; ---</div><ul style="margin:10px 0 0;padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:6px">必须放在 md<b>最开头</b>，前后用<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">---</code>包围。</li><li>00169 后期要求<b>Front Matter 标准去掉分类</b>。</li></ul></div></div>

| 维度 | 规则（照录） |
|---|---|
| **时间格式** | ISO 8601：`createTime: "2024-03-15T10:30:00Z"`。创建时间**不可改**，修改时间每次更新时刷新。 |
| **分类** | 预设主分类：技术 / 生活 / 读书 / 旅行 / 思考 / 工作；每篇**有且仅有 1 个主分类**，2–4 个汉字，保持数量有限。 |
| **标签** | 每篇**2–5 个标签**；技术术语优先英文（JavaScript / CSS / GitHub），避免过宽泛。 |

## 03 · 推文卡片怎么排、每页几条、怎么翻页（00165 / 00167）

首页把每篇推文渲染成一张卡片：**正中是标题，标题下方依次是创建时间、修改时间、标签、分类**；按创建时间倒序，每页最多 20 篇，余下在底部用序号翻页。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00167 · 推文数据结构</span><h3>每篇推文对象长这样</h3></div><div style="padding:14px 16px"><div style="margin:14px 0">{ id: 1, title: &quot;我的第一篇推文&quot;, createdAt: &quot;2024-10-01&quot;, updatedAt: &quot;2024-10-01&quot;, tags: [&quot;JavaScript&quot;, &quot;GitHub&quot;], categories: [&quot;技术&quot;] }</div><div style="overflow-x:auto;margin:16px 0;margin:14px 0 0"><table><thead><tr><th style="width:160px">字段</th><th>说明</th></tr></thead><tbody><tr><td><b>id</b></td><td>唯一标识，数字递增。</td></tr><tr><td><b>title</b></td><td>卡片正中显示的标题。</td></tr><tr><td><b>createdAt / updatedAt</b></td><td>创建时间 / 修改时间，YYYY-MM-DD；首页按 createdAt 倒序。</td></tr><tr><td><b>tags / categories</b></td><td>数组，即使只有一项也要用方括号。</td></tr></tbody></table></div></div></div>

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">分页逻辑</h3><p style="font-size:13.5px;color:inherit;line-height:1.72"><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">postsPerPage = 20</code>；<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">startIndex = (currentPage-1)*20</code>，<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">endIndex = startIndex+20</code>，对数组 slice；<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">totalPages = Math.ceil(总数/20)</code>；底部渲染上一页 / 页码 / 下一页，点页码切页并回到顶部。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">分类 / 标签页</h3><p style="font-size:13.5px;color:inherit;line-height:1.72">分类页、标签页各自用<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">Set</code>去重收集全站分类/标签，渲染成卡片并标注该分类下的推文数量。</p></div></div>

> **「首页打开看不到推文卡片」怎么查（00166 实录）**
> - 推文数据有没有真正加载进页面——早期方案数据在`js/script.js`的`postsData`数组里，忘了填或路径错都会空。
> - JS 控制台有没有报错；卡片容器`#posts-container`是否真被渲染。

## 04 · md 推文生成器子页面（00165 / 00169）

用户不想手写 Front Matter，于是要一个**子网页**：输入文档标题和内容，自动生成一篇 md 推文、自动做好标签和分类，再放到 _posts 里推送首页。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00165 / 00169 · 生成器思路</span><h3>填表单 → 出一段可粘贴的 md</h3></div><div style="padding:14px 16px"><ol style="margin:0;padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:8px">表单字段：标题、内容、创建日期、修改日期、标签（逗号分隔）、分类（逗号分隔）。</li><li style="margin-bottom:8px">点「生成」后拼成一个推文对象，<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">JSON.stringify(postObject, null, 2)</code>输出，供复制。</li><li style="margin-bottom:8px">id 用<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">Date.now()</code>临时生成；日期默认填今天。</li><li>把生成的 md / JSON 贴进<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">_posts/</code>或<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">data/posts.json</code>，push 到仓库即上线。</li></ol><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:14px;margin-bottom:0"><b>用户原话</b>：「我是一个新手，我会利用 md 生成器生成的文章在 posts 里边提交文件，太复杂的过程，比如 json 文件目前我还操作不了。」——这正是下一节要解决的痛点。</div></div></div>

## 05 · 新手简化：只改 _posts 下的 md 就同步主页（00169）

00169 的收尾是一次「减负」：用户把前面那套文件都传上去了，能显示标题和导航，但**中间看不到推文**；而且 json、改 main.js 对他太难。最终诉求收敛成一句——**只想通过修改 _posts 下的 md 文件来同步主页，其他文件不动**。

| 阶段 | 做法 | 卡点 |
|---|---|---|
| **早期** | 数据放`data/posts.json`，前端 fetch 加载 | 「json 文件目前操作不了」。 |
| **中期** | 提示去`assets/js/main.js`、`tags.js`加文章数据 | 「这种操作对我来说还是太难」。 |
| **最终** | 重做逻辑：**只往 _posts/ 放 md 文件**，主页自动按最新日期读取并列出推文；首页**不一定用卡片**，按最新日期不断更新即可 | 其他文件不动，降低到「只会传 md」。 |

> **这条线的价值**：推文博客从「前端写死 postsData / 维护 json」演进到「md 即数据、仓库即数据库」——用户每发一篇就是往`_posts/`丢一个按命名规则的 md，主页自动重排。这与第 1 篇里 Jekyll 自动渲染 _posts 的思路一致，只是这里用前端在 md/JSON 之间做了一轮适配。
