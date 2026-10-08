---
title: "GitHub 主页 Logo·点赞·DOCTYPE 修改"
description: "Canvas 漂浮 Logo、红心点赞 localStorage 防重、不蒜子 PV/UV、滚动进度条与主页精简导航。"
pubDatetime: 2025-10-01
category: "建站与技术"
kind: "长文"
tags: ["Canvas 粒子", "localStorage 点赞", "不蒜子", "视频旋转"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00145-2025-10-01 个人主页 Logo 背景动态实现00147-2025-10-01 网页优化与红心点赞功能添加00148-2025-10-01 主页修改 <!DOCTYPE html> <html lang=…>

## 01 · 把悬浮粒子背景换成大小不一的 Logo（00145）

00145 的诉求：背景上原本悬浮的圆形粒子，换成**直径大小不一的 Logo**。做法是保留粒子的运动特性，把圆形粒子替换成一张 Logo 图片，并加上旋转。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">核心思路</h3><ol style="margin:0;padding-left:18px;font-size:13.5px;color:inherit"><li style="margin-bottom:7px">用<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">&lt;canvas&gt;</code>绘制多个 Logo 实例。</li><li style="margin-bottom:7px">每个 Logo 有不同直径、位置、移动速度和旋转角。</li><li style="margin-bottom:7px">用<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">requestAnimationFrame</code>跑平滑动画。</li><li>Logo 图加载完再开动画，避免空图。</li></ol></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">关键参数（照录）</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>Logo 地址</dt><dd><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">https://cdn4.winhlb.com/2025/10/01/68dc359deeea1.jpg</code></dd><dt>直径</dt><dd><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">Math.random()*60 + 20</code>，即 20–80px。</dd><dt>数量</dt><dd><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">logoCount = 屏宽×屏高 / 15000</code>，随屏幕大小自适应。</dd><dt>透明度</dt><dd><code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">random*0.5 + 0.3</code>，即 0.3–0.8。</dd></dl></div></div>

> **性能要点**：Logo 数量按屏幕面积算（除以 15000），避免小屏堆太多；窗口 resize 时重算 canvas 尺寸与 Logo 数组；内容卡片用毛玻璃`backdrop-filter: blur`压在背景之上，保证文字可读。

## 02 · 悬浮红心点赞按钮：陌生人也能点（00147）

00147 的硬要求：文字不动、在不影响整体显示的前提下加一个红心点赞按钮，**支持陌生人点赞**（不用登录）。关键是用`localStorage`存状态，既防同一浏览器重复点，又不要求注册。

| 组成 | 做法（照录） |
|---|---|
| **按钮本体** | 页面左下角悬浮`.heart-like`，里面是`<i class="far fa-heart">`+ 一个`.like-count`数字。 |
| **计数来源** | `let currentLikes = parseInt(localStorage.getItem('pageLikes')) \|\| 0`。 |
| **防重复** | 读`localStorage.getItem('hasLiked') === 'true'`；已点过就 toast「您已经点过赞了！」，不再累加。 |
| **点赞动画** | 点中后给按钮加`.liked`，图标换实心`fas fa-heart`，跑`heartBeat 0.6s`心跳关键帧。 |
| **提示** | `.like-toast`显示「感谢您的点赞！」，2 秒后自动消失。 |

> **localStorage 方案的边界（源笔记原话）**
> - 同一浏览器里重复访问不会重复计数；**不同浏览器/设备会各自独立计数**。
> - 要跨设备汇总真实点赞数，必须接后端 API——源笔记留了`sendLikeToServer()`占位，注释里写明应替换为`fetch('/api/like', …)`。

## 03 · 滚动进度条、返回顶部与访问统计（00147）

00147 在同一轮优化里还加了三个「站点级」小部件：顶部滚动进度条、右下角返回顶部、页脚不蒜子 PV/UV 统计。都是纯前端、无后端。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">滚动进度条</h3><p style="font-size:13.5px;color:inherit;line-height:1.72">顶部<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">.progress-container</code>（高 4px、fixed），里面<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">.progress-bar</code>宽度随<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">scrollTop / (scrollHeight - innerHeight)</code>变化，渐变填色。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">返回顶部</h3><p style="font-size:13.5px;color:inherit;line-height:1.72">右下角<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">.back-to-top</code>圆钮，初始<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">opacity:0; visibility:hidden</code>；滚动超过阈值才加<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">.active</code>显现，点了<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">scrollTo(0,0)</code>。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">不蒜子 PV/UV</h3><p style="font-size:13.5px;color:inherit;line-height:1.72">页脚引入<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js</code>（async），用<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12px">busuanzi_container_site_pv / _uv</code>两个容器挂本站总访问量与访客数。</p></div></div>

> **搭配关系**：00147 的主页同时保留了「红心点赞」和「不蒜子访客统计」——前者是交互反馈、后者是站点流量，两者互不依赖，都能纯前端跑。这也是 00148 后来拆子网页时明确要求「保留点赞和访客统计」的原因。

## 04 · 主页太复杂？拆成子网页标题导航（00148）

00148 的转折：用户觉得主页一长页太杂，要求**各板块改成子网页、主页只留标题**。这正是把前面学的「子目录/子网页」用到自己身上。下面是源笔记沉淀下来的主页骨架。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00148 · 主页精简要求（照录）</span><h3>主页只保留入口，内容拆出去</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">位置</th><th>放什么</th></tr></thead><tbody><tr><td><b>顶部</b></td><td>个人头像<b>往左</b>放；头像右侧放「可拨打的电话」与「可一键复制的微信号」。</td></tr><tr><td><b>中间</b></td><td>各板块只留<b>标题（+图标）</b>，点进去才是子网页：健康集团、青海基地介绍、个人介绍、主要采购品类、工作目标、擅长领域、知识库、产品库。</td></tr><tr><td><b>底部正中</b></td><td>放一个 logo，规格<b>285×65 像素</b>；底部背景用<b>黑底</b>。</td></tr><tr><td><b>保留</b></td><td>点赞功能 + 访客统计（即 00147 的红心与不蒜子）。</td></tr></tbody></table></div><p style="margin:0">后续又迭代两轮：要求把「分类」从一排改<b>分两行</b>排布；产品子网页本身再做导航栏——<b>传统渠道、电商渠道 3 区、其他、首页</b>四个入口，每个用<b>下拉列表</b>展开。</p></div></div>

<details><summary>「DOCTYPE 修改」这个文件名到底在说什么<span>命名由来</span></summary><div><p>这份笔记的标题里<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">&lt;!DOCTYPE html&gt; &lt;html lang=</code>并不是在讨论文档类型声明——它只是用户每次提问时把当前主页的 HTML 头两行（<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">&lt;!DOCTYPE html&gt;</code>、<code style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:12.5px">&lt;html lang=&quot;zh-CN&quot;&gt;</code>）原样粘进对话框，文件名就照抄了这两行。真正的内容是主页的一轮轮精修：渐变文字标题、毛玻璃弹窗、拆子网页、加视频。</p></div></details>

## 05 · 在线视频播放器：旋转 90 度与横版适配（00148）

00148 后半段连续追了几次视频需求：先给一个在线视频网址做播放页，再要求「只放一个视频、要简约」，接着要**把播放器转 90 度**、横版视频要完整展现、播放按钮要放在好点的位置。

| 需求迭代 | 做法要点 |
|---|---|
| **在线播放 mp4** | 用`<video controls autoplay>`+`<source src="在线mp4地址" type="video/mp4">`，页面尽量留白、只放播放器。 |
| **播放器转 90 度** | 给播放器容器套 CSS`transform: rotate(90deg)`，并配合调整宽高与定位，让旋转后仍居中、不溢出。 |
| **横版完整展现** | 视频本身是横版，却只显示了一部分——用`object-fit: contain`让横版视频完整装入容器，再把播放/暂停/进度等控制条（插件）放到不遮挡画面、便于点击的位置。 |

> **经验沉淀**：在线视频最容易翻车的是「竖屏手机里横版视频只露一半」——根因是容器是竖的、视频是横的，光旋转不够，必须同时用`object-fit: contain`保证完整画面，再挪控制条位置。
