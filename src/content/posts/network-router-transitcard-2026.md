---
title: "无线网络对比·路由器级联·公交卡技术"
description: "2.4G 与 5G 无线网络对比、路由器分线再接路由器（二级路由级联）方法、公交卡通信技术解析（NFC）与刷卡记录查询方法。"
pubDatetime: 2026-04-10
category: "建站与技术"
kind: "长文"
tags: ["2.4G/5G", "二级路由", "NFC", "公交卡"]
---

> **本文合并自以下笔记**：00601-2026-02-26 2.4G 与 5G 无线网对比00649-2026-03-04 路由器分线再接路由器方法00865-2026-04-07 公交卡通信技术解析00100-2025-09-09 公交卡刷卡记录查询方法汇总

## 01 · 2.4G 与 5G 无线网络对比（00601 · 2026-02-26）

现在的双频路由器同时广播 2.4GHz 和 5GHz 两个 Wi-Fi。两者不是「谁快谁慢」那么简单：**2.4G 胜在穿墙和覆盖，5G 胜在速度和抗干扰**，选哪个看你的位置和用途。

| 对比项 | 2.4GHz | 5GHz |
|---|---|---|
| **传输速度** | 慢，多为几十到几百 Mbps | 快，主流千兆起步，近距离跑满宽带 |
| **穿墙能力** | **强**，波长更长，穿一两堵墙信号仍可用 | 弱，穿墙后速度暴跌，隔墙可能只剩一格 |
| **覆盖范围** | 大，适合全屋/远距离弱信号区 | 小，适合路由器附近的设备 |
| **干扰情况** | 拥挤：蓝牙、微波炉、邻居 Wi-Fi 都挤在这 | 干净得多，频段宽、信道多 |
| **适合场景** | 离路由远、隔好几堵墙、只刷网页/微信 | 同屋打游戏、看 4K 视频、大文件传输 |

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">怎么连更合理</h3><p style="font-size:13.5px;color:inherit">路由器就在旁边、追求速度 → 连<b>5G</b>；隔了墙、信号总是不满、只是日常刷手机 → 连<b>2.4G</b>反而更稳。很多新手机/路由支持「双频合一」自动切换，嫌麻烦就开它。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">提醒</h3><p style="font-size:13.5px;color:inherit">2.4G 的「G」指频段，和手机套餐的 5G 移动网络不是一回事；这里说的 5GHz Wi-Fi 也不是第五代移动通信。智能家电（摄像头、插座）大多只支持 2.4G，配网时别连错。</p></div></div>

## 02 · 路由器分线再接路由器：二级路由接法（00649 · 2026-03-04）

想把客厅主路由的网口用一根网线拉到房间，再接第二台路由器扩大覆盖，常见两种接法：**LAN-LAN（当无线交换机用）**和**LAN-WAN（真二级路由）**。选哪种看你要不要第二台再分一层内网。

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>接法一 · LAN-LAN</span><h3>把第二台当无线交换机（推荐新手）</h3></div><div style="padding:14px 16px"><ol style="margin:0;padding-left:20px;font-size:13.5px;color:inherit"><li style="margin-bottom:8px">先用电脑/手机连上<b>第二台路由器自己的 Wi-Fi</b>，进它的管理页（地址见机身标签，如 192.168.1.1）。</li><li style="margin-bottom:8px"><b>关掉第二台的 DHCP 服务器</b>——这是关键一步，否则两台都分地址会打架。</li><li style="margin-bottom:8px">网线从<b>主路由的 LAN 口</b>出来，插到<b>第二台的 LAN 口</b>（注意不是 WAN 口）。</li><li>第二台的 Wi-Fi 名称/密码可以设成和主路由一样（漫游更顺），它就相当于把主路由的有线信号转成 Wi-Fi 继续发。</li></ol><p style="font-size:13.5px;color:inherit;margin-top:8px">优点：所有设备在同一网段，互相访问最方便，打印/投屏都不折腾。</p></div></div>

<div style="border:1px solid #dfe6ef;border-radius:8px;overflow:hidden;background:#fff;margin:14px 0"><div style="padding:12px 16px;border-bottom:1px solid #dfe6ef;background:#f6f8fa;font-weight:700"><span>接法二 · LAN-WAN</span><h3>第二台做独立二级路由</h3></div><div style="padding:14px 16px"><ol style="margin:0;padding-left:20px;font-size:13.5px;color:inherit"><li style="margin-bottom:8px">网线从<b>主路由 LAN 口</b>出来，插到<b>第二台的 WAN 口</b>。</li><li style="margin-bottom:8px">第二台 DHCP<b>保持开启</b>，并把它的 LAN 网段改成和主路由不同（例如主路由是 192.168.1.x，第二台改成 192.168.2.1），避免 IP 冲突。</li><li>第二台自己拨号或自动获取主路由分来的地址，形成独立小内网。</li></ol><p style="font-size:13.5px;color:inherit;margin-top:8px">优点：隔离性强；缺点：跨网段访问设备需要额外设置，新手容易在投屏、远程访问上踩坑。</p></div></div>

> **排坑要点**
> - 两根线插错口是最高频错误：LAN-LAN 接法必须两头都是 LAN 口；WAN/LAN 口通常有颜色区分。
> - 两台路由不要用相同 LAN 网段，DHCP 只留一台开（LAN-LAN 时留主路由开）。
> - 网线距离别太长，超五类线建议不超过约 80–100 米，否则丢包严重。

## 03 · 公交卡通信技术解析：NFC 非接触式（00865 · 2026-04-07）

把公交卡往读卡器上一靠，「嘀」一声就完成扣款——这背后是**NFC（近场通信）**为基础的非接触式 IC 卡技术，和身份证、手机刷卡乘车是同一类原理。

<div style="display:grid;gap:14px;margin:14px 0;grid-template-columns:repeat(2,minmax(0,1fr))"><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">卡是怎么「供电」和「通信」的</h3><p style="font-size:13.5px;color:inherit">实体公交卡（如 MIFARE 类）<b>本身不带电池</b>。读卡器发出 13.56MHz 的射频场，卡片靠近时卡内线圈感应出电流给自己供电，再把卡号/余额等数据通过射频回传给读卡器，整个过程在几厘米内、毫秒级完成——所以「贴一下」就行，不需要接触。</p></div><div style="border:1px solid #dfe6ef;border-radius:8px;padding:16px 20px;background:#fff;margin:14px 0"><h3 style="font-size:15px;font-weight:700;margin-bottom:8px">和手机 NFC 刷卡的关系</h3><p style="font-size:13.5px;color:inherit">手机 NFC 模拟的就是这张卡：手机里的 NFC 芯片虚拟出一张「卡」，向闸机读卡器出示同一份协议的卡号。交通联合、各地公交 App 的「乘车码」NFC 模式走的都是这套近场通信标准，因此可以互刷。</p></div></div>

| 特点 | 说明 |
|---|---|
| **工作频率** | 13.56MHz，感应距离通常 4cm 以内，贴太近太远都不行。 |
| **无源卡** | 实体卡靠读卡器电磁场取电，所以卡面没有电池、不怕没电，只是余额随次数扣减。 |
| **速度与安全** | 一次交易毫秒级；卡号与密钥分区存储，消费记录由后台系统统一记账。 |
| **与 RFID 的关系** | NFC 是 RFID 在 13.56MHz 频段上的近场标准，公交卡、门禁卡、银行卡闪付都属这一家族。 |

## 04 · 公交卡刷卡记录查询方法汇总（00100 · 2025-09-09）

想查某张公交卡最近坐了哪几趟车、刷了多少钱，实体卡和手机 NFC 卡的查询渠道不一样。原笔记汇总了常用几条路子。

| 渠道 | 能查到什么 / 怎么查 |
|---|---|
| **官方 App / 小程序** | 当地公交集团或「交通联合」App、小程序绑卡后，一般可看近一个月的消费记录、时间、线路和余额——最方便的首选。 |
| **手机 NFC 读卡** | 带 NFC 的安卓手机装读卡工具，把实体卡贴背面可读出卡号、近期交易摘要；部分城市 NFC 公交卡（如华为/小米钱包）直接在钱包 App 里看明细。 |
| **地铁站客服 / 充值点** | 拿实体卡到地铁客服中心或公交充值窗口，工作人员可在系统里打印/查询较完整的交易流水。 |
| **官方网站 / 客服电话** | 当地公交卡官网或客服热线，报卡号和身份信息后可申请导出历史记录，适合需要长周期明细报销/核对的场景。 |

> **说明**
> - 记录保留时长和明细粒度各城市不同：App 通常只留近期一个月，导出历史要走官方渠道。
> - 实体卡挂失、补卡、退余额都以官方系统记录为准，自己截图的读卡信息不能作凭证。
