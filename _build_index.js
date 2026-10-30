import fs from 'node:fs';

// 改完 _pages_registry.js 并跑过 _build_home.js 之后，跑本脚本重出 index.html 的目录
// 用法：node _build_index.js
global.window = {};
await import('./manifest.js');
const W = window.WORKS;

const slugOf = u => (u || '')
  .replace(/^pages\//, '')
  .replace(/^tools\//, '')
  .replace(/\/index\.html$/, '')
  .replace(/\.html$/, '');

const sorted = [...W].filter(x => x.d && x.t).sort((a, b) => String(b.d).localeCompare(String(a.d)));
const rows = [];
for (const w of sorted) {
  const slug = slugOf(w.u);
  const img = `assets/works/${slug}.jpg`;
  if (!fs.existsSync(img)) continue;
  rows.push({ w, img });
  if (rows.length >= 10) break;
}

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const listHTML = rows.map(({ w, img }, i) => `      <li><a class="row" href="${w.u}">
        <img class="row-fig" src="${img}" alt="「${esc(w.t)}」页面顶部截图" width="208" height="130" loading="${i < 4 ? 'eager' : 'lazy'}" data-rv style="--i:${Math.min(i, 8) * 40}ms">
        <span class="row-body" data-rv style="--i:${Math.min(i, 8) * 40 + 45}ms"><span class="row-t">${esc(w.t)}</span><span class="row-d">${esc(w.d)}</span></span>
      </a></li>`).join('\n');

const html = `<!DOCTYPE html>
<html lang="zh-CN" class="no-js">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%231b1917'/%3E%3Cpath d='M8 21h16M8 16h16M8 11h9' stroke='%23a16207' stroke-width='2.4' stroke-linecap='round'/%3E%3C/svg%3E">
<title>GERVAS · 815 篇笔记与工具</title>
<meta name="description" content="一个人在杭州写了三年：815 篇笔记、21 个工具，九类，全部静态开源可检索。">
<link rel="canonical" href="https://eastseao.github.io/rc/">
<meta property="og:type" content="website">
<meta property="og:title" content="GERVAS · 815 篇笔记与工具">
<meta property="og:description" content="九类笔记、21 个工具，从 2023 年 10 月写到现在，全部能检索。">
<meta property="og:url" content="https://eastseao.github.io/rc/">
<meta name="twitter:card" content="summary">
<link rel="preload" href="assets/fonts/worksans-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>
@font-face{
  font-family:"Work Sans"; font-style:normal; font-weight:300 500; font-display:swap;
  src:url("assets/fonts/worksans-latin.woff2") format("woff2");
  unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215;
}
@font-face{
  font-family:"Work Sans"; font-style:normal; font-weight:300 500; font-display:swap;
  src:url("assets/fonts/worksans-latin-ext.woff2") format("woff2");
  unicode-range:U+0100-02BA,U+1E00-1E9F;
}

/* 一底一墨一色，两个字号：条目名与其余 */
:root{
  --ground:#e6e1d6;
  --ground-2:#dbd5c6;
  --ink:#1b1917;
  --ink-2:#413c34;
  --ink-3:#5f5849;
  --accent:#a16207;
  --accent-ink:#7a4a05;
  --fs-row:clamp(19px,1.7vw,24px);
  --fs-body:16px;
  --pad:clamp(18px,3vw,32px);
  --w:1000px;
  --ease:cubic-bezier(.22,.61,.36,1);
}

*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;overflow-x:hidden}
body{
  margin:0;background:var(--ground);color:var(--ink);overflow-x:hidden;
  font-family:"Work Sans","PingFang SC","Hiragino Sans GB","Microsoft YaHei",system-ui,sans-serif;
  font-size:var(--fs-body);line-height:1.6;font-weight:400;
  -webkit-font-smoothing:antialiased;
}
img{display:block;max-width:100%;height:auto}
a{color:inherit}
h1,h2,p,ol,li{margin:0}
ol{padding:0;list-style:none}
::selection{background:var(--accent);color:#fff}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px}

.wrap{max-width:var(--w);margin:0 auto;padding:0 var(--pad)}

/* ══ 页头 ══════════════════════════════════════════════ */
.top{
  display:flex;justify-content:space-between;align-items:baseline;gap:32px;
  padding:30px 0 0;
}
.top h1{font-size:var(--fs-body);font-weight:400;letter-spacing:0;color:var(--ink)}
.top nav{display:flex;gap:24px}
.top nav a{
  font-size:var(--fs-body);color:var(--ink-2);text-decoration:none;
  transition:color .16s var(--ease);
}
.top nav a:hover{color:var(--accent-ink)}

/* ══ 目录 ══════════════════════════════════════════════ */
.head{padding:74px 0 10px}
.head h2{font-size:var(--fs-body);font-weight:400;color:var(--ink-2)}

.all{
  display:inline-block;margin:34px 0 0 calc(208px + 34px);
  font-size:var(--fs-row);color:var(--accent-ink);text-decoration:none;
  transition:color .16s var(--ease);
}
.all span{display:inline-block;transition:transform .2s var(--ease)}
.all:hover span{transform:translateX(5px)}

.row{
  display:grid;grid-template-columns:208px minmax(0,1fr);
  gap:34px;align-items:center;
  padding:12px 0;text-decoration:none;
}
.row-fig{
  width:208px;aspect-ratio:16/10;object-fit:cover;object-position:top left;
  background:var(--ground-2);
  transition:opacity .18s var(--ease);
}
.row-body{display:flex;flex-direction:column;gap:6px;min-width:0}
.row-t{
  font-size:var(--fs-row);line-height:1.28;letter-spacing:-.008em;color:var(--ink);
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;
  transition:color .16s var(--ease);
}
.row-d{
  font-size:14px;color:var(--ink-3);
  font-variant-numeric:tabular-nums;white-space:nowrap;
}
.row:hover .row-t,.row:focus-visible .row-t{color:var(--accent-ink)}
.row:hover .row-fig{opacity:.82}

/* ══ 页脚 ══════════════════════════════════════════════ */
.foot{
  display:flex;justify-content:space-between;align-items:baseline;gap:24px;flex-wrap:wrap;
  padding:88px 0 44px;font-size:var(--fs-body);color:var(--ink-3);
}
.foot .name{color:var(--ink);letter-spacing:.02em}

/* ══ 入场：脚本生效才隐藏，失败也不会留白 ═════════════════ */
.js [data-rv]{opacity:0;transform:translateY(18px)}
.js [data-rv].in{
  opacity:1;transform:none;
  transition:opacity .5s var(--ease) var(--i,0ms),transform .5s var(--ease) var(--i,0ms);
}

@media (max-width:720px){
  .top{padding-top:22px}
  .head{padding:52px 0 6px}
  .row{
    grid-template-columns:96px minmax(0,1fr);
    gap:16px;align-items:start;padding:15px 0;
  }
  .row-fig{width:96px;aspect-ratio:4/3}
  .all{margin:26px 0 0 calc(96px + 16px);font-size:19px}
  .row-body{gap:4px;padding-top:2px}
  .row-t{font-size:17px;line-height:1.36;-webkit-line-clamp:3}
  .row-d{font-size:14px}
  .foot{padding:64px 0 36px;gap:6px;flex-direction:column}
}

@media (prefers-reduced-motion:reduce){
  .js [data-rv]{opacity:1;transform:none}
  .js [data-rv].in{transition:none}
  *{scroll-behavior:auto}
}
</style>
<script>document.documentElement.className='js';</script>
</head>
<body>
<div class="wrap">

  <header class="top">
    <h1>815 篇 · 21 个工具 · 九类</h1>
    <nav aria-label="主导航">
      <a href="archive.html">档案</a>
      <a href="https://github.com/eastseao/rc">GitHub</a>
    </nav>
  </header>

  <main>
    <div class="head">
      <h2 data-rv>最近写的</h2>
    </div>
    <ol class="list">
${listHTML}
    </ol>
    <a class="all" href="archive.html" data-rv>全部 815 篇 <span aria-hidden="true">→</span></a>
  </main>

  <footer class="foot">
    <span class="name">GERVAS</span>
    <span>杭州 · 自 2023 年 10 月</span>
  </footer>

</div>
<script>
(function(){
  var d = document, els = [].slice.call(d.querySelectorAll('[data-rv]'));
  if (!('IntersectionObserver' in window)) {
    els.forEach(function(el){ el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { rootMargin:'0px 0px -4% 0px', threshold:0.01 });
  els.forEach(function(el){ io.observe(el); });
  /* 兜底：任何情况下内容都不会永久隐形 */
  setTimeout(function(){ els.forEach(function(el){ el.classList.add('in'); }); }, 1400);
})();
</script>
</body>
</html>
`;

fs.writeFileSync('index.html', html, 'utf8');
console.log('rows', rows.length);
rows.forEach(({ w }, i) => console.log((i + 1) + ' ' + w.d + ' ' + w.t.slice(0, 30)));
