---
title: "万能视频下载器 · LinkGrab"
description: "粘贴任意视频链接即下载：抖音/B站/YouTube/TikTok/小红书等数百站点，yt-dlp 引擎，清晰度可选、默认 MP4、实时进度。在线页仅展示界面，完整功能在本机双击 start.bat 启动。"
pubDatetime: 2026-10-07
category: "建站与技术"
kind: "工具"
tags: ["视频下载", "yt-dlp", "本地工具"]
---

<style>
.rc-tool{
    --bg:#f7f8fa; --card:#ffffff; --line:#dfe6ef; --ink:#0f172a;
    --muted:#64748b; --accent:#0d9488; --accent-soft:#e3f5f2;
    --danger:#b91c1c; --warn:#b45309; --warn-soft:#fdf3e3; --radius:8px;
  }.rc-tool *{box-sizing:border-box;margin:0;padding:0}.rc-tool{background:var(--bg);color:var(--ink);font-family:var(--sans);min-height:100vh;padding:36px 16px 70px}.rc-tool .wrap{max-width:720px;margin:0 auto}.rc-tool header{display:flex;align-items:center;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:10px}.rc-tool .logo{display:flex;align-items:center;gap:12px}.rc-tool .logo-badge{width:40px;height:40px;border-radius:9px;background:linear-gradient(135deg,#14b8a6,#0d9488);display:flex;align-items:center;justify-content:center;font-size:19px;color:#fff;font-weight:800}.rc-tool .logo h1{font-size:18px;font-weight:700}.rc-tool .logo p{font-size:12px;color:var(--muted);margin-top:2px}.rc-tool .badge{font-size:12px;padding:5px 11px;border-radius:999px;border:1px solid var(--line);color:var(--muted)}.rc-tool .badge.on{color:var(--accent);border-color:var(--accent);background:var(--accent-soft)}.rc-tool .online-banner{display:none;background:var(--warn-soft);border:1px solid #fcd9a8;border-radius:var(--radius);padding:14px 16px;margin-bottom:16px;font-size:13.5px;line-height:1.7;color:#7c4a12}.rc-tool .online-banner b{color:var(--warn)}.rc-tool .online-banner ol{margin:8px 0 0 20px}.rc-tool .online-banner code{background:#fff;padding:1px 6px;border-radius:4px;font-family:var(--mono);font-size:12px;border:1px solid var(--line)}.rc-tool .card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:20px}.rc-tool .card + .card{margin-top:14px}.rc-tool .card h2{font-size:14px;color:var(--muted);font-weight:500;margin-bottom:12px}.rc-tool .input-row{display:flex;gap:10px}.rc-tool #url{flex:1;background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:12px 15px;font-size:15px;outline:none;transition:border-color .15s;color:var(--ink)}.rc-tool #url:focus{border-color:var(--accent)}.rc-tool #url::placeholder{color:#94a3b8}.rc-tool .btn{border:none;border-radius:var(--radius);padding:12px 20px;font-size:14.5px;font-weight:600;cursor:pointer;transition:opacity .15s,transform .05s;font-family:inherit}.rc-tool .btn:active{transform:scale(.97)}.rc-tool .btn:disabled{opacity:.5;cursor:not-allowed}.rc-tool .btn-primary{background:var(--accent);color:#fff}.rc-tool .btn-primary:hover{background:#0f766e}.rc-tool .platforms{display:flex;flex-wrap:wrap;gap:7px;margin-top:13px}.rc-tool .chip{font-size:12px;padding:3px 9px;border-radius:999px;background:#f1f5f9;border:1px solid var(--line);color:var(--muted)}.rc-tool .chip.hit{border-color:var(--accent);color:var(--accent);background:var(--accent-soft)}.rc-tool .result{display:none}.rc-tool .video-row{display:flex;gap:14px}.rc-tool .thumb{width:160px;height:90px;object-fit:cover;border-radius:6px;background:#f1f5f9;flex-shrink:0;border:1px solid var(--line)}.rc-tool .vtitle{font-size:15px;font-weight:600;line-height:1.45;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}.rc-tool .vmeta{display:flex;align-items:center;gap:8px;margin-top:7px;font-size:12.5px;color:var(--muted);flex-wrap:wrap}.rc-tool .ptag{padding:2px 8px;border-radius:5px;font-weight:600}.rc-tool .opt-label{font-size:12.5px;color:var(--muted);margin:15px 0 8px}.rc-tool .opt-row{display:flex;flex-wrap:wrap;gap:8px}.rc-tool .opt{border:1px solid var(--line);background:#fff;color:var(--ink);border-radius:6px;padding:7px 13px;font-size:13.5px;cursor:pointer;transition:all .12s;font-family:inherit}.rc-tool .opt:hover{border-color:var(--accent)}.rc-tool .opt.active{background:var(--accent-soft);border-color:var(--accent);color:var(--accent);font-weight:600}.rc-tool .opt:disabled{opacity:.35;cursor:not-allowed}.rc-tool .dl-row{margin-top:16px}.rc-tool .btn-download{width:100%;padding:13px;background:var(--accent);color:#fff;font-size:15px}.rc-tool .progress-box{display:none}.rc-tool .p-top{display:flex;justify-content:space-between;font-size:13px;margin-bottom:9px}.rc-tool .bar{height:8px;background:#eef1f5;border-radius:999px;overflow:hidden}.rc-tool .bar>div{height:100%;width:0%;background:linear-gradient(90deg,#14b8a6,#0d9488);transition:width .3s;border-radius:999px}.rc-tool .p-status{margin-top:9px;font-size:13px}.rc-tool .p-status.err{color:var(--danger)}.rc-tool .p-status.ok{color:var(--accent)}.rc-tool .files h3{font-size:13px;color:var(--muted);font-weight:600;margin-bottom:9px}.rc-tool .file-row{display:flex;align-items:center;gap:11px;background:#fff;border:1px solid var(--line);border-radius:6px;padding:10px 13px;margin-bottom:7px}.rc-tool .file-name{flex:1;min-width:0;font-size:13px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.rc-tool .file-size{font-size:12px;color:var(--muted);white-space:nowrap}.rc-tool .file-dl{font-size:12.5px;color:var(--accent);text-decoration:none;white-space:nowrap}.rc-tool .file-dl:hover{text-decoration:underline}.rc-tool .empty{color:var(--muted);font-size:13px}.rc-tool footer{margin-top:26px;font-size:12px;color:var(--muted);line-height:1.7}.rc-tool .toast{position:fixed;top:18px;left:50%;transform:translateX(-50%);background:#0f172a;color:#f1f5f9;padding:10px 18px;border-radius:8px;font-size:13px;opacity:0;transition:opacity .2s;pointer-events:none;z-index:99}.rc-tool .toast.show{opacity:1}.rc-tool .spinner{display:inline-block;width:13px;height:13px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:sp .7s linear infinite;vertical-align:-2px;margin-right:6px}
  @keyframes sp{to{transform:rotate(360deg)}}
  @media (max-width:560px){.video-row{flex-direction:column}.thumb{width:100%;height:auto;aspect-ratio:16/9}.input-row{flex-direction:column}}

</style>

<div class="rc-tool"><div class="wrap"><header><div class="logo"><div class="logo-badge">⬇</div><div><h1>视频下载器 · LinkGrab</h1><p>粘贴链接 → 选清晰度 → 默认下载 MP4</p></div></div><span class="badge" id="modeBadge">检测中…</span></header><div class="online-banner" id="onlineBanner"><b>⚠ 本工具为本地运行软件</b>——当前你在 gervas.wang 在线页，后端解析/下载无法在网页上运行。完整功能需在本机启动：<ol><li>下载本仓库（或整个<code>tools/video-downloader/</code>目录）到本地；</li><li>已装 Python 后双击<code>install.bat</code>（装 yt-dlp），再双击<code>start.bat</code>；</li><li>浏览器打开<code>http://127.0.0.1:8765</code>，在本地页面粘贴链接即可下载。</li></ol></div><div class="card"><h2>粘贴任意视频链接，自动识别平台</h2><div class="input-row"><input id="url" type="text" placeholder="https://www.douyin.com/video/xxxx …" autocomplete="off"></div><div class="platforms" id="platforms"></div></div><div class="result" id="result"><div class="card"><div class="video-row"><img class="thumb" id="thumb" alt></div><div class="opt-label">清晰度</div><div class="opt-row" id="tierRow"></div><div class="opt-label">格式（默认 MP4）</div><div class="opt-row" id="fmtRow"></div><div class="dl-row"><button class="btn btn-download" id="dlBtn">⬇ 开始下载</button></div></div></div><div class="progress-box card" id="progressBox"><div class="p-top"><span id="pStage">排队中…</span><span id="pPct">0%</span></div><div class="bar"><div id="pBar"></div></div><div class="p-status" id="pStatus"></div></div><div class="files"><h3>本机已下载</h3><div id="fileList"><div class="empty">还没有文件。</div></div></div><footer>基于 yt-dlp + FFmpeg 的本地下载引擎，支持抖音 / 哔哩哔哩 / YouTube / TikTok / Instagram / X / 小红书 / 快手等数百站点。<br></footer></div><div class="toast" id="toast"></div><script>
const PLATFORMS = [
  { re:/youtube\.com|youtu\.be/, name:"YouTube", color:"#dc2626" },
  { re:/douyin\.com|iesdouyin\.com/, name:"抖音", color:"#e11d48" },
  { re:/bilibili\.com|b23\.tv/, name:"哔哩哔哩", color:"#db2777" },
  { re:/weibo\.com/, name:"微博", color:"#dc2626" },
  { re:/xiaohongshu\.com|xhslink\.com/, name:"小红书", color:"#e11d48" },
  { re:/tiktok\.com/, name:"TikTok", color:"#0f766e" },
  { re:/instagram\.com/, name:"Instagram", color:"#c026d3" },
  { re:/twitter\.com|x\.com/, name:"X / Twitter", color:"#475569" },
  { re:/reddit\.com/, name:"Reddit", color:"#ea580c" },
  { re:/pinterest\.com/, name:"Pinterest", color:"#dc2626" },
  { re:/kuaishou\.com/, name:"快手", color:"#ea580c" },
  { re:/qq\.com|weixin|wechat/, name:"微信 / QQ", color:"#16a34a" },
];
const $=id=>document.getElementById(id);
let state={url:"",info:null,tier:"best",fmt:"mp4",taskId:null,poller:null,LOCAL:false};

function detectPlatform(u){for(const p of PLATFORMS) if(p.re.test(u)) return p; return {name:"其他平台",color:"#64748b"}}
function renderPlatforms(u){
  const hit=detectPlatform(u);
  $("platforms").innerHTML=PLATFORMS.map(p=>`<span class="chip${u&&p===hit?' hit':''}">${p.name}</span>`).join("");
}
$("url").addEventListener("input",e=>renderPlatforms(e.target.value.trim()));

async function probe(){
  try{
    const ctl=new AbortController(); setTimeout(()=>ctl.abort(),3000);
    const r=await fetch("/api/files",{cache:"no-store",signal:ctl.signal});
    state.LOCAL=r.ok;
  }catch(e){ state.LOCAL=false; }
  applyMode();
  if(state.LOCAL) refreshFiles();
}
function applyMode(){
  const on=state.LOCAL;
  $("onlineBanner").style.display=on?"none":"block";
  $("modeBadge").textContent=on?"● 本地已连接":"○ 在线只读";
  $("modeBadge").classList.toggle("on",on);
  ["url","parseBtn","dlBtn"].forEach(id=>$(id).disabled=!on);
}

$("parseBtn").addEventListener("click",parse);
$("url").addEventListener("keydown",e=>{if(e.key==="Enter")parse()});
async function parse(){
  const url=$("url").value.trim();
  if(!url) return toast("请先粘贴一个链接");
  const btn=$("parseBtn"); btn.disabled=true; btn.innerHTML='<span class="spinner"></span>解析中…';
  try{
    const r=await fetch("/api/info",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({url})});
    const d=await r.json();
    if(!d.ok) throw new Error(d.error||"解析失败");
    showResult(d.info,url);
  }catch(e){ toast("解析失败："+e.message); }
  finally{ btn.disabled=false; btn.textContent="解析视频"; }
}
function showResult(info,url){
  state.url=url; state.info=info; state.tier="best"; state.fmt="mp4";
  $("result").style.display="block";
  $("thumb").src=info.thumbnail||""; $("thumb").style.display=info.thumbnail?"":"none";
  $("vTitle").textContent=info.title;
  const p=detectPlatform(info.webpage_url||url);
  const tag=$("vPlat"); tag.textContent=p.name; tag.style.background=p.color+"1a"; tag.style.color=p.color;
  $("vUploader").textContent=info.uploader||"";
  $("vDur").textContent=info.duration?"时长 "+fmtDur(info.duration):"";
  $("tierRow").innerHTML=info.tiers.map(t=>`<button class="opt${t.key==="best"?" active":""}" data-tier="${t.key}">${t.label}</button>`).join("");
  $("fmtRow").innerHTML=[["mp4","MP4（默认）"],["m4a","M4A 音频"],["mp3","MP3 音频"]].map(([k,l])=>
    `<button class="opt${k==="mp4"?" active":""}" data-fmt="${k}"${k==="mp3"&&!info.ffmpeg?" disabled title='需要 FFmpeg'":""}>${l}</button>`).join("");
  document.querySelectorAll("#tierRow .opt").forEach(b=>b.onclick=()=>{document.querySelectorAll("#tierRow .opt").forEach(x=>x.classList.remove("active"));b.classList.add("active");state.tier=b.dataset.tier});
  document.querySelectorAll("#fmtRow .opt").forEach(b=>b.onclick=()=>{if(b.disabled)return;document.querySelectorAll("#fmtRow .opt").forEach(x=>x.classList.remove("active"));b.classList.add("active");state.fmt=b.dataset.fmt});
}
$("dlBtn").addEventListener("click",async()=>{
  if(!state.url)return;
  const btn=$("dlBtn"); btn.disabled=true; btn.textContent="已加入队列…";
  try{
    const r=await fetch("/api/download",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({url:state.url,tier:state.tier,format:state.fmt})});
    const d=await r.json();
    if(!d.ok) throw new Error(d.error||"启动失败");
    state.taskId=d.task.id; $("progressBox").style.display="block";
    $("pStage").textContent="排队中…"; $("pPct").textContent="0%"; $("pBar").style.width="0%";
    $("pStatus").textContent=""; $("pStatus").className="p-status";
    startPolling();
  }catch(e){ toast("启动失败："+e.message); btn.disabled=false; btn.textContent="⬇ 开始下载"; }
});
function startPolling(){
  if(state.poller)clearInterval(state.poller);
  state.poller=setInterval(async()=>{
    if(!state.taskId)return;
    try{
      const r=await fetch("/api/progress",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({id:state.taskId})});
      const d=await r.json(); const t=d.task;
      $("pStage").textContent=t.stage||t.status;
      $("pPct").textContent=(t.percent||0).toFixed(0)+"%";
      $("pBar").style.width=(t.percent||0)+"%";
      if(t.status==="done"){ clearInterval(state.poller); state.poller=null;
        $("pStatus").className="p-status ok"; $("pStatus").textContent="✅ 完成："+(t.filename||"");
        $("dlBtn").disabled=false; $("dlBtn").textContent="⬇ 开始下载"; refreshFiles();
      }else if(t.status==="error"){ clearInterval(state.poller); state.poller=null;
        $("pStatus").className="p-status err"; $("pStatus").textContent="❌ 失败："+(t.error||"");
        $("dlBtn").disabled=false; $("dlBtn").textContent="⬇ 重新下载";
      }
    }catch(e){}
  },800);
}
async function refreshFiles(){
  try{
    const r=await fetch("/api/files"); const d=await r.json();
    const list=d.files||[];
    $("fileList").innerHTML=list.length?list.map(f=>`
      <div class="file-row"><span>🎬</span>
      <span class="file-name" title="${esc(f.name)}">${esc(f.name)}</span>
      <span class="file-size">${fmtSize(f.size)}</span>
      <a class="file-dl" href="${f.url}" download>下载</a></div>`).join("")
      :'<div class="empty">还没有文件。</div>';
  }catch(e){}
}
function fmtDur(s){s=Math.round(s);const h=Math.floor(s/3600),m=Math.floor(s%3600/60),x=s%60;return h?`${h}:${String(m).padStart(2,"0")}:${String(x).padStart(2,"0")}`:`${m}:${String(x).padStart(2,"0")}`}
function fmtSize(b){if(!b)return"0 B";const u=["B","KB","MB","GB"];let i=0;while(b>=1024&&i<u.length-1){b/=1024;i++}return b.toFixed(1)+" "+u[i]}
function esc(s){return s.replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}
let tt; function toast(m){const t=$("toast");t.textContent=m;t.classList.add("show");clearTimeout(tt);tt=setTimeout(()=>t.classList.remove("show"),3200)}
probe(); refreshFiles(); setInterval(()=>{if(!state.poller&&state.LOCAL)refreshFiles()},15000);
</script></div>
