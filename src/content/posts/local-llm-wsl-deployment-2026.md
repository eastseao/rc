---
title: "本地大模型部署·WSL·LM Studio"
description: "Qwen2.5-7B 本地部署 API 四方案、LM Studio 2026 使用教程与开 API、WSL 安装应用指南与 WSL Ubuntu 用途。"
pubDatetime: 2026-04-24
category: "AI与Agent"
kind: "长文"
tags: ["Qwen2.5-7B", "OpenAI 兼容 API", "LM Studio", "WSL2", "本地部署"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：00801-2026-03-25 Qwen2.5 7B本地部署API方案01018-2026-04-24 LM Studio使用教程202600893-2026-04-10 WSL安装应用指南00954-2026-04-17 WSL Ubuntu用途指南

## 01 · Qwen2.5-7B 封装成 API 的四种方案（00801）

Qwen2.5-7B 支持多种方式封装成 API，且几乎所有主流方案都提供**与 OpenAI API 完全兼容**的接口——只需换掉代码里的`base_url`和`api_key`，就能像调 GPT 一样调本地模型。

<table><thead><tr><th style="width:130px">方案</th><th style="width:170px">定位</th><th>启动命令与默认端口</th></tr></thead><tbody><tr><td><b>vLLM</b></td><td>高性能生产环境首选；PagedAttention，吞吐极高，适合高并发</td><td><pre style="margin-bottom:0">vllm serve Qwen/Qwen2.5-7B-Instruct --port 8000</pre>默认监听 8000</td></tr><tr><td><b>TGI</b></td><td>Hugging Face 官方出品；支持张量并行、流式输出、speculative decoding</td><td><pre style="margin-bottom:0">docker run --gpus all -p 8080:80 ghcr.io/huggingface/text-generation-inference:2.0 --model-id Qwen/Qwen2.5-7B-Instruct</pre>映射 8080</td></tr><tr><td><b>Ollama</b></td><td>零成本上手、最适合新手；自动处理量化与显存分配</td><td><pre style="margin-bottom:0">ollama run qwen2.5:7b</pre>自动下载并启动，默认 11434</td></tr><tr><td><b>OpenLLM</b></td><td>Python 开发者最爱；pip 安装，与 Python 生态结合紧</td><td><pre style="margin-bottom:0">pip install openllm openllm serve qwen2.5:7b</pre>默认 3000</td></tr></tbody></table>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>00801 · 2026-03-25</span><h3>客户端调用：换端口即可通用</h3></div><div style="padding:14px 16px"><p style="margin-bottom:10px">以 vLLM 为例（Ollama 改 11434、TGI 改 8080）：</p><pre>from openai import OpenAI client = OpenAI( base_url=&quot;http://localhost:8000/v1&quot;, # 替换成你的实际端口 api_key=&quot;EMPTY&quot; # 本地服务不需要真实 Key ) response = client.chat.completions.create( model=&quot;Qwen/Qwen2.5-7B-Instruct&quot;, messages=[{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;你好，请介绍一下自己&quot;}], temperature=0.7, max_tokens=512 ) print(response.choices[0].message.content)</pre><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>硬件提醒</b>：Qwen2.5-7B 在 FP16 精度下约需<b>16GB</b>显存；显存不足时用 vLLM 或 Ollama 加载<b>GPTQ/AWQ 量化版</b>，显存可降到<b>6-8GB</b>。</div></div></div>

## 02 · LM Studio：图形界面里取 API（01018）

本地已装好 LM Studio 与`Qwen2.5-7B-Instruct`，怎么拿到 API？LM Studio 的 API 遵循 OpenAI 规范，直接用 OpenAI 客户端 SDK 即可。前提：先在**「设置 → 开发者模式」**里把它打开，API 配置项才会出现。

<table><thead><tr><th style="width:150px">步骤</th><th>操作</th></tr></thead><tbody><tr><td><b>① 启动本地服务器</b></td><td><b>图形界面</b>：左侧「开发者 (Developer)」标签 →「模型服务 (Model Serving)」选已加载模型 →「启动服务器 (Start Server)」；需远程访问可在设置里改为<code>0.0.0.0</code>。<br></td></tr><tr><td><b>② 验证服务</b></td><td>启动成功默认地址<code>http://localhost:1234</code>，验证：<pre style="margin:8px 0 0">curl http://localhost:1234/v1/models</pre>返回模型列表即就绪。</td></tr><tr><td><b>③ API 验证（可选）</b></td><td>默认<b>不需要认证</b>（本地开发用）；需要更安全可在开发者页生成令牌，请求头加<code>Authorization: Bearer $LM_API_TOKEN</code>。</td></tr></tbody></table>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>01018 · 2026-04-24</span><h3>代码调用：只改 base_url 与 api_key</h3></div><div style="padding:14px 16px"><pre>from openai import OpenAI client = OpenAI( base_url=&quot;http://localhost:1234/v1&quot;, # 默认本地地址 api_key=&quot;lm-studio&quot; # 内容随意，仅占位 ) response = client.chat.completions.create( model=&quot;local-model&quot;, # 名字被忽略，始终用当前加载的模型 messages=[ {&quot;role&quot;: &quot;system&quot;, &quot;content&quot;: &quot;You are a helpful assistant.&quot;}, {&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Hello!&quot;} ], temperature=0.7, ) print(response.choices[0].message.content)</pre><p style="margin-bottom:10px">等价的 cURL 调用：</p><pre>curl http://localhost:1234/v1/chat/completions \ -H &quot;Content-Type: application/json&quot; \ -d '{ &quot;model&quot;: &quot;local-model&quot;, &quot;messages&quot;: [ {&quot;role&quot;: &quot;system&quot;, &quot;content&quot;: &quot;You are a helpful assistant.&quot;}, {&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Hello!&quot;} ] }'</pre><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>重要注意事项</h5><ul><li>确认<code>base_url</code>端口（默认 1234）与开发者界面显示一致。</li><li>启动 API 前先在「开发者」或「聊天」界面加载好模型，或确保自动加载开启。</li><li>服务器一旦启动，模型持续占用内存/显存，用完记得关闭释放资源。</li><li>进阶玩法：多请求并发批处理、流式输出逐字显示、<code>tools</code>参数做 Function Calling、新版有状态端点<code>/api/v1/chat</code>免传完整历史。</li></ul></div></div></div>

## 03 · 在 WSL 里安装应用（00893）

核心理念：把 WSL 里的 Linux 当成一台独立电脑，用 Linux 的方式在终端里装软件。下面是三种主要安装法，外加「打不开 WSL」的排查流程。

| 安装方式 | 命令 / 操作 | 适用场景 |
|---|---|---|
| **包管理器（推荐）** | `sudo apt update`先刷新源；再`sudo apt install git`/`curl`/`build-essential`。Fedora 用`dnf`，Arch 用`pacman`。 | 90% 的常规软件，最简单省心 |
| **Linux 图形应用（WSLg）** | WSL2 + Win10 19044+/Win11 已内置支持，照常`sudo apt install firefox`/`gnome-text-editor`/`gimp`，终端输应用名即以窗口打开。 | 需要 GUI 的 Linux 程序 |
| **手动装 .deb** | Windows 下载的包在`/mnt/c/Users/你的用户名/Downloads/`；建议复制进 WSL 文件系统再装：`sudo dpkg -i 包名.deb`；缺依赖跑`sudo apt install -f`。 | 官方源没有或需特定版本 |
| **编译源码** | `./configure`、`make`、`sudo make install` | 开发者定制或极致性能 |
| **跨语言工具链** | `npm`/`pip`/`go get` | Node.js / Python / Go 生态 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">apt 其他常用操作</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>卸载</dt><dd><code>sudo apt remove 软件名</code>；连同配置<code>sudo apt purge 软件名</code>。</dd><dt>搜索</dt><dd><code>apt search 关键词</code>；已装列表<code>apt list --installed</code>。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">日常技巧</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>更新 WSL</dt><dd>管理员 PowerShell 跑<code>wsl --update</code>。</dd><dt>换源提速</dt><dd>apt 慢或超时就换清华/中科大/阿里镜像源。</dd><dt>访问 Windows</dt><dd>经<code>/mnt/c/</code>访问 C 盘；项目文件放 Ubuntu 文件系统里读写快得多。</dd></dl></div></div>

<details style="margin-top:16px"><summary>打不开 WSL？从错误代码开始的分步排查（00893）<span>六步</span></summary><div><p>先记下弹窗里的错误代码（例如<code>0x8007019e</code>），再按顺序尝试：</p><ul><li><b>① 系统与功能</b>：<code>winver</code>确认 WSL2 需 Win10 19044+ 或 Win11；「Windows 功能」里勾选「适用于 Linux 的 Windows 子系统」与「虚拟机平台」，未开则重启。</li><li><b>② 重启服务与内核</b>：<code>wsl --shutdown</code>；到微软站下载「适用于 x64 计算机的 WSL2 Linux 内核更新包」。</li><li><b>③ 看发行版状态</b>：<code>wsl -l -v</code>，观察目标发行版 STATE 是否 Running/Stopped。</li><li><b>④ 修复/重置发行版</b>：设置 → 应用 → 已安装的应用 → 找到 Ubuntu →「…」→ 高级选项 → 先「修复」，无效再「重置」（重置会清空该发行版数据）。</li><li><b>⑤ 代理冲突</b>：Clash/v2rayN 可能干扰 WSL2 启动，先完全退出代理再试；必要时在<code>C:\Users\你的用户名\.wslconfig</code>写<code>[wsl2] networkingMode=mirrored</code>，再<code>wsl --shutdown</code>生效。</li><li><b>⑥ 更底层</b>：<code>services.msc</code>重启<code>LxssManager</code>服务；注册表<code>HKCU\Software\Microsoft\Windows\CurrentVersion\Lxss</code>先「导出」备份再删除（高风险），重启后由 WSL 重建。</li></ul><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-top:10px;margin-bottom:0">约 90% 的问题可通过<b>更新系统、开启 Windows 功能、重启服务或升级内核</b>解决。另：强烈推荐<b>WSL 2</b>，可用<code>wsl --set-default-version 2</code>设为默认；报<code>Permission denied</code>就在命令前加<code>sudo</code>。</div></div></details>

## 04 · 装好 WSL Ubuntu，能做什么（00954）

在 PowerShell 里装好 Ubuntu（WSL），等于在电脑里得到一个免费「影子系统」，适合开发、学习、运维与快速体验，且不必担心弄乱 Windows。

| 方向 | 具体能做的事 |
|---|---|
| **软件开发** | 一键装 Python/Node/Ruby/Go + Nginx/Apache，配 VS Code 的 WSL 插件写调代码；GPU 加速装 Anaconda/TensorFlow/PyTorch 做 AI/ML；直接装 Docker（比 Windows 版性能更好）；一次编译跨平台运行。 |
| **学习实验** | 沙盒里练`ls`/`cd`/`grep`/`find`；写 Bash 脚本自动化备份监控；用 apt 亲手装配 Nginx/MySQL/Redis。 |
| **系统运维** | Shell/Python 批量处理文件、管服务；用`curl`/`wget`/`rsync`下载同步；跑`nmap`/`tcpdump`学网络与基础安全测试。 |
| **网络服务** | 本地起 Node/Python Web 服务，Windows 浏览器直接访`localhost`；起 Redis/MySQL 做客户端-服务器联调；用`iptables`学包过滤转发。 |
| **Linux 桌面** | WSL2 里 GIMP、Blender 像原生应用出现在开始菜单；甚至可装 XFCE/GNOME 体验完整桌面。 |
| **自建小服务** | Vaultwarden 私人密码库、Jellyfin/Plex 家庭媒体中心、私人在线笔记、GitLab 私有实例。 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">让体验更好</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.85"><li>首选<b>WSL 2</b>：完整内核、支持 Docker 与 GUI。</li><li>项目文件放 Ubuntu 虚拟文件系统（如<code>~/projects</code>），别放<code>/mnt/c/</code>，读写快非常多。</li><li>VS Code 装 WSL 插件，像本地一样编辑 Ubuntu 里的代码。</li><li>用 Windows Terminal 统一开 PowerShell/CMD/Ubuntu；Windows 访 Ubuntu 服务直接走<code>localhost</code>。</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">了解这些「边界」</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.85"><li>不是裸机 Linux：对硬件要求极高的任务性能不如原生。</li><li>硬件直通受限：无法像完整虚拟机那样独占 USB 加密狗等设备。</li><li>部分需特殊内核模块的系统级服务可能跑不起来。</li></ul></div></div>
