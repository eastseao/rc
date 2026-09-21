<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230f766e'/%3E%3Cpath d='M16 44V20l16 12 16-12v24' stroke='white' stroke-width='5' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<title>商务沟通：订单与打样安排汇总</title>
<meta name="description" content="订单追加、梯度报价、下单与打样寄样安排，以及原浆铝瓶第三方送检的两点确认事项，整理为可直接用于邮件的商务纪要。">
<link rel="stylesheet" href="../theme.css">
<style>
:root{
  --s1:#0d9488; --s2:#2563eb; --s3:#7c3aed; --s4:#ea580c; --s5:#db2777;
  --s1s:#ccfbf1; --s2s:#dbeafe; --s3s:#ede9fe; --s4s:#ffedd5; --s5s:#fce7f3;
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

.card{background:#fbfcfd;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;margin-bottom:14px}
.card-h{padding:14px 18px;border-bottom:1px solid var(--line);border-top:3px solid var(--sc,var(--accent));background:var(--scs,var(--accent-soft))}
.card-h .tag{display:inline-block;font-family:var(--mono);font-size:10.5px;font-weight:700;color:var(--sc,var(--accent));background:#fff;border:1px solid var(--sc,var(--accent));border-radius:999px;padding:2px 9px;margin-bottom:7px;letter-spacing:.04em}
.card-h h3{font-size:16px;font-weight:700;color:var(--ink);line-height:1.45}
.card-b{padding:18px}
.kv{display:grid;grid-template-columns:120px minmax(0,1fr);gap:10px 16px}
.kv dt{font-family:var(--mono);font-size:11.5px;font-weight:700;color:var(--accent-ink);padding-top:3px;letter-spacing:.02em}
.kv dd{font-size:13.5px;color:var(--ink);line-height:1.72}
.kv dd ul{margin:0;padding-left:18px}
.kv dd li{margin-bottom:6px;line-height:1.7}
@media(max-width:560px){.kv{grid-template-columns:1fr;gap:2px 0}.kv dt{padding-top:8px}}

.tblwrap{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;margin-bottom:20px}
table{width:100%;border-collapse:collapse;font-size:13px}
th{background:var(--band);color:#475569;text-align:left;font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.04em;padding:10px 11px;border-bottom:1px solid var(--line)}
td{padding:10px 11px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2);line-height:1.7}
tbody tr:nth-child(even) td{background:#fbfcfd}
tbody tr:last-child td{border-bottom:0}
td b{color:var(--ink)}

.rl{border:1px solid #f3c6c4;background:var(--danger-soft);border-radius:var(--radius);padding:15px 17px;margin-bottom:14px}
.rl h4{font-family:var(--mono);font-size:11.5px;font-weight:700;color:var(--danger);letter-spacing:.06em;margin-bottom:7px}
.rl .mid{font-size:15px;font-weight:700;color:var(--ink);margin-bottom:8px;line-height:1.5}
.rl p{font-size:13.5px;color:var(--ink-2);line-height:1.72}

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
.strd{--sc:var(--danger);--scs:var(--danger-soft)}

@media(max-width:900px){
  .s-main{padding:8px 18px 30px}
  .s-nav{overflow-x:auto;scrollbar-width:none}
  .s-nav::-webkit-scrollbar{display:none}
}
@media(max-width:760px){
  .tblwrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
  table{min-width:600px;font-size:12.5px}
  th,td{padding:9px 9px}
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
      <a href="#s1" data-sec="s1">01 订单事项</a>
      <a href="#s2" data-sec="s2">02 打样寄样</a>
      <a href="#s3" data-sec="s3">03 铝瓶送检</a>
    </nav>
  </div>
</header>

<div class="s-head">
  <span class="s-eyebrow">商务沟通 · 订单与打样</span>
  <h1 class="s-h1">订单与打样安排汇总</h1>
  <p class="s-lede">把当日订单追加、梯度报价、下单与打样寄样整理成正式商务纪要，便于直接用于邮件或工作沟通；另附原浆铝瓶第三方送检的两点内部确认事项。</p>
  <div class="s-meta">
    <span>发布日期 <b>2025-11-12</b></span>
    <span>文档类型 <b>商务纪要</b></span>
    <span>适用对象 <b>采购 / 供应商对接</b></span>
  </div>
  <div class="s-chips">
    <span class="s-chip">追加订单</span>
    <span class="s-chip">梯度报价</span>
    <span class="s-chip">打样寄样</span>
    <span class="s-chip">第三方送检</span>
  </div>
</div>

<div class="s-body">
<main class="s-main">

  <section id="s1" class="st1">
    <div class="sec-h"><span class="idx st1">01</span><h2>订单相关事宜</h2><span class="hint">今日需推进</span></div>

    <div class="card st1">
      <div class="card-h"><span class="tag">追加订单</span><h3>γ-氨基丁酸酸枣仁饮品（桃子味）350ml 外盒 · 追加 3 万盒</h3></div>
      <div class="card-b">
        <dl class="kv">
          <dt>项目</dt><dd>产品外盒</dd>
          <dt>追加数量</dt><dd>30,000 盒</dd>
          <dt>当前库存</dt><dd>外盒库存 37,000 盒；对应内托与卡纸库存 38,000 件</dd>
          <dt>要求</dt><dd>请基于此数量出具一份正式的订单回稿文件以供确认</dd>
        </dl>
      </div>
    </div>

    <div class="card st2">
      <div class="card-h"><span class="tag">梯度报价</span><h3>同产品外盒 · 今日按三个数量梯度报价</h3></div>
      <div class="card-b">
        <dl class="kv">
          <dt>项目</dt><dd>γ-氨基丁酸酸枣仁饮品（桃子味）350ml 产品外盒</dd>
          <dt>报价数量</dt><dd>请按 <b>5,000 盒 / 10,000 盒 / 20,000 盒</b> 三个梯度分别报价</dd>
          <dt>要求</dt><dd>请于今日提供正式报价，并出具含以上梯度的正式回稿报价文件</dd>
        </dl>
      </div>
    </div>

    <div class="card st3">
      <div class="card-h"><span class="tag">直接下单</span><h3>280g 山药粉产品包装盒</h3></div>
      <div class="card-b">
        <dl class="kv">
          <dt>项目</dt><dd>280g 山药粉产品包装盒</dd>
          <dt>下单数量</dt><dd>2,000 个</dd>
          <dt>要求</dt><dd>请安排下单生产</dd>
        </dl>
      </div>
    </div>
  </section>

  <section id="s2" class="st2">
    <div class="sec-h"><span class="idx st2">02</span><h2>打样与寄样事宜</h2><span class="hint">今日务必寄出</span></div>
    <p class="lede">以下样品需于<b>今日</b>安排寄出，并同步提供报价。</p>

    <div class="card st4">
      <div class="card-h"><span class="tag">寄样一</span><h3>自热燕窝封套</h3></div>
      <div class="card-b">
        <p style="font-size:13.5px;color:var(--ink);line-height:1.78">今日务必寄出样品。</p>
      </div>
    </div>

    <div class="card st3">
      <div class="card-h"><span class="tag">寄样二 · 两款</span><h3>人参不定根包装盒（两款）</h3></div>
      <div class="card-b">
        <dl class="kv">
          <dt>寄样</dt><dd>两款盒子的样品今日务必一并寄出</dd>
          <dt>报价方式</dt><dd>请根据两款盒子分别使用的<b>材质与工艺</b>提供口头报价</dd>
          <dt>报价数量</dt><dd>2,000 个</dd>
        </dl>
      </div>
    </div>
  </section>

  <section id="s3" class="strd">
    <div class="sec-h"><span class="idx strd">03</span><h2>原浆铝瓶送检 · 两点确认</h2><span class="hint">需内部确认后反馈厂家</span></div>
    <div class="srcnote"><b>背景</b>：装原浆所用铝瓶已与厂家初步沟通。厂家已咨询第三方检测机构，确认出具检测报告的时间周期约为 <b>15 个工作日</b>。</div>

    <div class="rl">
      <h4>确认点一 · 送检样品规格</h4>
      <div class="mid">光板素瓶，还是带印刷图案的成品瓶？</div>
      <p>需确认送检的铝瓶样品，是提供光板素瓶，还是提供带有印刷图案的成品瓶。</p>
    </div>
    <div class="rl">
      <h4>确认点二 · 送检指标项目</h4>
      <div class="mid">检测需涵盖哪些具体指标？</div>
      <p>需由我方明确本次检测需要涵盖的具体指标清单。待信息明确后，将立即通知厂家安排后续送检工作。</p>
    </div>
  </section>

</main>
</div>

<footer class="s-foot">
  <div class="s-foot-in">
    <b>GERVAS</b>
    <span>订单与打样安排汇总 · V1.0</span>
    <span class="sp">Copyright 2026 gervas.wang</span>
  </div>
  <div class="s-disc"><p>本页为商务沟通纪要整理，具体数量与交期以最终确认函为准。</p></div>
</footer>

<a class="g-pill" href="../index.html" title="返回作品集首页">返回首页</a>

<script>
(function(){
  var SECS=['s1','s2','s3'];
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
