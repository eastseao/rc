---
title: "网页布局样式优化与微信不安全提示"
description: "网页布局与样式优化总结、关于我页面响应式调整与微信提示网页不安全的 HTTPS/CNAME 申诉解决方法。"
pubDatetime: 2025-10-23
category: "建站与技术"
kind: "长文"
tags: ["关于我页面", "响应式", "HTTPS", "CNAME", "微信申诉"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00297-2025-10-23 网页布局与样式优化总结00194-2025-10-09 微信提示网页不安全解决方法

## 01 · 「关于我」页面的布局与样式修正（00297）

00297 是一个 Jekyll（layout: page）的关于我页：顶部头像 + 名字简介，下面三张卡片——在职、技能、爱好，底部一句信念。AI 给出的修正集中在**可访问性、响应式、视觉层次与代码结构**五方面。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00297 · 2025-10-23</span><h3>五项主要修正</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:150px">方面</th><th>具体改动</th></tr></thead><tbody><tr><td><b>可访问性</b></td><td>头像补<code>width/height</code>属性、alt 改成「王维的头像」、增强颜色对比度。</td></tr><tr><td><b>布局响应式</b></td><td>改用相对单位 rem；卡片网格<code>repeat(auto-fit,minmax(280px,1fr))</code>；768/480 两档断点下调间距与字号。</td></tr><tr><td><b>视觉增强</b></td><td>每张卡片加 💼🚀❤️ 图标；悬停上浮 + 阴影加深；列表项用主题色圆点。</td></tr><tr><td><b>代码结构</b></td><td>CSS 加注释、媒体查询分断点整理。</td></tr><tr><td><b>内容组织</b></td><td>底部信念单独封装<code>.about-footer</code>加分隔线；行高与间距统一。</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>页面数据（照录）</b>：现居杭州｜40 岁；在职北京同仁堂健康药业（青海）有限公司，包装解决方案专员；技能含 PS/Illustrator、电商运营、电视购物策划；爱好阅读写作、旅行摄影、书法、音乐、烹饪、新技术学习。</div></div></div>

## 02 · 微信「无法确认网页安全性」的成因（00194）

在微信里打开`http://gervas.wang`出现「无法确认该网页的安全性，请谨慎访问。」——这是微信严格的网址安全检测触发的，笔记列了五个成因。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00194 · 2025-10-09</span><h3>五个主要原因</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:160px">原因</th><th>说明</th></tr></thead><tbody><tr><td><b>未用 HTTPS（最可能）</b></td><td>网站是<code>http://</code>；微信倾向信任 HTTPS，对纯 HTTP、新域名默认判「不安全」。</td></tr><tr><td><b>域名信誉不足</b></td><td><code>.wang</code>是较新顶级域，不如 .com/.cn/.net 常见，安全库还没建立信任数据。</td></tr><tr><td><b>未备案 / 未被收录</b></td><td>服务器在国内必须 ICP 备案；微信爬虫还没抓取分析你的内容。</td></tr><tr><td><b>内容触发规则</b></td><td>敏感话题、大量可疑外链、或结构像钓鱼站。</td></tr><tr><td><b>被用户举报</b></td><td>曾被访问者通过投诉入口举报，网址进待审核列表。</td></tr></tbody></table></div></div></div>

## 03 · 把网站变成 https://gervas.wang（00194）

GitHub Pages + 腾讯云买域名，要让它走 HTTPS 自定义域名，笔记给了四步流程。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00194 · 2025-10-09</span><h3>四步走</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0"><table><thead><tr><th style="width:160px">步骤</th><th>操作</th></tr></thead><tbody><tr><td><b>① GitHub 设域名</b></td><td>仓库 Settings → Pages，Custom domain 填<code>gervas.wang</code>，勾选<b>Enforce HTTPS</b>。</td></tr><tr><td><b>② 腾讯云 DNS</b></td><td>解析加两条 CNAME：<code>www</code>与<code>@</code>都指向<code>你的用户名.github.io</code>（TTL 600，不带 http:// 或尾斜杠）。</td></tr><tr><td><b>③ 建 CNAME 文件</b></td><td>仓库根目录建无扩展名文件<code>CNAME</code>，内容一行<code>gervas.wang</code>。</td></tr><tr><td><b>④ 等生效</b></td><td>DNS 通常 10 分钟~2 小时、最多 24 小时；GitHub 验证与签发证书可能再等几小时。</td></tr></tbody></table></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>验证与常见问题</h5><ul><li>验证：<code>nslookup gervas.wang</code>或 dnschecker.org；回 Settings→Pages 确认域名与 Enforce HTTPS 绿勾。</li><li>HTTPS 选项不可用：DNS 未传播完或 GitHub 未检测到，等 2-24 小时；可先取消自定义域名、等几分钟再重设。</li><li>访问 GitHub 404：检查 CNAME 文件内容正确、Pages 源分支正确。</li></ul></div></div></div>

## 04 · 仍报警告：申诉与加速（00194）

配好 HTTPS 后微信仍提示，最有效是走微信官方申诉，配合 QQ 浏览器安全检测平台，并耐心等审核。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00194 · 2025-10-09</span><h3>两条申诉通道</h3></div><div style="padding:14px 16px"><div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>微信内申诉</dt><dd>发现 → 搜一搜 搜<code>https://gervas.wang</code>→ 进网站 → 右上角「···」→ 举报 → 页面内容 → 网页可能存在问题 →<b>申请恢复访问</b>。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>QQ 安全检测</dt><dd>访问<code>http://urlsec.qq.com/</code>输入网址查检测结果，按提示整改后重检；另用<code>ssllabs.com/ssltest</code>查证书与混合内容。</dd></dl></div></div><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:14px"><h5>时间与技巧</h5><ul><li>微信审核通常<b>3-7 个工作日</b>；网站信誉建立需几周到几个月。</li><li>加速：完善「关于我」与联系方式、保持更新、多触发微信爬虫（聊天/朋友圈/文件助手发链接）。</li><li>不要重复频繁申诉；保存申诉凭证；被拒后补个人介绍、等两周再申。</li></ul></div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00194 · 2025-10-09</span><h3>200 字以内申诉文案（照录）</h3></div><div style="padding:14px 16px"><p style="font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13px;background:#f8fafc;border-radius:6px;padding:14px 16px;line-height:1.8">申诉标题：个人博客安全申诉 - https://gervas.wang<br></p><p style="font-size:13.5px;color:inherit;margin-top:12px">约 150 字，含网站性质、安全措施、申诉理由、联系方式四块。</p></div></div>
