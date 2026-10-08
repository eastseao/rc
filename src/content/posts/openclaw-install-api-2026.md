---
title: "OpenClaw 桌面/Ubuntu 安装与 API 设置"
description: "OpenClaw 桌面端一键脚本、四款桌面应用、Ubuntu 全流程安装与 API Key/Qwen2.5 配置。"
pubDatetime: 2026-06-11
category: "AI与Agent"
kind: "手册"
tags: ["OpenClaw", "一键安装脚本", "Ubuntu", "API Key", "Qwen2.5"]
---

> **本文合并自以下笔记**（序号即原笔记编号，括号内为笔记日期）：01040-2026-04-27 OpenClaw Desktop安装指南01042-2026-04-27 OpenClaw桌面应用咨询01297-2026-06-11 Ubuntu登录后安装OpenClaw01298-2026-06-11 OpenClaw API设置指南01063-2026-04-28 OpenClaw调用Qwen2.5应用场景

## 01 · Windows 一键脚本与桌面客户端（01040 / 01042）

安装 OpenClaw 主要有两条官方途径：**一键安装脚本**（官方推荐，一行命令自动配置环境）和**官方/第三方桌面客户端**（图形界面、解压即用）。开始前先备份重要数据，并**暂时关闭**360、腾讯电脑管家、火绒等第三方杀毒软件及 Windows Defender 实时防护，避免误报导致安装失败。

| 项 | 要求 |
|---|---|
| **操作系统** | Windows 10/11（建议 64 位专业版/企业版）、macOS 12+，或主流 Linux 发行版（如 Ubuntu 22.04+）。 |
| **内存空间** | 建议 4GB 以上内存，以及至少 4GB 的空闲硬盘空间。 |
| **安装时长** | 脚本全自动完成（含检测安装 Node.js 等环境），全程约 3-5 分钟。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方法一 · 官方推荐</span><h3>一键安装脚本</h3></div><div style="padding:14px 16px"><p>Windows：在开始菜单搜索<b>PowerShell</b>，右键选择「以管理员身份运行」。国内用户推荐镜像加速：</p><pre>iwr -useb https://open-claw.org.cn/install-cn.ps1 | iex</pre><p>国际用户则用官方源：</p><pre>iwr -useb https://openclaw.ai/install.ps1 | iex</pre><p>macOS / Linux：打开终端，国内用户用镜像加速：</p><pre>curl -fsSL https://open-claw.org.cn/install-cn.sh | bash</pre><p>国际用户：</p><pre>curl -fsSL https://openclaw.ai/install.sh | bash</pre><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>初始化</dt><dd>脚本完成后自动进入<code>onboard</code>交互式配置向导；意外中断后可随时运行<code>openclaw onboard</code>重新进入。</dd><dt>验证安装</dt><dd>终端输入<code>openclaw --version</code>并回车，能正确显示版本号即核心程序安装成功。</dd></dl></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方法二 · Windows</span><h3>OpenClaw Desktop 桌面客户端</h3></div><div style="padding:14px 16px"><ol style="margin:0 0 14px;padding-left:20px;font-size:13.5px;color:inherit;line-height:1.8"><li>从 GitHub Releases 页面或网盘链接下载对应系统的安装包，<b>务必先解压</b>到纯英文路径（如<code>D:\OpenClaw</code>），切勿在压缩包内直接运行。</li><li>双击<code>Openclaw Windows 一键启动.exe</code>；出现 Windows 安全提示时，点「更多信息」→「仍要运行」。</li><li>图形化安装界面中，安装路径<b>务必使用纯英文路径</b>，不能包含中文、空格或特殊符号。</li><li>勾选同意用户协议，点「开始安装」，等待自动部署完成（约 3-5 分钟）。</li><li>首次运行初始化，当主界面右上角显示「<b>Gateway 在线</b>」时，即表示部署成功。</li></ol><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0"><h5>常见问题排查</h5><ul><li><b>安装中断/失败</b>：检查是否已关闭所有杀毒软件，安装路径无中文字符/空格，建议以管理员身份运行。</li><li><b>网络连接问题</b>：优先使用国内镜像加速命令。</li><li><b>提示缺少 Node.js</b>：一键脚本通常自动安装，未成功可手动从 Node.js 官网下载安装 LTS 版本。</li><li><b>Windows 安全中心拦截</b>：出现「Windows 已保护你的电脑」弹窗时，点「更多信息」→「仍要运行」即可。</li></ul></div></div></div>

笔记 01042 还梳理了市面上几款把命令行变成图形界面的 Windows 桌面应用，供选型参考：

| 应用 | 定位 | 核心特点与体验 |
|---|---|---|
| **ClawX** | 新手开箱即用 | 内置运行时，命令行转直观 UI，支持多渠道管理、定时任务和技能扩展；原生支持中文、社区活跃。 |
| **OpenClaw Windows Node** | 系统级重度用户 | 微软技术专家主导，专为 Win10/11 打造，系统托盘常驻，可深度操控文件、进程等系统底层。 |
| **OpenClaw Desktop（小龙虾）** | 专业控制台 | 开源免费、功能全面，可视化管理面板，支持远程连接管理远端实例，适配 Windows/macOS/Linux。 |
| **EasyClaw AI** | 安全沙箱 | 零配置且带安全沙箱环境，为 AI 智能体提供隔离运行环境，适合对安全性要求较高的开发者与专业用户。 |

## 02 · Ubuntu 命令行：从登录到初始化（01297）

在 TTY 命令行模式下看到`HomePC login:`很正常——系统在等待你手动登录后才能继续安装。OpenClaw 强烈依赖 Node.js 环境，需要先更新系统并装好 Node.js。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>第一步</span><h3>登录 Ubuntu 系统</h3></div><div style="padding:14px 16px"><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>输入用户名</dt><dd>在<code>login:</code>后输入用户名，按<code>Enter</code>。</dd><dt>输入密码</dt><dd>出现<code>Password:</code>提示后输入用户密码（屏幕上<b>不会显示</b>，属正常），回车即登录，看到类似<code>username@HomePC:~$</code>的提示符。</dd></dl><p style="font-size:13.5px;color:inherit;margin-top:10px">习惯图形化界面的话，可试按<code>Ctrl + Alt + F1</code>或<code>Ctrl + Alt + F7</code>切换回桌面环境。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>第二步</span><h3>准备环境：更新系统并安装 Node.js 22.x</h3></div><div style="padding:14px 16px"><p>OpenClaw 需要 Node.js 22.x 或更高版本。先更新软件源：</p><pre>sudo apt update</pre><p>添加 NodeSource 官方仓库（自动配置 Node.js 22.x 安装源）：</p><pre>curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -</pre><p>安装 Node.js：</p><pre>sudo apt install -y nodejs</pre><p>验证是否安装成功，正确显示版本号（如<code>v22.x.x</code>）即装好：</p><pre>node --version</pre><p>（可选但推荐）安装基础开发工具包，确保编译过程顺利：</p><pre>sudo apt install -y build-essential</pre></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>第三、四步</span><h3>安装 OpenClaw 并初始化</h3></div><div style="padding:14px 16px"><p>优先用官方安装脚本，它能自动处理大部分配置：</p><pre>curl -fsSL https://openclaw.ai/install.sh | bash</pre><p>验证安装：</p><pre>openclaw --version</pre><p>初始化向导自动启动，也可手动运行（首次安装直接一路回车选默认<code>QuickStart</code>最顺畅）：</p><pre>openclaw onboard --install-daemon</pre><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>AI 提供商</dt><dd>快速上手可优先选<b>Qwen</b>（通义千问），对初次体验提供免费额度，熟练后再切换其他服务商。</dd><dt>模型选择</dt><dd>保持默认即可。</dd><dt>聊天渠道</dt><dd>初始化阶段可直接「跳过」，不影响核心功能。</dd><dt>技能和钩子</dt><dd>先保持默认或跳过，后续有需要再详细配置。</dd></dl></div></div>

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:14px"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">通过 Web 界面使用（推荐）</h3><p style="font-size:13.5px;color:inherit;margin-bottom:8px">浏览器访问<code>http://127.0.0.1:18789/</code>进入 Web 管理界面；提示配对时，终端运行<code>openclaw dashboard</code>，把输出的带令牌完整链接复制到浏览器打开。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">通过终端界面使用</h3><pre style="margin-bottom:0">openclaw tui</pre></div></div>

> **Ubuntu 常见问题与排查**
> - **Command 'openclaw' not found**：重启终端，或重新运行安装脚本。
> - **端口占用**：Web 界面无法访问时检查端口，`sudo lsof -i :18789`。
> - **Token 不匹配**：重新运行`openclaw dashboard`，把输出完整链接复制到浏览器。
> - **AI 认证失效**：第二天重启可能需重新认证，如用 Qwen 运行`openclaw models auth login --provider qwen-portal`。
> - **Qwen 登录问题**：默认`qwen-portal`通常指向国际版，**可能无法用支付宝或国内手机号登录**，需用 Google 或 GitHub 账号。
> - **Permission denied**：命令前加`sudo`重试。
> - **服务不自启动**：启用 linger 服务`sudo loginctl enable-linger $(whoami)`。
> - **Gateway closed 报错**：在`openclaw`目录下运行`npm run gateway`重启网关。

## 03 · API 的三种设置方式（01298）

配置大模型 API 是使用 OpenClaw 的关键一步——OpenClaw 本身并非 AI 模型，需要接入外部大模型服务（它的「大脑」）才能理解并执行指令。设置 API 主要有三种途径。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(3,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">① 图形界面 GUI</h3><p style="font-size:13px;color:inherit">最直观，适合桌面客户端（尤其 Windows/macOS）。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">② 命令行/环境变量</h3><p style="font-size:13px;color:inherit">适合服务器部署或技术用户，灵活度高。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">③ 配置文件编辑</h3><p style="font-size:13px;color:inherit">适合批量或精准配置，改<code>openclaw.json</code>。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方法一</span><h3>图形界面（GUI）设置 · 以阿里云百炼为例</h3></div><div style="padding:14px 16px"><ol style="margin:0 0 14px;padding-left:20px;font-size:13.5px;color:inherit;line-height:1.8"><li>主界面<b>右上角</b>点「设置」。</li><li>左侧菜单栏选「模型配置」板块。</li><li>右侧模型提供商列表中点需要的服务商（如「阿里云百炼」）。</li><li>把从服务商获取的<code>API Key</code>（通常<code>sk-</code>开头）粘贴到对应输入框。</li><li>点「测试」检查连接是否成功，通过后点右上角「保存全部配置」。</li><li>回聊天页面，在模型下拉列表选刚配置好的模型即可对话。</li></ol></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方法二</span><h3>命令行 / 环境变量设置</h3></div><div style="padding:14px 16px"><p>用向导配置（<code>configure</code>与<code>onboard</code>等效）：</p><pre>openclaw onboard</pre><p>常驻运行的服务器场景推荐环境变量，OpenClaw 检测到后会自动启用对应提供商：</p><pre># 例如，为 NVIDIA 设置 API 密钥 export NVIDIA_API_KEY=&quot;nvapi-...&quot;</pre><div style="border:1px solid #fcd9a8;background:#fdf3e3;border-radius:8px;padding:12px 16px;margin:14px 0;margin-bottom:0"><b>环境变量存放位置</b>：临时运行直接在终端<code>export</code>即可；守护进程（如 systemd、launchd）建议写入<code>~/.openclaw/.env</code>，守护进程才能读到。</div></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>方法三</span><h3>配置文件编辑 openclaw.json</h3></div><div style="padding:14px 16px"><p>核心配置文件<code>openclaw.json</code>默认存放在<code>~/.openclaw/</code>目录下，替换<code>apiKey</code>字段即可：</p><pre>{ &quot;env&quot;: { // 如果你想用环境变量，可以把 API Key 写在这里 }, &quot;models&quot;: { &quot;providers&quot;: { &quot;siliconflow&quot;: { &quot;baseUrl&quot;: &quot;https://api.siliconflow.cn/v1&quot;, &quot;apiKey&quot;: &quot;你的_API_密钥&quot;, // 将你的 API 密钥粘贴到这里 &quot;api&quot;: &quot;openai-completions&quot; } } } }</pre></div></div>

| 关键命令 / 路径 | 作用 |
|---|---|
| `~/.openclaw/openclaw.json` | 核心配置文件。 |
| `openclaw doctor` | 诊断命令。 |
| `openclaw models status` | 测试/查看模型连接状态。 |
| `openclaw config file` | 查看活动配置文件路径。 |
| `openclaw config schema` | 查看配置结构。 |
| Web 控制台`http://127.0.0.1:18789` | 浏览器中进行配置管理和修改。 |
| `/etc/openclaw/conf.d/`下 .env 文件 | 生产环境更规范的密钥管理方式。 |

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>实操示例</span><h3>把 DeepSeek API 配置进 OpenClaw</h3></div><div style="padding:14px 16px"><p>方式一：用官方推荐的一键配置<code>onboard</code>，按提示选择<code>Yes</code>免责声明 →<code>QuickStart</code>模式 → 服务提供商选<code>DeepSeek</code>→ 粘贴 API 密钥 → 默认模型新手推荐<code>deepseek-v4-flash</code>：</p><pre>openclaw onboard --install-daemon</pre><p>方式三：在<code>openclaw.json</code>的<code>models.providers</code>中为 DeepSeek 添加/修改如下配置：</p><pre>{ &quot;models&quot;: { &quot;providers&quot;: { &quot;deepseek&quot;: { &quot;baseUrl&quot;: &quot;https://api.deepseek.com&quot;, &quot;apiKey&quot;: &quot;你的_DeepSeek_API_密钥&quot; } } } }</pre><p>配置完成后验证：聊天界面模型选择框搜索<code>deepseek</code>并选中（如<code>deepseek-v4-flash</code>），或终端运行<code>openclaw models status</code>查看连接状态。</p></div></div>

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">从哪里获取 API Key</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>国内/免费平台</dt><dd>阿里云百炼、MiniMax、Kimi、智谱 AI 等，免费额度多、访问稳定。</dd><dt>国际商业平台</dt><dd>OpenAI（GPT 系列）、Anthropic（Claude 系列），能力强但需海外支付、国内访问可能不稳。</dd><dt>本地模型</dt><dd>Ollama、LM Studio 等，数据隐私好、无需联网，但对显卡有要求。</dd></dl></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">OpenAI 兼容接口关键参数</h3><dl style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><dt>API Key</dt><dd>服务凭证，示例<code>sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</code>。</dd><dt>Base URL</dt><dd>服务地址，如<code>https://api.openai-proxy.com/v1</code>；官方 OpenAI 用户无需填写。</dd><dt>Model Name</dt><dd>实际能用的模型名，如<code>gpt-4-turbo</code>、<code>claude-3-opus-20240229</code>。</dd></dl></div></div>

## 04 · 接入大模型：以 Qwen2.5 7B 为例（01063）

通过 OpenClaw 调用 Qwen2.5 7B Instruct，意味着拥有一位由大语言模型驱动的「智能数字员工」——它能听懂自然语言指令，并实际操作电脑完成任务。两者结合了 Qwen2.5**强大的指令遵循、中文处理与代码数学能力**和 OpenClaw**操作执行工具的能力**。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">办公与开发自动化</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.7"><li><b>会议纪要助手</b>：读取录音/文字记录，生成要点突出的纪要。</li><li><b>智能文档处理</b>：批量处理合同、报告，提取关键信息、格式转换、生成摘要。</li><li><b>邮件与报表</b>：草拟邮件、分析 Excel 数据生成图表、撰写分析报告。</li><li><b>代码生成与调试</b>：自然语言生成代码、审查问题、执行 Git 命令与测试脚本。</li></ul></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:16px;font-weight:700;margin-bottom:10px">数据信息与生活服务</h3><ul style="margin:0;padding-left:18px;font-size:13.5px;color:inherit;line-height:1.7"><li><b>智能爬虫与分析</b>：抓取网页/新闻/商品信息并输出总结报告。</li><li><b>结构化信息抽取</b>：从客户评价、问卷中提取信息输出规整 JSON。</li><li><b>个人知识库问答</b>：基于本地笔记、PDF 问答，保障数据隐私。</li><li><b>信息管家</b>：通过微信、Telegram 下达指令，获取会议提醒、天气、新闻推送；支持 29+ 种语言，可做翻译伙伴。</li></ul></div></div>

> **配置与使用关键提醒**
> - **模型选择**：务必选**通用对话模型**（如`qwen2.5:7b-instruct`），**不要选**专为特定任务的`coder`模型，否则 Agent 在聊天等任务中可能无法正常回复。
> - **上下文窗口**：为最大化 32K 长上下文能力，建议把 OpenClaw 配置文件中的上下文长度设为**32K 或更高**。
> - **善用技能扩展**：官方插件库（如`clawhub.ai`）安装技能包，如`File System`读写本地文件、`Shell Execution`执行终端命令。
> - **API 与本地运行**：可通过阿里云 DashScope 调用 Qwen2.5 的 API，或用 Ollama 等本地运行，本地运行更保护隐私、避免 API 费用。

##### 模型局限性

纯文本模型，不具备视觉能力；7B 规模复杂推理弱于更大版本

它是纯文本模型，**不具备识别和解读图像、视频等视觉信息的能力**；7B 参数规模在极其复杂的推理任务上效果不如 72B 或更大版本；联网搜索等操作通常需要额外工具支持，而非模型本身直接支持。
