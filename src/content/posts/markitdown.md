---
title: "MarkItDown"
description: "微软开源 MarkItDown 网页版：PDF/Word/PPT/Excel/图片/音频等 10+ 格式一键转 Markdown，纯浏览器本地转换。"
pubDatetime: 2026-09-23
category: "AI与Agent"
kind: "工具"
tags: ["MarkItDown", "转换", "效率", "微软开源"]
---

微软开源项目 · markitdown

## MarkItDown · 文件转 Markdown

基于微软开源项目[MarkItDown](https://github.com/microsoft/markitdown)（v0.1.8）能力的浏览器本地版：上传文件即转换为 Markdown，适合喂给 LLM 与文本分析管线。 所有转换均在浏览器本地完成，文件不会上传到任何服务器。 官方 Python 版支持更完整的音频转写、YouTube 转录与 Azure 云端增强，见页尾说明。

### 1 · 选择文件

支持多选与拖放。可转换：PDF / Word / PowerPoint / Excel / 图片(OCR) / HTML / CSV / JSON / XML / ZIP / EPUB / 纯文本。

点击选择文件，或将文件拖到这里

可一次拖入多个文件，ZIP/EPUB 会递归转换内部内容

PDF

DOCX

PPTX

XLSX/XLS

图片 OCR

HTML

CSV/JSON/XML

ZIP

EPUB

TXT/MD

音频/YouTube/Outlook（受限）

开始转换

清空

### 2 · 转换结果

尚未转换

复制

下载 .md

```

```

### 浏览器限制与官方用法

以下能力受浏览器沙箱限制，本页无法完全复现，建议使用官方 Python 版本：

·

音频转写

（mp3/wav 等语音转文字）与

YouTube 转录

：浏览器端无法对本地音频文件/视频链接直接转写，本页不处理。

·

Outlook .msg

：前端无可用解析库，暂不支持。

·

图片描述（LLM Vision）

：官方版可接 OpenAI 等大模型生成图片描述，浏览器版仅提供本地 OCR 文字识别。

· 本页实现为纯前端近似版，与官方输出可能存在结构差异；高保真转换请用官方 CLI：

pip install 'markitdown[all]'

→

markitdown 文件.pdf -o 输出.md
