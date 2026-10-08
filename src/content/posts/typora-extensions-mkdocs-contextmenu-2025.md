---
title: "Typora 扩展替代·MkDocs·右键新建 Markdown"
description: "Typora 扩展功能与插件替代方案、Pandoc、Windows 安装 MkDocs 教程与右键新建 Markdown 注册表方法。"
pubDatetime: 2026-04-19
category: "建站与技术"
kind: "手册"
tags: ["Typora 扩展", "Pandoc", "MkDocs", "注册表", ".reg"]
---

> **本手册合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00020-2025-07-16 Typora 扩展功能与插件替代方案（含 plugin 文件夹授权排障）00151-2025-10-02 Windows 安装 MkDocs 详细教程00920-2026-04-14 Windows 右键新建 Markdown 文件00960-2026-04-19 右键新建 Markdown 文档教程（Win11）

## 01 · Typora 没有官方插件，四种扩展方式（00020）

Typora**不支持传统意义上的插件系统**（没有 VSCode/Obsidian 那样的官方插件商店），设计上追求简洁专注。所谓「插件」都是曲线救国，按实用度排序如下。

| 方式 | 作用 | 要点 / 必备度 |
|---|---|---|
| **1. Pandoc 集成** | 扩展导出能力（最强大常用） | 解锁导出 Word/.pptx/LaTeX/ePub/ODT/Jupyter Notebook；模板与过滤器可控制页眉页脚、封面、目录、字体、边距，结合 BibTeX 做参考文献。在「文件 > 偏好设置 > 导出」指定 pandoc.exe 路径。⭐⭐⭐⭐⭐ |
| **2. 自定义 CSS 主题** | 改界面与导出外观 | 「偏好设置 > 外观 > 打开主题文件夹」编辑或新建 .css。可改字体字号行高、代码块/表格/引用块样式、加背景图或水印。⭐⭐⭐⭐ |
| **3. 外部脚本自动化** | Python/Shell/AHK 等与 Typora 交互 | 最常见是粘贴图片自动压缩、上传图床、替换 URL（Python + PicGo）；还可批量改链接/Front Matter、智能粘贴、发送到 Todoist/Notion。需一定脚本能力。⭐⭐⭐ |
| **4. 图像设置集成外部命令** | 「偏好设置 > 图像」 | 插入图片时复制到指定文件夹，或调用命令行工具（PicGo CLI）上传并替换链接。比自写脚本简单但功能有限。⭐⭐ |

> **重要提示（照录）**
> - 官方无插件 API，上述都是「曲线救国」；Pandoc、脚本、CSS 都有学习曲线。
> - 外部脚本可能与 Typora 更新冲突，需自行维护；从网上下载的脚本/CSS 要谨慎，注意代码安全。
> - 资源关键词：`typora theme`、`typora uploader`、`typora pandoc template`、「Typora 自动上传图片」。

## 02 · 装了第三方脚本却提示「请给 plugin 文件夹授权」（00020）

这个「plugin 文件夹」不是 Typora 内部目录，而是**你下载/解压的那个脚本工具自己所在的文件夹**。报错含义：脚本需要读写/执行它自己目录的权限，但当前权限不足。解法是给那个具体文件夹授权。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">Windows</h3><ol style="margin:0;padding-left:18px;font-size:13px;color:inherit;line-height:1.8"><li>资源管理器定位该文件夹 → 右键 → 属性。</li><li>「安全」选项卡 → 选中当前登录用户名。</li><li>勾选「修改」或「完全控制」（不足则点「编辑」）。</li><li>应用 → 确定 → 重启 Typora/脚本。</li></ol></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">macOS</h3><ol style="margin:0;padding-left:18px;font-size:13px;color:inherit;line-height:1.8"><li>Finder 定位该文件夹 → 右键「显示简介」。</li><li>「共享与权限」→ 点锁输入密码解锁。</li><li>确保用户名在列表，权限选「读与写」。</li><li>重新锁定 → 重启 Typora/脚本。</li></ol></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">Linux (Ubuntu)</h3><ol style="margin:0;padding-left:18px;font-size:13px;color:inherit;line-height:1.8"><li>属性 → 权限 → 文件夹访问设「创建和删除文件」、文件访问设「读写」。</li><li>勾选「允许作为程序运行」。</li><li>或终端：<code>sudo chmod -R 755 文件夹名/</code>。</li><li>重启 Typora/脚本。</li></ol></div></div>

> **排查顺序（照录）**
> - 先确认改的就是**报错里那个具体文件夹路径**，别误改 Typora 安装目录。
> - 改完**务必重启**Typora 与脚本（含 PicGo）；仍不行可右键「以管理员身份运行 Typora」。
> - 检查脚本自身依赖（Python 库、API key、PicGo 配置）是否漏装。
> - Linux 优先`755`，别轻易`777`（安全风险）；只从可信来源下载脚本。

## 03 · Windows 安装 MkDocs 建站工具（00151）

MkDocs 是基于 Python 的静态文档站生成器。安装走 pip，三步：确认 Python → pip 安装 → 验证。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>安装</span><h3>确认 Python、pip 安装与验证</h3></div><div style="padding:14px 16px"><pre>python --version pip --version pip install mkdocs # 国内加速用清华镜像： pip install mkdocs -i https://pypi.tuna.tsinghua.edu.cn/simple # 验证（显示如 mkdocs, version 1.5.x 即成功）： mkdocs --version</pre><p style="font-size:13px;color:#64748b">未装 Python 到 python.org 下载，安装时<b>务必勾选 Add Python to PATH</b>；权限不足则以管理员身份运行命令行。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>使用</span><h3>新建项目、本地预览、构建发布</h3></div><div style="padding:14px 16px"><pre>mkdocs new my-project cd my-project mkdocs serve # 浏览器打开 http://127.0.0.1:8000，改 .md 自动热重载 mkdocs build # 生成 site/ 静态文件，可部署到任意 Web 服务器</pre><p style="font-size:13px;color:#64748b">项目结构：<code>mkdocs.yml</code>（配置站名称、导航）+<code>docs/</code>（Markdown 文档，初始 index.md 为首页）。</p></div></div>

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">永久镜像源（可选）</h3><p style="font-size:13px;color:inherit;margin-bottom:8px">在<code>C:\Users\你的用户名\</code>下建<code>pip\pip.ini</code>：</p><pre>[global] index-url = https://pypi.tuna.tsinghua.edu.cn/simple trusted-host = pypi.tuna.tsinghua.edu.cn timeout = 120</pre></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">Material 主题与排障</h3><pre>pip install mkdocs-material # mkdocs.yml 里写：theme: material # 8000 端口被占用： mkdocs serve --dev-addr 127.0.0.1:8080</pre><p style="font-size:13px;color:#64748b">命令「未识别」多为环境变量问题：确认装时勾了 Add to PATH，或重开命令行。</p></div></div>

## 04 · 右键「新建」里加 .md：.reg 一键导入（00920）

改注册表前**强烈建议先备份**：`Win+R`→`regedit`→ 文件 → 导出，存一份备份。下面脚本照录自 00920。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方法一</span><h3>新建文本文档 → 粘贴 → 另存为 .reg → 双击导入</h3></div><div style="padding:14px 16px"><pre>Windows Registry Editor Version 5.00 [HKEY_CLASSES_ROOT\.md] @=&quot;MarkdownFile&quot; &quot;Content Type&quot;=&quot;text/markdown&quot; &quot;PerceivedType&quot;=&quot;text&quot; [HKEY_CLASSES_ROOT\.md\ShellNew] &quot;NullFile&quot;=&quot;&quot; [HKEY_CLASSES_ROOT\MarkdownFile] @=&quot;Markdown 文件&quot; [HKEY_CLASSES_ROOT\MarkdownFile\DefaultIcon] @=&quot;\&quot;C:\\Program Files\\Typora\\Typora.exe\&quot;,0&quot; [HKEY_CLASSES_ROOT\MarkdownFile\shell\open\command] @=&quot;\&quot;C:\\Program Files\\Typora\\Typora.exe\&quot; \&quot;%1\&quot;&quot;</pre><ol style="margin:0 0 0 20px;font-size:13.5px;color:inherit;line-height:1.8"><li>另存为时文件名写<code>Add_Markdown_New.reg</code>，保存类型选「所有文件 (*.*)」。</li><li>双击该 .reg → 系统警告点「是」确认导入。</li><li>最后两行是默认打开程序与图标，<b>把 Typora.exe 路径改成你机器的实际路径</b>（VS Code/Notepad++ 同理）；不清楚可先删掉这两行，之后再手动关联。</li></ol></div></div>

<details open><summary>方法二：手动改注册表（了解原理用）<span>00920</span></summary><div><ol><li><code>Win+R</code>→<code>regedit</code>，地址栏输入<code>计算机\HKEY_CLASSES_ROOT\.md</code>。</li><li>.md 不存在则右键 HKEY_CLASSES_ROOT → 新建 → 项，命名<code>.md</code>；右侧默认值设为<code>MarkdownFile</code>。</li><li>在 .md 下新建项<code>ShellNew</code>；选中它 → 右侧新建「字符串值」<code>NullFile</code>，数值留空。</li><li>新建<code>MarkdownFile</code>项，默认值设<code>Markdown 文件</code>；其下依次建<code>shell\open\command</code>。</li><li>command 默认值设<code>&quot;C:\Program Files\Typora\Typora.exe&quot; &quot;%1&quot;</code>（路径用英文双引号）。</li><li>关闭注册表，<b>重启电脑或重启 explorer.exe</b>生效。</li></ol></div></details>

> **常见问题（00920）**
> - 右键里看不到：先重启电脑；再检查`HKEY_CLASSES_ROOT\.md\ShellNew`与`NullFile`是否正确创建。
> - 新建的 .md 打不开：右键 .md → 打开方式 → 选编辑器并勾「始终使用此应用打开 .md 文件」。
> - 想删除菜单项：删`计算机\HKEY_CLASSES_ROOT\.md\ShellNew`，重启即可。

## 05 · Win11 右键新建 Markdown：Typora 自带 + 两套脚本（00960）

已装 Typora 的 Win11 用户，最省事的是用 Typora 自带开关；不生效再走注册表。改注册表前先`regedit`→ 文件 → 导出备份。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">方法一：Typora 自带（最推荐）</h3><ol style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.8"><li>打开 Typora → 文件 → 偏好设置。</li><li>「通用」里点「向 Windows 资源管理器的'新建'菜单项中添加 Markdown 选项」。</li><li>等系统提示成功即可。</li></ol></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:10px">方案A：.md 加「新建」子菜单</h3><ol style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.8"><li>regedit 定位<code>计算机\HKEY_CLASSES_ROOT\.md</code>。</li><li>双击「默认」，数值改<code>Typora.md</code>。</li><li>.md 下新建项<code>ShellNew</code>；其下建字符串值<code>NullFile</code>，留空。</li><li>任务管理器重启「Windows 资源管理器」即生效。</li></ol></div></div>

<details open><summary>方案B：一级菜单直接「用 Typora 新建」+ 两个 .reg 脚本<span>00960</span></summary><div><p style="margin-bottom:10px">方案B 手动步骤：定位<code>计算机\HKEY_CLASSES_ROOT\Directory\Background\shell</code>→ 新建项<code>Typora</code>→ 默认值写<code>新增 Markdown 文件</code>（可自定义）→ 可加字符串值<code>icon</code>指向 Typora.exe → 其下新建项<code>command</code>，默认值写<code>&quot;C:\Program Files\Typora\Typora.exe&quot; &quot;%V&quot;</code>（路径有空格务必加英文双引号，<code>%V</code>代表当前文件夹）→ 重启资源管理器。</p><p style="font-size:13px;font-weight:700;color:#0f172a;margin:8px 0 6px">脚本一：为 .md 加「新建」选项（保存为 add_md_new.reg，管理员运行）</p><pre>Windows Registry Editor Version 5.00 [HKEY_CLASSES_ROOT\.md] @=&quot;Typora.md&quot; [HKEY_CLASSES_ROOT\.md\ShellNew] &quot;NullFile&quot;=&quot;&quot; [HKEY_CLASSES_ROOT\Typora.md] @=&quot;Markdown File&quot;</pre><p style="font-size:13px;font-weight:700;color:#0f172a;margin:8px 0 6px">脚本二：一级菜单「用 Typora 新建」（按实际安装路径改）</p><pre>Windows Registry Editor Version 5.00 [HKEY_CLASSES_ROOT\Directory\Background\shell\Typora] @=&quot;新增 Markdown 文件&quot; &quot;Icon&quot;=&quot;\&quot;C:\\Program Files\\Typora\\Typora.exe\&quot;&quot; [HKEY_CLASSES_ROOT\Directory\Background\shell\Typora\command] @=&quot;\&quot;C:\\Program Files\\Typora\\Typora.exe\&quot; \&quot;%V\&quot;&quot;</pre></div></details>

> **总结优先级（00960）**：已装 Typora 先用**方法一**（一键）；不生效用**方案A**（通用可靠）；不想手动就用**.reg 脚本**（管理员运行）。右键不出现就查注册表路径或重启资源管理器；新建文件双击打不开，就在「打开方式」里选 Typora 并勾「始终使用」。
