---
title: "桌面 EXE·小程序转桌面·1024 桌面版开发"
description: "桌面 EXE 开发步骤（PyInstaller/Electron/Tauri/Pygame）、小程序转桌面软件方法、1024 桌面版制作与小程序发布流程。"
pubDatetime: 2026-06-28
category: "建站与技术"
kind: "长文"
tags: ["桌面 EXE", "PyInstaller", "Electron Tauri", "Pygame", "小程序发布"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：01272-2026-06-06 桌面 EXE 开发步骤指南00781-2026-03-22 小程序转桌面软件方法（含本地采购管理系统方案）00957-2026-04-17 1024 桌面版制作指南（含 3×3 无限改版）01316-2026-06-16 小程序发布流程01350-2026-06-28 个人开发微信小程序指南01351-2026-06-28 个人开发小程序指南（与 01350 同题，含 BOM 查询小程序案例）

## 01 · 桌面 EXE 开发九步与技术栈（01272）

无论选哪种技术，做 Windows 桌面 EXE 都走「需求 → 选栈 → 环境 → 编码 → 调试 → 打包 → 安装包 → 签名分发 → 维护」九步。新手推荐 C# WinForms 或 Python+PyInstaller。

| 技术栈 | 打包方式 | 适合场景 |
|---|---|---|
| **C# WinForms/WPF** | VS Release 发布，.NET 5+ 可单文件 | 传统企业软件、工具类。 |
| **C++ Qt** | windeployqt 收依赖 + Inno Setup/NSIS | 工业软件、复杂图形。 |
| **Electron** | `npx electron-builder --win` | 跨平台工具、聊天软件。 |
| **Python+PyQt/Tkinter** | `pyinstaller --onefile --windowed` | 脚本化/内部工具。 |
| **Flutter Desktop** | `flutter build windows` | 移动桌面统一体验。 |
| **Rust+Tauri** | `npm run tauri build` | 小体积高性能新项目。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">关键步骤</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>打包后必测</dt><dd>在<b>没装开发环境的纯净 Windows</b>上跑，查缺 VCRUNTIME140.dll 等运行库。</dd><dt>安装包工具</dt><dd>Inno Setup（免费经典）、NSIS、WiX（MSI 企业）、Advanced Installer（商业）。</dd><dt>代码签名</dt><dd>买 DigiCert/Sectigo 证书签名，避免杀毒误报与「未知发布者」警告。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">新手最快路线</h3><p style="font-size:13.5px;color:inherit;margin-bottom:0">装 VS2022 Community 选「.NET 桌面开发」→ 新建 WinForms 项目 → 拖拽控件双击写事件 → 切 Release 生成解决方案 → 到 bin\Release 把 exe 连同同目录 dll/config 一起压缩发给朋友即可。</p></div></div>

## 02 · 小程序转桌面软件的四条路径（00781）

微信小程序依赖微信环境，无法直接转 .exe；按「你手上的是什么」分情况选方案。最通用的是 Electron 复用前端代码，要小体积选 Tauri，不想写代码用 PWA 或 Nativefier 一行命令。

| 方案 | 做法与取舍 |
|---|---|
| **Electron（推荐）** | wxml→html、wxss→css、js 逻辑微调后放进 Electron 项目，配窗口图标，electron-builder 打包。1 小时能跑起来桌面窗口。 |
| **Tauri** | 系统 WebView 打包，体积约为 Electron 的 1/10（<10MB），需 Rust 环境。 |
| **Uni-app 转换** | 原小程序若用 uni-app 开发，manifest.json 配桌面端后 HBuilderX 直接编译 Win/macOS 安装包。 |
| **PWA / Nativefier** | HTTPS+ServiceWorker 的网页用 Chrome/Edge「安装」到桌面；或`npm i -g nativefier && nativefier "网址"`一行打包。无法深调系统底层。 |
| **Python 脚本** | PyWebView/Eel 让 Python 当后端浏览器当前端，再 PyInstaller 打单 exe；或 Tkinter/PyQt5 重写界面。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00781 · 2026-03-22</span><h3>案例：本地采购管理系统（Python+SQLite+PyQt5）</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>技术栈</dt><dd>Python 3.9+ / SQLite（文件即库，免服务器）/ PyQt5 / PyInstaller。</dd><dt>核心模块</dt><dd>供应商、商品、采购订单（选供应商+商品+数量，自动算总价）、入库更新库存、库存查询。</dd><dt>建表</dt><dd>suppliers / products（含 stock）/ purchase_orders（order_no 唯一、status pending·completed）/ order_items（order_id+product_id+quantity+price+amount）四张表。</dd><dt>界面</dt><dd>QTabWidget 三标签页，每模块一个 QWidget 子类：QTableView + QStandardItemModel 显示，QFormLayout 录入，增删改刷新按钮绑信号。</dd><dt>打包</dt><dd><code>pyinstaller --onefile --windowed --name 采购管理系统 main.py</code>，产物在 dist/。</dd></dl></div></div>

## 03 · 1024 桌面版：Pygame 游戏与 EXE 打包（00957）

小白也能跟着做：Python+Pygame 写 4×4 合成游戏（方向键移动、相同数合并、合成 1024 胜利、R 重开），再 PyInstaller 打 EXE。后续应要求改成**3×3 九宫格、不设数字上限**。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">开发四步</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>装环境</dt><dd>python.org 装 Python 3.8+（勾 Add to PATH），<code>pip install pygame pyinstaller</code>。</dd><dt>写代码</dt><dd>桌面建 1024_Game 文件夹，新建 game.py 粘贴完整代码。</dd><dt>运行</dt><dd><code>python game.py</code>，方向键移动，R 重开。</dd><dt>打包</dt><dd><code>pyinstaller --onefile --windowed --name &quot;1024&quot; game.py</code>，dist/ 里出 exe。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:12px">3×3 无限版改动</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>网格</dt><dd>SIZE=3，TILE_SIZE 120。</dd><dt>胜利</dt><dd>移除「合成 1024 胜利」逻辑，可无限合成。</dd><dt>颜色</dt><dd>预定义到 65536，超大数用 log2 对数渐变；数字超 1000/10000 自动缩字号。</dd><dt>主循环</dt><dd>方向键触发 move_left/right/up/down，有移动才 add_new_tile，填满即游戏结束。</dd></dl></div></div>

> **常见问题**
> - 「python 不是内部命令」= 装时没勾 Add to PATH，重装勾选。
> - 打包后 EXE 报 Failed to execute script：去掉 --windowed 重打看错误；本代码只用默认字体一般不缺资源。
> - 360 等杀毒误报是 PyInstaller 常见现象，加信任即可。

## 04 · 小程序发布流程与个人主体限制（01316 / 01350 / 01351）

01316 讲完整发布四步，01350/01351 同题补充个人开发者的关键限制。核心链路：**注册认证 → 开发测试 → 提交审核 → 发布上线**，ICP 备案与资质最耗时要提前办。

| 阶段 | 要点 |
|---|---|
| **注册认证** | mp.weixin.qq.com 选「小程序」注册；个人身份证即可，企业营业执照+法人身份证，企业认证 300 元/年（个人免费）；拿 AppID；上线必须 ICP 备案（5-20 工作日）。 |
| **开发测试** | 装微信开发者工具，用 AppID 建项目；后台配 HTTPS 合法域名白名单；预览扫码真机调试不同机型；上传成开发版本→设体验版。 |
| **提交审核** | 填功能描述、测试账号、功能截图；审核 1-7 工作日，特殊类目更久；驳回按原因改完重提。 |
| **发布上线** | 全量发布或分阶段灰度；发布后用户可搜索到。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01351 · 2026-06-28</span><h3>个人主体的硬限制（照录）</h3></div><div style="padding:14px 16px"><div style="overflow-x:auto;margin:16px 0;margin-bottom:0"><table><thead><tr><th style="width:150px">限制项</th><th>取值/说明</th></tr></thead><tbody><tr><td>微信支付</td><td>个人主体无法开通，盈利主要靠广告。</td></tr><tr><td>服务类目</td><td>仅工具、资讯等基础类目；电商、社交需企业资质。</td></tr><tr><td>命名</td><td>不能用「官方」「旗舰店」「企业」「公司」等词。</td></tr><tr><td>主包体积</td><td>不超过 2MB。</td></tr><tr><td>页面层级</td><td>跳转深度不超过 10 层。</td></tr><tr><td>本地存储</td><td>上限 10MB。</td></tr><tr><td>合规</td><td>首启弹《隐私保护指引》；UGC 走官方安全接口；请求全 HTTPS+白名单；禁诱导分享、强制授权。</td></tr></tbody></table></div></div></div>

案例「企业产品 BOM 查询」：核心是父子型一张表（父件编码/子件编码/用量）做正查（向下展开）反查（向上追溯）；因个人主体不能含「企业」字样且无支付，建议注册**个体工商户**（一张执照，成本低，功能介于个人与企业之间）。
