# 视频下载器 · LinkGrab（本地工具）

粘贴一个链接 → 自动解析 → 选择清晰度 → 默认下载 MP4。
引擎：[yt-dlp](https://github.com/yt-dlp/yt-dlp) + FFmpeg；纯 Python 标准库后端，零 Web 框架。

> ⚠️ **GitHub Pages 上的在线页只是界面展示**，解析与下载必须在本机跑 `server.py`。
> 打开 `https://gervas.wang/tools/video-downloader/` 会看到引导，按下面三步即可在本机使用。

## 本地使用

1. 已装 Python 3.8+；双击 `install.bat` 安装依赖（`pip install -U yt-dlp`），并确保系统装有 FFmpeg（未装则 MP3/合并不可用）。
2. 双击 `start.bat` 启动服务。
3. 浏览器访问 **http://127.0.0.1:8765**，粘贴链接 → 解析 → 选清晰度 → 下载。文件落在本目录 `downloads/`。

## 目录

```
tools/video-downloader/
├── index.html     # 子页（在线展示 + 本地运行时的操作界面）
├── server.py      # 后端：HTTP API + 调用 yt-dlp
├── start.bat      # 一键启动
├── install.bat    # 一键装依赖
├── downloads/     # 下载输出目录（自动生成）
└── README.md
```

## 支持

抖音 / 哔哩哔哩 / YouTube / TikTok / Instagram / X(Twitter) / 微博 / 小红书 / 快手 / Reddit 等 yt-dlp 支持的数百个站点。需登录的站点可把浏览器导出的 `cookies.txt` 放在本目录自动加载。

## 版权

仅供下载你有权获取的公开媒体内容，遵守平台条款与版权法规，勿用于绕过 DRM。
