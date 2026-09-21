<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230f766e'/%3E%3Cpath d='M16 44V20l16 12 16-12v24' stroke='white' stroke-width='5' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<title>包装采购下单全流程及注意事项</title>
<meta name="description" content="从需求定义、寻源询价、决策签约、生产跟单到验收结算，一款包装从概念到收货的五阶段采购作业手册与注意事项清单。">
<link rel="stylesheet" href="../theme.css">
<style>
:root{
  --s1:#0d9488; --s2:#2563eb; --s3:#7c3aed; --s4:#ea580c; --s5:#db2777;
  --s1s:#ccfbf1; --s2s:#dbeafe; --s3s:#ede9fe; --s4s:#ffedd5; --s5s:#fce7f3;
  --fz-xs:12px; --fz-sm:13px; --fz:14px; --fz-md:15px;
  --fz-lg:17px; --fz-xl:21px; --fz-2xl:29px;
  --sp1:4px; --sp2:8px; --sp3:12px; --sp4:16px; --sp5:22px; --sp6:30px; --sp7:42px;
  --bar-h:50px;
  --side-ink:#94a3b8; --side-ink-hi:#5eead4; --side-hi:rgba(13,148,136,.18);
  --sc:var(--accent); --scs:var(--accent-soft);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:14.5px;line-height:1.76;-webkit-font-smoothing:antialiased}

.s-bar{background:#0f172a;color:#f1f5f9;position:sticky;top:0;z-index:60}
.s-bar-in{max-width:var(--maxw);margin:0 auto;padding:0 32px;height:var(--bar-h);display:flex;align-items:center;gap:12px}
.s-brand{font-family:var(--mono);font-size:14px;font-weight:700;letter-spacing:.1em;white-space:nowrap}
.s-brand em{font-style:normal;font-size:12px;font-weight:400;color:var(--side-ink);letter-spacing:.02em;margin-inline-start:8px}
.s-nav{margin-inline-start:auto;display:flex;align-items:center;gap:2px;font-size:13px}
.s-nav a{padding:5px 11px;border-radius:var(--radius-sm);color:var(--side-ink);text-decoration:none;white-space:nowrap;transition:.15s}
.s-nav a:hover{color:#f1f5f9}
.s-nav a.on{color:#f1f5f9;background:var(--side-hi);font-weight:600}

.s-head{max-width:var(--maxw-read);margin:0 auto;padding:44px 32px 0}
.s-eyebrow{display:inline-flex;align-items:center;gap:7px;font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--accent)}
.s-eyebrow::before{content:"";width:5px;height:5px;border-radius:50%;background:var(--accent)}
.s-h1{font-size:clamp(23px,2.9vw,32px);font-weight:700;letter-spacing:-.014em;line-height:1.28;margin:14px 0 12px;color:var(--ink)}
.s-lede{font-size:14.5px;color:var(--muted);line-height:1.8;max-width:var(--maxw-text)}
.s-meta{margin-top:16px;padding-top:14px;border-top:1px solid var(--line);font-family:var(--mono);font-size:11.5px;color:var(--muted-2);display:flex;flex-wrap:wrap;gap:6px 16px}
.s-meta b{color:var(--ink);font-weight:700}
.s-chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:14px}
.s-chip{display:inline-block;font-family:var(--mono);font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px;background:var(--accent-soft);color:var(--accent)}

.s-body{max-width:var(--maxw-read);margin:0 auto;padding:26px 32px 50px}
.s-main{min-width:0;max-width:var(--maxw-read);margin:0 auto;background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 34px 40px}

section{padding-top:28px;border-top:1px solid var(--line);scroll-margin-top:calc(var(--bar-h) + 14px)}
section:first-of-type{border-top:0;padding-top:22px}
.sec-h{display:flex;align-items:baseline;gap:12px;margin-bottom:14px;flex-wrap:wrap}
.sec-h .idx{font-family:var(--mono);font-size:11px;font-weight:700;color:var(--sc,var(--accent));background:var(--scs,var(--accent-soft));border:1px solid transparent;padding:3px 10px;border-radius:var(--radius-sm);letter-spacing:.06em;white-space:nowrap}
.sec-h h2{font-size:19px;font-weight:700;letter-spacing:-.012em;color:var(--ink);line-height:1.4}
.sec-h .hint{font-family:var(--mono);font-size:11px;color:var(--muted-2)}
.lede{font-size:14px;color:var(--ink-2);margin-bottom:16px;max-width:var(--maxw-text);line-height:1.78}
.lede b{color:var(--ink)}

.panel{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px}
.grid{display:grid;gap:14px}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
@media(max-width:1100px){.g3{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:760px){.g3,.g2{grid-template-columns:1fr}}

.rl{border:1px solid #f3c6c4;background:var(--danger-soft);border-radius:var(--radius);padding:15px 17px}
.rl h4{font-family:var(--mono);font-size:11.5px;font-weight:700;color:var(--danger);letter-spacing:.06em;margin-bottom:7px}
.rl .mid{font-size:15px;font-weight:700;color:var(--ink);margin-bottom:8px;line-height:1.5}
.rl p{font-size:13.5px;color:var(--ink-2);line-height:1.72}

.card{background:#fbfcfd;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.card-h{padding:14px 18px;border-bottom:1px solid var(--line);border-top:3px solid var(--sc,var(--accent));background:var(--scs,var(--accent-soft))}
.card-h .tag{display:inline-block;font-family:var(--mono);font-size:10.5px;font-weight:700;color:var(--sc,var(--accent));background:#fff;border:1px solid var(--sc,var(--accent));border-radius:999px;padding:2px 9px;margin-bottom:7px;letter-spacing:.04em}
.card-h h3{font-size:16px;font-weight:700;color:var(--ink);line-height:1.45}
.card-b{padding:18px}
.kv{display:grid;grid-template-columns:104px minmax(0,1fr);gap:10px 16px}
.kv dt{font-family:var(--mono);font-size:11.5px;font-weight:700;color:var(--accent-ink);padding-top:3px;letter-spacing:.02em}
.kv dd{font-size:13.5px;color:var(--ink);line-height:1.72}
.kv dd ul{margin:0;padding-left:18px}
.kv dd li{margin-bottom:6px;line-height:1.7}
@media(max-width:560px){.kv{grid-template-columns:1fr;gap:2px 0}.kv dt{padding-top:8px}}
.warnbox{margin-top:16px;background:var(--warn-soft);border:1px solid var(--warnline);border-radius:var(--radius-sm);padding:14px 16px}
.warnbox h5{font-family:var(--mono);font-size:11.5px;font-weight:700;color:var(--warn);margin-bottom:8px;letter-spacing:.06em}
.warnbox ul{margin:0;padding-left:18px}
.warnbox li{font-size:13.5px;color:var(--ink);margin-bottom:7px;line-height:1.7}

.tblwrap{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;margin-bottom:20px}
table{width:100%;border-collapse:collapse;font-size:13px}
th{background:var(--band);color:#475569;text-align:left;font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.06em;padding:10px 13px;border-bottom:1px solid var(--line)}
td{padding:10px 13px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2);line-height:1.7}
tbody tr:nth-child(even) td{background:#fbfcfd}
tbody tr:last-child td{border-bottom:0}

.srcnote{font-size:13.5px;color:var(--ink-2);background:var(--warn-soft);border:1px solid var(--warnline);border-radius:var(--radius-sm);padding:14px 16px;margin-bottom:16px}
.srcnote b{color:var(--warn)}

.s-foot{background:var(--band);border-top:1px solid var(--line)}
.s-foot-in{max-width:var(--maxw);margin:0 auto;padding:26px 32px 10px;display:flex;flex-wrap:wrap;gap:10px 22px;align-items:center;font-size:12.5px;color:var(--muted)}
.s-foot b{font-family:var(--mono);font-size:12px;font-weight:700;letter-spacing:.14em;color:var(--ink)}
.s-foot .sp{margin-inline-start:auto;font-family:var(--mono);font-size:11px;color:var(--muted-2)}
.s-disc{max-width:var(--maxw);margin:0 auto;padding:0 32px 24px;font-size:12px;color:var(--muted-2);line-height:1.7}

.st1{--sc:var(--s1);--scs:var(--s1s)}
.st2{--sc:var(--s2);--scs:var(--s2s)}
.st3{--sc:var(--s3);--scs:var(--s3s)}
.st4{--sc:var(--s4);--scs:var(--s4s)}
.st5{--sc:var(--s5);--scs:var(--s5s)}
.strd{--sc:var(--danger);--scs:var(--danger-soft)}

@media(max-width:900px){
  .s-main{padding:8px 18px 30px}
  .s-nav{overflow-x:auto;scrollbar-width:none}
  .s-nav::-webkit-scrollbar{display:none}
}
@media(max-width:760px){
  .tblwrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
  table{min-width:600px;font-size:12.5px}
  th,td{padding:9px 11px}
}
@media(max-width:640px){
  .s-brand em{display:none}
  .s-nav a{padding:5px 8px;font-size:12.5px}
  .s-head{padding:30px 18px 0}
  .s-bar-in,.s-foot-in,.s-disc{padding-inline:18px}
}
</style>
</head>
<body>

<header class="s-bar">
  <div class="s-bar-in">
    <span class="s-brand">GERVAS<em>日常 · Agent 作品集</em></span>
    <nav class="s-nav" id="topnav" aria-label="章节导航">
      <a href="#s0" data-sec="s0">00 总览</a>
      <a href="#s1" data-sec="s1">01 准备定义</a>
      <a href="#s2" data-sec="s2">02 寻源询价</a>
      <a href="#s3" data-sec="s3">03 决策签约</a>
      <a href="#s4" data-sec="s4">04 生产跟单</a>
      <a href="#s5" data-sec="s5">05 验收结算</a>
    </nav>
  </div>
</header>

<div class="s-head">
  <span class="s-eyebrow">操作手册 · 采购 SOP</span>
  <h1 class="s-h1">包装采购下单全流程及注意事项</h1>
  <p class="s-lede">一款包装从概念到收货的完整路线图。把整个采购拆成五个阶段——前期准备与定义、寻源与询价、决策与签约、生产与跟单、验收与结算——逐阶段列出核心任务、关键输出与容易踩坑的注意事项。</p>
  <div class="s-meta">
    <span>发布日期 <b>2025-09-18</b></span>
    <span>文档类型 <b>作业手册</b></span>
    <span>适用对象 <b>包装采购 / 跟单</b></span>
  </div>
  <div class="s-chips">
    <span class="s-chip">RFQ 询价</span>
    <span class="s-chip">确认样</span>
    <span class="s-chip">PO 合同</span>
    <span class="s-chip">跟单验货</span>
  </div>
</div>

<div class="s-body">
<main class="s-main">

  <section id="s0" class="st1">
    <div class="sec-h"><span class="idx st1">00</span><h2>五阶段总览</h2><span class="hint">线性流程 · 带反馈循环</span></div>
    <p class="lede">整个采购是一个<b>线性且带反馈循环</b>的系统工程：前一阶段的输出是后一阶段的输入。其中"实体样确认"和"大货样确认"是两个最重要的质量闸口，一旦签字确认，即成为后续生产与验收的标准。</p>
    <div class="tblwrap"><table>
      <thead><tr><th style="width:150px">阶段</th><th style="width:220px">核心任务</th><th>关键输出 / 注意事项</th></tr></thead>
      <tbody>
        <tr><td><b>1. 准备与定义</b></td><td>明确需求、完成设计</td><td>需求文档、设计稿（CMYK + 出血）、刀模图、确认样标准</td></tr>
        <tr><td><b>2. 寻源与询价</b></td><td>寻找供应商、获取报价和样品</td><td>RFQ 包、多家报价对比、<b>实体确认样</b></td></tr>
        <tr><td><b>3. 决策与签约</b></td><td>选定供应商、签订合同</td><td>采购合同 / PO（金额、付款方式、交期、质量条款）</td></tr>
        <tr><td><b>4. 生产与跟单</b></td><td>支付定金、跟进生产、确认大货样</td><td>付款凭证、生产进度照片、<b>大货样确认</b></td></tr>
        <tr><td><b>5. 验收与结算</b></td><td>验货、付款、收货、归档</td><td>验货报告、尾款支付、到货抽检记录、项目档案</td></tr>
      </tbody>
    </table></div>
    <div class="srcnote"><b>反馈循环</b>：若最终验收时发现问题，应可追溯至"确认大货样"甚至更早的环节进行核对与追责。第四阶段的"过程跟进"是主动介入而非被动等待，是保证交期和质量的关键。</div>
  </section>

  <section id="s1" class="st2">
    <div class="sec-h"><span class="idx st2">01</span><h2>前期准备与定义（内部工作）</h2><span class="hint">谋定而后动</span></div>
    <p class="lede">这是最重要的一步，决定了后续所有工作的方向和效率。先把需求和设计在内部彻底锁死，再对外沟通。</p>

    <div class="card st2">
      <div class="card-h"><span class="tag">需求定义</span><h3>明确产品、市场、预算与时间</h3></div>
      <div class="card-b">
        <dl class="kv">
          <dt>产品信息</dt><dd>包装产品的尺寸、重量、形状、材质；是否易碎，是否需要防潮 / 防震。</dd>
          <dt>市场定位</dt><dd>走高端奢华、环保简约还是成本优先路线——直接影响材质与工艺选择。</dd>
          <dt>预算范围</dt><dd>设定清晰的单件成本目标与总预算，含设计、打样、运输等全部费用。</dd>
          <dt>时间节点</dt><dd>明确大货交货日期，并反向推算设计、打样、生产、物流每个环节的截止日。</dd>
          <dt>数量要求</dt><dd>首次订单量、预计未来一年的采购频率与数量，影响单价与供应商配合度。</dd>
        </dl>
      </div>
    </div>

    <div class="grid g2" style="margin-top:14px">
      <div class="card st1">
        <div class="card-h"><span class="tag">设计文件</span><h3>结构设计与刀模图</h3></div>
        <div class="card-b">
          <dl class="kv">
            <dt>结构设计</dt><dd>盒型、开启方式合理，能有效保护产品，并便于自动化或人工包装。</dd>
            <dt>刀模图</dt><dd>提供准确的刀模图（Die-line）——展开后精确轮廓与压痕线，是制作模具的依据。</dd>
          </dl>
        </div>
      </div>
      <div class="card st4">
        <div class="card-h"><span class="tag">平面设计</span><h3>设计稿交付规范</h3></div>
        <div class="card-b">
          <dl class="kv">
            <dt>软件</dt><dd>用矢量软件（AI、CorelDRAW），避免用 Photoshop 等位图软件。</dd>
            <dt>出血位</dt><dd>设计稿必须含出血（通常 3mm），避免裁切后露白边。</dd>
            <dt>色彩模式</dt><dd>CMYK 模式；品牌色需提供潘通色号（Pantone）确保颜色准确。</dd>
            <dt>文字转曲</dt><dd>所有文字必须转曲（创建轮廓），避免供应商缺字体导致错版。</dd>
            <dt>工艺标注</dt><dd>在设计稿上明确标注烫金、UV、击凸、专色印刷等所需工艺。</dd>
          </dl>
        </div>
      </div>
    </div>

    <div class="warnbox" style="margin-top:16px"><h5>阶段注意事项</h5>
      <ul>
        <li><b>内部评审</b>：设计稿必须经市场、销售、物流等所有相关部门确认，避免事后修改。</li>
        <li><b>合规性</b>：检查成分表、生产日期、条形码、环保标识等所有需印制的信息是否符合法规与行业标准。</li>
      </ul>
    </div>
  </section>

  <section id="s2" class="st3">
    <div class="sec-h"><span class="idx st3">02</span><h2>寻源与询价（对外沟通）</h2><span class="hint">RFQ · 打样</span></div>
    <p class="lede">找到合适供应商，发出专业询价包，再通过打样把抽象的"报价"变成可触摸、可核对的实物。</p>

    <div class="card st3">
      <div class="card-h"><span class="tag">询价包 RFQ</span><h3>一份专业的询价包应包含</h3></div>
      <div class="card-b">
        <dl class="kv">
          <dt>需求说明</dt><dd>产品名称、数量、目标交货日期。</dd>
          <dt>设计稿文件</dt><dd>PDF 效果图 + 高精度可输出文件（AI 或 PDF）。</dd>
          <dt>刀模图</dt><dd>AI 或 DXF 格式的刀模文件。</dd>
          <dt>材质工艺</dt><dd>材质（如"350g 灰底白板纸""0.8mm 单坑瓦楞"）与工艺（如"四色印刷 + 专红烫金 + 局部 UV"）。</dd>
          <dt>样品要求</dt><dd>询问打样费用与周期。</dd>
        </dl>
      </div>
    </div>

    <div class="grid g2" style="margin-top:14px">
      <div class="panel">
        <h4 style="font-size:14.5px;color:var(--sc);margin-bottom:8px">供应商筛选</h4>
        <p style="font-size:13.5px;color:var(--ink-2)">渠道包括行业展会、B2B 平台（如阿里巴巴 1688）、朋友推荐与现有供应商网络。筛选时综合评估<b>专业领域</b>（是否擅长所需品类，如纸盒 / 软包 / 玻璃瓶）、生产能力、质量口碑、最小起订量（MOQ）、配合度与地理位置。</p>
      </div>
      <div class="panel">
        <h4 style="font-size:14.5px;color:var(--sc);margin-bottom:8px">报价对比不能只看价格</h4>
        <p style="font-size:13.5px;color:var(--ink-2)">要综合对比<b>单价、打样费、模具费</b>（刀模版、烫金版）、付款方式、交货周期。问清报价是否含税、含运费，是否有版费等隐藏费用；并确认订单量是否达到起订量，否则单价会很高。</p>
      </div>
    </div>

    <div class="grid g2" style="margin-top:14px">
      <div class="rl">
        <h4>打样 · 数字样</h4>
        <div class="mid">用于确认内容和颜色</div>
        <p>Virtual Sample，先在数字层面把内容、配色方向对齐。</p>
      </div>
      <div class="rl">
        <h4>打样 · 实体样（必须步骤）</h4>
        <div class="mid">签字即标准</div>
        <p>Physical Sample，用于确认材质、手感、工艺、结构、尺寸与实际装配效果。<b>一旦签字确认样品，大货就必须以样品为准。</b></p>
      </div>
    </div>

    <div class="warnbox" style="margin-top:16px"><h5>阶段注意事项</h5>
      <ul>
        <li><b>沟通效率</b>：与响应及时、沟通顺畅的供应商合作，能极大减少后续问题。</li>
        <li><b>评审样品</b>：收到样品后严格对照设计稿和需求逐项检查，再决定是否签字。</li>
      </ul>
    </div>
  </section>

  <section id="s3" class="st4">
    <div class="sec-h"><span class="idx st4">03</span><h2>决策与签约（内部评审与法律确认）</h2><span class="hint">锁定条款</span></div>
    <p class="lede">召集相关部门基于价格、质量、交期、服务共同定标，再把沟通成果固化成具有法律效力的合同 / PO。</p>

    <div class="card st4">
      <div class="card-h"><span class="tag">合同 / PO 必备条款</span><h3>采购合同或 PO 必须写清的内容</h3></div>
      <div class="card-b">
        <dl class="kv">
          <dt>双方信息</dt><dd>双方公司信息；产品详细描述（可注明"具体规格以确认样为准"）。</dd>
          <dt>金额</dt><dd>单价、总金额、货币类型。</dd>
          <dt>付款方式</dt><dd>通常"下单付 X%，交货付 X%"，如 30% 定金、70% 见提单付款或货到付清。</dd>
          <dt>交货</dt><dd>交货日期和地点；Incoterms 条款（如 FOB、EXW）要明确。</dd>
          <dt>质量验收</dt><dd>写明以确认样为准。</dd>
          <dt>违约责任</dt><dd>延迟交货、质量不达标等的处理办法。</dd>
        </dl>
      </div>
    </div>

    <div class="warnbox" style="margin-top:16px"><h5>阶段注意事项</h5>
      <ul>
        <li><b>签字盖章</b>：合同需双方签字盖章生效。</li>
        <li><b>付款谈判</b>：尽量争取对自己有利的付款方式；新供应商可要求更严格条款以控制风险。</li>
        <li><b>保留确认样</b>：双方各保留一份签字确认的样品，作为大货验收的"法官"。</li>
      </ul>
    </div>
  </section>

  <section id="s4" class="st5">
    <div class="sec-h"><span class="idx st5">04</span><h2>生产与跟单（过程监控）</h2><span class="hint">不是付了定金就万事大吉</span></div>
    <p class="lede">主动跟单是保证质量和交期的关键。从付定金、产前会到中期跟进与大货样确认，每一步都要有留痕。</p>

    <div class="tblwrap"><table>
      <thead><tr><th style="width:150px">跟单动作</th><th style="width:200px">要点</th><th>说明</th></tr></thead>
      <tbody>
        <tr><td><b>预付定金</b></td><td>按合同支付</td><td>支付预付款，通知供应商安排生产。</td></tr>
        <tr><td><b>产前会议</b></td><td>批量前确认细节</td><td>要求供应商在批量生产前召开产前会，确认所有细节。</td></tr>
        <tr><td><b>中期跟进</b></td><td>进度留痕</td><td>生产中期要求提供生产进度照片或视频（尤其首批合作）；有条件可安排中期验货（DPI）。</td></tr>
        <tr><td><b>确认大货样</b></td><td>二次确认品质</td><td>大货批量出来后要求寄送大货样，再次确认品质是否符合确认样标准。</td></tr>
      </tbody>
    </table></div>

    <div class="warnbox" style="margin-top:16px"><h5>阶段注意事项</h5>
      <ul>
        <li><b>变更管理</b>：任何对设计、材质、数量的变更都必须以书面形式（如邮件）确认，并评估对成本和交期的影响。</li>
        <li><b>风险预警</b>：如发现可能延迟，立即启动应急计划，与内部团队（市场、销售）沟通。</li>
      </ul>
    </div>
  </section>

  <section id="s5" class="strd">
    <div class="sec-h"><span class="idx strd">05</span><h2>验收与结算（收尾工作）</h2><span class="hint">及时验货 · 完整归档</span></div>
    <p class="lede">收尾不是简单签收付款。把好验货关、及时到货抽检、完整归档，才能为下一次采购和售后问题留好依据。</p>

    <div class="tblwrap"><table>
      <thead><tr><th style="width:150px">收尾动作</th><th>要点</th></tr></thead>
      <tbody>
        <tr><td><b>安排验货（可选但推荐）</b></td><td>重要订单或新供应商，可委托第三方验货公司（如 SGS、BV）或内部 QC 在出厂前做最终随机抽样检验（FRI），出具验货报告。</td></tr>
        <tr><td><b>尾款与物流</b></td><td>验货通过后按合同支付尾款；与供应商确认物流安排，获取提单 / 运单号跟踪货物动态。</td></tr>
        <tr><td><b>到货验收</b></td><td>货到仓库立即开箱抽检：核对数量、检查外箱破损、抽查内部包装有无瑕疵 / 脏污 / 破损 / 色差。发现问题立即拍照留存并与供应商沟通。</td></tr>
        <tr><td><b>对账结算</b></td><td>核对发票和订单，办理付款结算。</td></tr>
        <tr><td><b>项目归档</b></td><td>将合同、PO、设计稿、刀模图、确认样照片、沟通记录归档保存。</td></tr>
      </tbody>
    </table></div>

    <div class="warnbox" style="margin-top:16px"><h5>阶段注意事项</h5>
      <ul>
        <li><b>及时验货</b>：到货后尽快查验——大部分质量问题都有索赔期。</li>
        <li><b>仓库管理</b>：包装材料应存放在干燥、通风的仓库，避免挤压变形或受潮。</li>
      </ul>
    </div>
  </section>

</main>
</div>

<footer class="s-foot">
  <div class="s-foot-in">
    <b>GERVAS</b>
    <span>包装采购下单全流程 · V1.0</span>
    <span class="sp">Copyright 2026 gervas.wang</span>
  </div>
  <div class="s-disc"><p>本页内容整理自包装采购工作笔记，仅供内部参考。</p></div>
</footer>

<a class="g-pill" href="../index.html" title="返回作品集首页">返回首页</a>

<script>
(function(){
  var SECS=['s0','s1','s2','s3','s4','s5'];
  var secLinks=document.querySelectorAll('#topnav a[data-sec]');
  function mark(cur){
    for(var i=0;i<secLinks.length;i++){
      secLinks[i].classList.toggle('on', secLinks[i].getAttribute('data-sec')===cur);
    }
  }
  function spy(){
    var y=window.scrollY+130, cur=SECS[0];
    for(var i=0;i<SECS.length;i++){
      var s=document.getElementById(SECS[i]);
      if(!s) continue;
      var top=s.getBoundingClientRect().top+window.scrollY;
      if(top<=y) cur=SECS[i];
    }
    mark(cur);
  }
  window.addEventListener('scroll', spy, {passive:true});
  window.addEventListener('resize', spy);
  spy();
})();
</script>
</body>
</html>
