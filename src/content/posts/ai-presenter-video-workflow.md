---
title: "照片 + 文案 → 竖版口播视频 · 制作工作流"
description: "从一张照片与配音文案到 55 秒竖版口播视频的完整链路：文案锁定 → MiniMax TTS 配音 → 人像归一化 → 分段数字人生成 → 拼接质检，含实测参数、可复制命令与踩坑修复经验。"
pubDatetime: 2026-10-05
category: "AI与Agent"
kind: "工具"
tags: ["口播视频", "数字人", "工作流", "MiniMax"]
---

AI PRESENTER VIDEO PIPELINE · 2026-09-29

## 一张照片 + 一份配音文案<br>

从科普文案到数字人口播成片的完整制作链路：文案锁定 → TTS 配音 → 人像准备 → 分段生成 → 拼接交付。本文档记录每一步的输入、工具、参数、实测数据与踩坑经验，可直接复现。

54.9s

配音实测时长（MiniMax TTS）

5

流水线阶段

2

生成平台（MiniMax / 豆包）

6

踩坑点与修复经验

### 01工作流总览

整条链路以「定稿音频」为唯一时间基准：口型、字幕、剪辑点全部对齐它。因此音频一旦生成就不回头改文案，改文案等于整条链路返工。

输入

#### 素材

60 秒科普配音文案（225 字）· presenter 人像照片 · MiniMax / 豆包 API 凭证

→

处理

#### 五阶段管线

文案锁定 → TTS 配音 → 人像准备 → 分段数字人生成 → 拼接交付

→

输出

#### 成片

9:16 竖版 · presenter_60s.mp4 · 全程 55 秒口播 + 字幕可叠加

### 02五阶段制作链路

点击任意阶段卡片展开输入、工具、参数与实测数据。时间轴以真实执行顺序与实测耗时为刻度。

T+00:00

STAGE 1 · 文案

#### 锁定 60 秒科普配音文案225 字 · 11 句节拍

钩子 1 句 + 主体 3 节 8 句 + 收束 2 句；零功效声称、零绝对化用语、零商业信息，合规风险最低。

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>输入</div><div>冬虫夏草60秒科普配音文案.md</div></div>

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>输出</div><div>冬虫夏草-配音稿.txt<small>（TTS 友好：无引号、数字写汉字）</small></div></div>

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>语速</div><div>4.5 字/秒<small>（讲解类常用区间 4.0–4.8）</small></div></div>

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>时长推算</div><div>净口播 ≈50s · 含停顿 ≈55s<small>（留 ~5s 片头余量）</small></div></div>

时长调整预案（超时删句 / 欠时补句，不靠放慢语速凑时长）

复制

```
超时删句（按序）：① 删「至今，它仍无法大规模人工栽培。」≈3s
                ② 「冬虫夏草，其实是个误会。」压缩句 02 ≈1.5s
                ③ 删「冬天是虫，夏天是草，名字就是这么来的。」≈4.5s
欠时补句（按序）：① 句 08 后补「能长到出土的，只是极少数。」≈3s
                ② 句 07 后补「海拔低的地方，它活不下来。」≈3s
```

关键约束

字数（225）是硬约束，时长（55s）是软结果：同一段文字换配音员可差 ±8 秒。音频一旦生成，改文案 = 整条链路返工。

T+00:02

STAGE 2 · 配音

#### MiniMax TTS 生成旁白speech-02-hd · male-qn-qingse

一次性合成全稿，实测 54.91 秒、880KB MP3，落在 55–62s 达标区间，无需删句。

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>模型</div><div>speech-02-hd</div></div>

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>音色</div><div>male-qn-qingse</div></div>

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>语速</div><div>1.05</div></div>

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>采样</div><div>24kHz · mp3</div></div>

voiceover.py · 环境变量注入凭证后运行

复制

```
Set-Location "O:\video\20260929_冬虫夏草60秒配音文案"
$env:MINIMAX_BASE = "https://api.minimaxi.com"   # 脚本内部拼 /v1/t2a_v2
python voiceover.py
# 输出：narration.mp3（54.91s）· delivery-report.json
```

两次踩坑

①`api.minimaxi.cn`返回网页而非 API；正确域名为`api.minimaxi.com`，且 base 不要带`/v1`。②`audio_setting.bitrate`传 192000 会报`2013 invalid params`，去掉该字段即可。

T+00:03

STAGE 3 · 人像

#### Presenter 照片转正PNG → JPG → 720×1280

书房场景、黑框眼镜、米色衬衫、领夹麦；统一为 9:16 偶数尺寸，供各生成平台复用。

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>原始素材</div><div>微信图片…5_2.png / ChatGPT Image…png</div></div>

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>输出</div><div>presenter.jpg<small>（941×1672 → 720×1280）</small></div></div>

尺寸归一化（H264 要求宽高为偶数）

复制

```
ffmpeg -y -nostdin -i presenter.png -q:v 9 presenter.jpg
ffmpeg -y -nostdin -loop 1 -i presenter.jpg `
  -vf "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280" `
  -t 15 -r 30 -pix_fmt yuv420p -c:v libx264 -crf 23 -preset fast v_seg.mp4
```

踩坑

原图`941×1672`宽度为奇数，libx264 直接报`width not divisible by 2`并产出 0 字节文件——必须先 scale + crop 到偶数尺寸。

T+00:05

STAGE 4 · 生成

#### 数字人视频分段生成两条路径实测

55s 音频超出单条时长上限，按 12s/15s 切段；每条用同一人像 + 对应音频片段驱动，逐段提交、轮询、下载。

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>路径 A · MiniMax H3</div><div>/v2/video_generation<small>768P · 9:16 · 单段≤12s</small></div></div>

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>路径 B · 豆包 Seedance</div><div>seedance_2.5（29s+26s）/ seedance_2.0_fast（15s×3+10s）</div></div>

音频切段（按 15s 上限）

复制

```
ffmpeg -y -nostdin -i narration.mp3 -t 15  -c:a libmp3lame -q:a 4 a_seg0.mp3
ffmpeg -y -nostdin -i narration.mp3 -ss 15 -t 15 -c:a libmp3lame -q:a 4 a_seg1.mp3
# ... 依次切满 55s；每段配一条同尺寸人像基视频 v_segN.mp4 提交
```

两个平台的关键差异

① MiniMax H3 必须走`/v2/video_generation`，图片 role 用`reference_image`（v1 的`first_frame`报`2013`）；② 豆包侧真人照片需先开启「素材合规承诺」，且参考视频不能是空流（空 mp4 会报`empty audio stream`）。

T+06:00

STAGE 5 · 交付

#### 拼接成片与质检ffmpeg concat · loudnorm

所有分段按顺序拼接；校验总时长、响度（目标 -16 LUFS）、黑帧/冻结画面，产出主片与分享片。

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>拼接</div><div>ffmpeg -f concat -c copy</div></div>

<div style="display:grid;grid-template-columns:110px 1fr;gap:8px 16px;margin:14px 0"><div>响度</div><div>loudnorm I=-16:TP=-1.5:LRA=11<small>两遍式标准化</small></div></div>

拼接命令（分段编码一致时走 copy）

复制

```
ffmpeg -y -f concat -safe 0 -i _concat.txt -c copy presenter_60s.mp4
# 编码不一致时回退 re-encode：
#   -c:v libx264 -crf 20 -c:a aac -pix_fmt yuv420p
```

质量门禁

生成后必须完整解码回读、全速播放目检口型/身份/手部/曝光，并抽帧做九宫格联系表；`check_state`全绿才可交付。

### 03踩坑与经验

同一动作失败两次就换通道，不降级交付物；下面这些是本次实测记录下来的修复路径。

##### !SSL 证书过期 / 域名回退

Python 访问`api.minimaxi.cn`报`CERTIFICATE_VERIFY_FAILED`，且该域名对 API 路径返回网页。改用`api.minimaxi.com`（base 不含`/v1`）后连通。

##### !TTS 参数 2013

`audio_setting.bitrate=192000`触发`invalid params`。去掉 bitrate 字段即可，默认输出 128kbps MP3，音质达标。

##### !H3 接口版本与 role

MiniMax-H3 必须用`/v2/video_generation`（v1 报「该模型请使用 v2 接口」）；图片`role`用`reference_image`，`first_frame`与 reference 场景互斥。

##### !空视频流 / 奇数尺寸

0 字节的基视频提交报`empty audio stream`；941 奇数宽让 libx264 直接失败。先`scale+crop`到 720×1280 再生成。

##### <svg viewbox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="3"><path d="M4 12.5l5 5L20 6.5"></path></svg>豆包素材合规承诺

真人照片入视频前需在设置 → 内容生成与产物设置 → 打开「素材合规承诺」，否则接口直接拒绝生成。

##### <svg viewbox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="3"><path d="M4 12.5l5 5L20 6.5"></path></svg>额度与模型路由

seedance 2.5 是会员专属且消耗最大；>15s 必须用它，短段优先`seedance_2.0_fast`（单段 4–15s）。额度用尽时平台会提示恢复时间，勿反复重试。

### 04文件与产物清单

目录`O:\video\20260929_冬虫夏草60秒配音文案\`下的实际文件；加亮行为本轮交付的核心产物。

| 文件 | 类型 / 角色 | 大小 | 说明 |
|---|---|---|---|
| 冬虫夏草60秒科普配音文案.md | 文案 | 8.2KB | 节拍表、时长预案、合规与事实边界 |
| 冬虫夏草-配音稿.txt | 文案 | 0.8KB | TTS 友好纯文本，225 字 |
| narration.mp3 | 配音 | 880KB | 54.91s · 24kHz MP3 · 全链路时间基准 |
| presenter.jpg | 人像 | 103KB | 书房场景 · 720×1280 归一化 |
| voiceover.py / h3_generate.py / run_pipeline.py | 脚本 | — | TTS、H3、一键管线（含踩坑修正） |
| a_seg*.mp3 / v_seg*.mp4 | 中间件 | — | 按 15s 上限切分的音频段与同尺寸人像基视频 |
| presenter_60s.mp4 | 成片 | — | 9:16 竖版 · 拼接后约 55s 口播视频 |

### 05备选路径与下一步

本次执行中并行验证过的三条生成路径，按成本与速度选择。

A

##### MiniMax H3 数字人

音频驱动口型、同一人像跨段。v2 接口已调通；受账户余额限制（HTTP 402），充值后即可续跑。

余额不足 · 待续

B

##### 豆包 Seedance 2.5

会员专属、单条可达 30s，55s 音频仅需两段。消耗额度最大，需先开素材合规承诺。

额度门控 · 待续

C

##### 豆包 Seedance 2.0_fast

15s/段、速度最快、额度消耗最低，适合先出样片验证口型与身份；质量略低于 2.5。

快速样片首选

AI Presenter Video Pipeline · 复现文档 v1.0

数据来源：2026-09-29 实际执行记录

已复制到剪贴板
