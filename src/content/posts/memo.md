---
title: "备忘录"
description: "随手记下的备忘录：粘贴即存卡片，支持搜索、复制、编辑与删除，数据保存在 pages/memo.json。"
pubDatetime: 2026-09-29
category: "建站与技术"
kind: "工具"
tags: ["备忘录", "本地工具"]
---

<style>
.rc-tool *{ box-sizing: border-box; margin: 0; padding: 0; }.rc-tool{ scroll-behavior: smooth; }.rc-tool{
    font-family: var(--sans); background: var(--bg); color: var(--ink);
    font-size: 14px; line-height: 1.65; min-height: 100vh; -webkit-font-smoothing: antialiased;
  }.rc-tool a{ color: inherit; text-decoration: none; }:focus-visible{ outline: 2px solid var(--accent-ink); outline-offset: 2px; }.rc-tool /* ── 顶栏（墨黑，与全站一致） ── */
  .topbar{
    position: sticky; top: 0; z-index: 50;
    background: #0f172a; border-bottom: 1px solid transparent;
    padding: 9px 32px; display: flex; align-items: center; gap: 14px; flex-wrap: wrap;
  }.rc-tool .brand{ display: flex; align-items: baseline; gap: 8px; white-space: nowrap; }.rc-tool .site-home{ font-family: var(--mono); font-size: 14px; font-weight: 600; letter-spacing: .04em; color: #fff; }.rc-tool .site-home:hover{ color: #5eead4; }.rc-tool .crumb-sep{ color: #64748b; font-size: 13px; }.rc-tool .brand-name{ font-size: 14px; font-weight: 600; color: #f1f5f9; }.rc-tool .brand-count{ font-family: var(--mono); font-size: 11px; color: #94a3b8; font-variant-numeric: tabular-nums; }.rc-tool .search-wrap{ flex: 1 1 240px; max-width: 460px; position: relative; }.rc-tool .search-wrap svg{ position: absolute; left: 11px; top: 50%; transform: translateY(-50%); width: 15px; height: 15px; color: #94a3b8; pointer-events: none; }.rc-tool #search{
    width: 100%; padding: 8px 46px 8px 32px; background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.14); border-radius: 3px;
    font-size: 13.5px; font-family: inherit; color: #f1f5f9; outline: none;
    transition: border-color .15s, background .15s;
  }.rc-tool #search::placeholder{ color: #94a3b8; }.rc-tool #search:focus{ border-color: var(--accent); background: rgba(255,255,255,.13); }.rc-tool kbd{
    position: absolute; right: 8px; top: 50%; transform: translateY(-50%);
    font-family: var(--mono); font-size: 10px; color: #94a3b8;
    border: 1px solid rgba(255,255,255,.16); border-radius: 3px; padding: 1px 5px;
    background: transparent; pointer-events: none;
  }.rc-tool #search:focus + kbd{ opacity: 0; }.rc-tool .top-actions{ display: flex; gap: 8px; align-items: center; margin-inline-start: auto; }.rc-tool .btn{
    padding: 7px 13px; border-radius: 3px; border: 1px solid var(--border);
    background: var(--surface); color: var(--ink); font-size: 13px; font-family: inherit;
    cursor: pointer; transition: background .15s, border-color .15s; font-weight: 500; white-space: nowrap;
  }.rc-tool .btn:hover{ background: var(--code); border-color: var(--muted); }.rc-tool .btn-dark{ background: var(--accent); border-color: var(--accent); color: #fff; }.rc-tool .btn-dark:hover{ background: var(--accent-ink); border-color: var(--accent-ink); }.rc-tool .btn-dark:disabled{ opacity: .45; cursor: default; }.rc-tool .icon-btn{
    width: 32px; height: 32px; border-radius: 3px; border: 1px solid var(--border);
    background: var(--surface); display: inline-flex; align-items: center; justify-content: center;
    cursor: pointer; color: var(--muted); transition: background .15s, color .15s;
  }.rc-tool .icon-btn:hover{ background: var(--code); color: var(--ink); }.rc-tool select.btn{ padding: 7px 8px; }.rc-tool .topbar .btn, .rc-tool .topbar .icon-btn{
    background: rgba(255,255,255,.08); border-color: rgba(255,255,255,.16); color: #e2e8f0;
  }.rc-tool .topbar .btn:hover, .rc-tool .topbar .icon-btn:hover{ background: rgba(255,255,255,.16); color: #fff; }.rc-tool .topbar .btn-dark{ background: var(--accent); border-color: var(--accent); color: #fff; }.rc-tool .topbar .btn-dark:hover{ background: #0f766e; border-color: #0f766e; }.rc-tool .topbar select.btn option{ color: var(--ink); background: var(--surface); }.rc-tool /* ── 顶部分类筛选条 ── */
  .catbar{ position: sticky; top: var(--bar-h, 53px); z-index: 49; background: var(--surface); border-bottom: 1px solid var(--border); }.rc-tool .catbar-in{ max-width: var(--maxw); margin: 0 auto; display: flex; align-items: center; gap: 12px; padding-inline: 32px; }.rc-tool .catbar-lab{ font-family: var(--mono); font-size: 10.5px; text-transform: uppercase; letter-spacing: .09em; color: var(--muted); white-space: nowrap; padding-block: 10px; }.rc-tool #catNav{ display: flex; flex-direction: row; flex-wrap: wrap; gap: 1px; min-width: 0; }.rc-tool .cat-chip{
    display: inline-flex; align-items: center; gap: 7px; width: auto; flex: 0 0 auto;
    padding: 10px 11px; border: 0; border-bottom: 2px solid transparent;
    background: transparent; color: var(--ink); font-size: 13px; font-family: inherit;
    cursor: pointer; transition: background .12s; line-height: 1.5; white-space: nowrap;
  }.rc-tool .cat-chip:hover{ background: var(--code); }.rc-tool .cat-chip.active{ font-weight: 600; border-bottom-color: var(--accent); background: var(--code); }.rc-tool .cat-dot{ width: 7px; height: 7px; border-radius: 50%; flex: 0 0 auto; }.rc-tool .cat-n{ font-family: var(--mono); font-size: 10.5px; color: var(--muted); font-variant-numeric: tabular-nums; }.rc-tool /* ── 两栏布局：正文 + 右侧说明 ── */
  .layout{ display: grid; grid-template-columns: minmax(0,1fr) 224px; max-width: var(--maxw-read); margin: 0 auto; min-height: calc(100vh - 53px); }.rc-tool main{ padding: 30px 40px 90px; max-width: var(--maxw-read); }.rc-tool .toolbar{ display: flex; align-items: center; justify-content: space-between; gap: 14px; margin-bottom: 16px; }.rc-tool .result-info{ font-family: var(--mono); font-size: 11.5px; color: var(--muted); letter-spacing: .03em; }.rc-tool .result-info b{ color: var(--ink); font-weight: 600; }.rc-tool .grid{ display: grid; grid-template-columns: 1fr; }.rc-tool .card{
    background: transparent; border: 0; border-bottom: 1px solid var(--border);
    border-radius: 0; padding: 20px 2px; display: flex; flex-direction: column; gap: 10px;
  }.rc-tool .card-top{ display: flex; align-items: flex-start; gap: 10px; }.rc-tool .card h3{ font-size: 16.5px; font-weight: 600; line-height: 1.45; flex: 1; cursor: pointer; word-break: break-word; }.rc-tool .card h3:hover{ color: var(--accent-ink); }.rc-tool .star{
    background: none; border: 0; cursor: pointer; font-size: 15px; line-height: 1;
    padding: 2px; color: var(--muted); transition: color .15s; flex: 0 0 auto; font-family: inherit;
  }.rc-tool .star:hover{ color: var(--accent); }.rc-tool .star.on{ color: var(--accent); }.rc-tool .card-body{
    font-family: var(--mono); font-size: 12.5px; line-height: 1.75; color: var(--ink);
    background: var(--code); border: 1px solid var(--border); border-radius: 3px;
    padding: 12px 14px; max-height: 120px; overflow: hidden; position: relative;
    white-space: pre-wrap; word-break: break-word; cursor: pointer;
  }.rc-tool .card-body::after{ content: ""; position: absolute; inset: auto 0 0 0; height: 30px; background: linear-gradient(transparent, var(--code)); }.rc-tool .card-foot{ display: flex; align-items: center; gap: 7px; flex-wrap: wrap; }.rc-tool .cat-tag{ display: inline-flex; align-items: center; gap: 5px; padding: 2px 8px; border-radius: 3px; font-size: 11px; font-weight: 550; font-family: var(--mono); }.rc-tool .tag-chip{ padding: 2px 7px; border-radius: 3px; font-size: 11px; color: var(--muted); background: var(--code); border: 1px solid var(--border); }.rc-tool .card-date{ margin-inline-start: auto; font-family: var(--mono); font-size: 10.5px; color: var(--muted); }.rc-tool .card-actions{ display: flex; gap: 6px; }.rc-tool .card-actions .btn{ padding: 4px 11px; font-size: 11.5px; }.rc-tool /* 空 / 加载更多 */
  .empty{ grid-column: 1/-1; text-align: center; padding: 80px 20px; color: var(--muted); border: 1px dashed var(--border); }.rc-tool .empty-icon{ font-size: 30px; margin-bottom: 10px; opacity: .6; }.rc-tool .empty-title{ font-size: 14px; color: var(--ink); margin-bottom: 4px; }.rc-tool .empty-sub{ font-size: 12.5px; }.rc-tool .skeleton{ grid-column: 1/-1; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 12px; }.rc-tool .sk{
    height: 150px; border-radius: 3px; border: 1px solid var(--border);
    background: linear-gradient(90deg, #f0ede6 25%, #e9e5dc 50%, #f0ede6 75%);
    background-size: 200% 100%; animation: shimmer 1.4s infinite;
  }
  @keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }.rc-tool .load-more{ grid-column: 1/-1; display: flex; justify-content: center; padding: 26px 0 6px; }.rc-tool /* 右侧使用说明 */
  .toc{
    padding: 30px 18px 32px; border-inline-start: 1px solid var(--border);
    position: sticky; top: 53px; align-self: start; max-height: calc(100vh - 53px); overflow: auto; font-size: 12.5px;
  }.rc-tool .toc-label{ font-family: var(--mono); font-size: 10.5px; text-transform: uppercase; letter-spacing: .09em; color: var(--muted); margin: 18px 0 8px; }.rc-tool .toc-label:first-child{ margin-top: 0; }.rc-tool .help{ color: var(--muted); line-height: 1.7; }.rc-tool .help code{ font-family: var(--mono); font-size: 11px; background: var(--code); border: 1px solid var(--border); border-radius: 3px; padding: 0 4px; }.rc-tool .h-row{ display: flex; align-items: center; gap: 8px; padding: 3px 0; }.rc-tool .h-k{ font-family: var(--mono); font-size: 10.5px; border: 1px solid var(--border); border-radius: 3px; padding: 1px 6px; background: var(--code); color: var(--ink); white-space: nowrap; }.rc-tool .toc-home{ display: block; margin-top: 22px; padding-top: 14px; border-top: 1px solid var(--border); color: var(--ink); }.rc-tool .toc-home:hover{ color: var(--accent-ink); }.rc-tool /* 弹窗 */
  .mask{ position: fixed; inset: 0; background: rgba(28,27,26,.35); display: none; align-items: center; justify-content: center; z-index: 100; padding: 20px; }.rc-tool .mask.show{ display: flex; }.rc-tool .modal{
    background: var(--surface); border: 1px solid var(--ink); border-radius: 4px;
    width: 100%; max-width: 620px; max-height: 88vh; overflow-y: auto;
    padding: 24px 26px; display: flex; flex-direction: column; gap: 14px;
    box-shadow: 0 12px 40px rgba(28,27,26,.18);
  }.rc-tool .modal h2{ font-size: 16px; font-weight: 600; }.rc-tool .modal label{ font-size: 12px; color: var(--muted); display: block; margin-bottom: 5px; }.rc-tool .modal input[type=text], .rc-tool .modal textarea, .rc-tool .modal input[type=password]{
    width: 100%; background: var(--bg); border: 1px solid var(--border); border-radius: 3px;
    color: var(--ink); padding: 9px 12px; font-size: 13.5px; outline: none; font-family: inherit;
    transition: border-color .15s;
  }.rc-tool .modal textarea{ min-height: 200px; resize: vertical; font-family: var(--mono); font-size: 12.5px; line-height: 1.7; }.rc-tool .modal input:focus, .rc-tool .modal textarea:focus{ border-color: var(--accent); }.rc-tool .row2{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }.rc-tool .modal-foot{ display: flex; gap: 8px; justify-content: flex-end; align-items: center; margin-top: 2px; }.rc-tool .hint{ font-size: 11.5px; color: var(--muted); line-height: 1.6; }.rc-tool .modal-foot .hint{ margin-inline-end: auto; }.rc-tool .view-body{
    background: var(--code); border: 1px solid var(--border); border-radius: 3px;
    padding: 14px 16px; font-family: var(--mono); font-size: 12.5px; line-height: 1.75;
    white-space: pre-wrap; word-break: break-word; max-height: 52vh; overflow-y: auto;
  }.rc-tool .meta-row{ display: flex; align-items: center; gap: 7px; flex-wrap: wrap; }.rc-tool /* Toast */
  #toast{
    position: fixed; bottom: 70px; left: 50%;
    transform: translateX(-50%) translateY(70px);
    background: var(--ink); color: #faf9f7; border: 1px solid var(--ink);
    padding: 9px 18px; border-radius: 3px; font-size: 13px;
    transition: .25s; z-index: 200; opacity: 0; pointer-events: none;
  }.rc-tool #toast.show{ transform: translateX(-50%) translateY(0); opacity: 1; }.rc-tool #toast.err{ background: #8a2b1a; border-color: #8a2b1a; }.rc-tool /* 响应式 */
  @media (max-width: 1120px){
    .layout { grid-template-columns: minmax(0,1fr); }
    .toc { display: none; }
  }
  @media (max-width: 860px) {
    .layout { grid-template-columns: 1fr; }
    .catbar { position: static; }
    .catbar-lab { display: none; }
    .catbar-in { padding-inline: 14px; }
    #catNav { flex-wrap: nowrap; overflow-x: auto; scrollbar-width: none; }
    #catNav::-webkit-scrollbar { display: none; }
    main { padding: 20px 18px 80px; }
    .topbar { padding: 10px 14px; }
    .search-wrap { order: 5; flex-basis: 100%; max-width: none; }
    .row2 { grid-template-columns: 1fr; }
  }

</style>

<div class="rc-tool"><div class="catbar"><div class="catbar-in"><span class="catbar-lab">分类</span><div id="catNav" role="tablist" aria-label="按分类筛选"></div></div></div><div class="layout"><main><div class="toolbar"><div class="result-info" id="resultInfo"></div></div><div class="grid" id="grid"><div class="skeleton"><div class="sk"></div><div class="sk"></div><div class="sk"></div><div class="sk"></div><div class="sk"></div><div class="sk"></div></div></div></main><aside class="toc" aria-label="使用说明"><div class="toc-label">快捷键</div><div class="help"><div class="h-row"><span class="h-k">Ctrl K</span><span>聚焦搜索</span></div><div class="h-row"><span class="h-k">Ctrl ⏎</span><span>保存编辑中的备忘录</span></div><div class="h-row"><span class="h-k">Esc</span><span>关闭弹窗</span></div></div><div class="toc-label">数据</div><div class="help">数据源为仓库<code>eastseao/rc</code>的<code>pages/memo.json</code>，每次改动都会以独立提交同步到 GitHub，可追溯。 添加 / 编辑 / 删除 / 收藏需先在右上角配置写入令牌；令牌只保存在当前浏览器，不会上传到任何服务器。</div><a class="toc-home" href="../video-downloader/">← 返回 日常 · 首页</a></aside></div><div class="mask" id="editMask"><div class="modal"><h2 id="editTitle">添加备忘录</h2><div><label>标题 *</label><input type="text" id="f_title" placeholder="给这条备忘录起个名字" maxlength="200"></div><div class="row2"><div><label>分类</label><input type="text" id="f_category" placeholder="如：工作 / 生活" maxlength="50" list="catList"></div><div><label>标签（逗号分隔）</label><input type="text" id="f_tags" placeholder="如：灵感, 待办" maxlength="200"></div></div><div><label>内容 *</label><textarea id="f_content" placeholder="把重要的文案粘贴到这里…"></textarea></div><p class="hint">保存后会直接提交到 GitHub 仓库 eastseao/rc 的 pages/memo.json</p><div class="modal-foot"><span class="hint">Ctrl + Enter 保存</span><button class="btn" onclick="closeEditor()">取消</button><button class="btn btn-dark" id="saveBtn" onclick="saveMemo()">保存</button></div></div></div><div class="mask" id="viewMask"><div class="modal"><div style="display:flex;align-items:center;gap:10px;"><h2 id="v_title" style="flex:1;"></h2><button class="star" id="v_star" onclick="toggleFavView()">☆</button></div><div class="meta-row" id="v_meta"></div><div class="view-body" id="v_content"></div><div class="modal-foot"><button class="btn" onclick="closeView()">关闭</button><button class="btn" onclick="copyView()">复制</button><button class="btn btn-dark" onclick="editFromView()">编辑</button></div></div></div><div class="mask" id="tokenMask"><div class="modal" style="max-width:480px;"><h2>写入令牌</h2><p class="hint">添加 / 编辑 / 删除需要 GitHub 写入权限。令牌只保存在当前浏览器，不会上传到任何服务器。</p><div><label>GitHub Fine-grained Token</label><input type="password" id="tokenInput" placeholder="github_pat_…" autocomplete="off"></div><ol class="hint" style="padding-left:18px;"><li>打开 github.com/settings/personal-access-tokens/new</li><li>Repository access → Only select repositories →<b>rc</b></li><li>Permissions → Contents →<b>Read and write</b></li><li>生成后粘贴到上方保存</li></ol><div class="modal-foot"><button class="btn" onclick="clearToken()">清除</button><button class="btn btn-dark" onclick="saveToken()">保存</button></div></div></div><div id="toast"></div><script>
const REPO = 'eastseao/rc', BRANCH = 'main', FILE = 'pages/memo.json';
const TOKEN_KEY = 'gh_memo_token';
const PAGE = 60;

const CAT_COLOR = {
  '润色': '#b45309', '办公': '#2563eb', '写作': '#7c3aed',
  '数据文件': '#0891b2', '编程': '#059669', '学习': '#db2777',
  '汇报': '#ea580c', '效率': '#4f46e5', '自动化': '#65a30d',
  '通用': '#64748b', '未分类': '#9aa0ae',
};

let memos = [], fileSha = null, currentViewId = null, editingId = null;
let activeCat = '全部', shown = PAGE;

const $ = id => document.getElementById(id);
const catColor = c => CAT_COLOR[c] || CAT_COLOR['未分类'];

function getToken() { return localStorage.getItem(TOKEN_KEY) || ''; }
function b64ToUtf8(b64) {
  const bin = atob(b64.replace(/\s/g, ''));
  return new TextDecoder().decode(Uint8Array.from(bin, c => c.charCodeAt(0)));
}
function utf8ToB64(s) {
  const b = new TextEncoder().encode(s);
  let bin = ''; b.forEach(x => bin += String.fromCharCode(x));
  return btoa(bin);
}
async function api(path, opts = {}) {
  const headers = { 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', ...(opts.headers || {}) };
  const t = getToken();
  if (t) headers['Authorization'] = 'Bearer ' + t;
  return fetch('https://api.github.com' + path, { ...opts, headers });
}

async function load() {
  try {
    let data;
    try {
      const r = await fetch('https://raw.githubusercontent.com/' + REPO + '/' + BRANCH + '/' + FILE + '?_=' + Date.now());
      if (!r.ok) throw new Error('raw ' + r.status);
      data = JSON.parse(await r.text());
    } catch (e1) {
      const r = await api('/repos/' + REPO + '/contents/' + FILE + '?ref=' + BRANCH + '&_=' + Date.now());
      if (r.status === 404) data = { memos: [] };
      else {
        if (!r.ok) throw new Error('GitHub ' + r.status);
        const j = await r.json(); fileSha = j.sha;
        data = JSON.parse(b64ToUtf8(j.content));
      }
    }
    memos = data.memos || [];
    renderNav(); render();
  } catch (e) {
    const tip = /403|429/.test(e.message) ? '（API 限流，可在右上角配置令牌）' : '';
    $('grid').innerHTML = '<div class="empty"><div class="empty-icon">⚠️</div>' +
      '<div class="empty-title">加载失败</div>' +
      '<div class="empty-sub">' + esc(e.message) + tip + '</div></div>';
  }
}

async function fetchLatest() {
  const r = await api('/repos/' + REPO + '/contents/' + FILE + '?ref=' + BRANCH);
  if (r.status === 404) return { data: { memos: [] }, sha: null };
  if (!r.ok) throw new Error('GitHub ' + r.status);
  const j = await r.json();
  return { data: JSON.parse(b64ToUtf8(j.content)), sha: j.sha };
}
async function putFile(data, sha, message) {
  const r = await api('/repos/' + REPO + '/contents/' + FILE, {
    method: 'PUT', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message, content: utf8ToB64(JSON.stringify(data, null, 2)),
      branch: BRANCH, ...(sha ? { sha: sha } : {})
    })
  });
  if (!r.ok) throw new Error('GitHub ' + r.status);
  const j = await r.json(); fileSha = j.content.sha; return j;
}

function renderNav() {
  const cnt = {};
  memos.forEach(m => { const c = m.category || '未分类'; cnt[c] = (cnt[c] || 0) + 1; });
  const rest = Object.keys(cnt).filter(c => c !== '润色').sort((a, b) => cnt[b] - cnt[a]);
  const cats = ['全部', ...(cnt['润色'] ? ['润色'] : []), ...rest];

  $('catNav').innerHTML = cats.map(c => {
    const n = c === '全部' ? memos.length : cnt[c];
    const active = c === activeCat ? ' active' : '';
    const dot = c === '全部' ? '' : '<span class="cat-dot" style="background:' + catColor(c) + '"></span>';
    return '<button class="cat-chip' + active + '" onclick="setCat(\'' + esc(c) + '\')">' +
           dot + esc(c) + '<span class="cat-n">' + n + '</span></button>';
  }).join('');

  $('brandCount').textContent = memos.length + ' 条';
  $('catList').innerHTML = Object.keys(cnt).map(c => '<option value="' + esc(c) + '">').join('');
}

function setCat(c) { activeCat = c; shown = PAGE; renderNav(); render(); }

function filtered() {
  const q = $('search').value.trim().toLowerCase();
  let list = memos.filter(m => activeCat === '全部' || (m.category || '未分类') === activeCat);
  if (q) list = list.filter(m =>
    m.title.toLowerCase().includes(q) || m.content.toLowerCase().includes(q) ||
    (m.tags || []).some(t => t.toLowerCase().includes(q)));
  const s = $('sortBy').value;
  list = [...list].sort((a, b) =>
    s === 'new' ? b.createdAt - a.createdAt :
    s === 'old' ? a.createdAt - b.createdAt :
    s === 'title' ? a.title.localeCompare(b.title, 'zh') :
    (b.favorite - a.favorite) || (b.createdAt - a.createdAt));
  return list;
}

function render() {
  const list = filtered();
  const total = memos.length;
  const q = $('search').value.trim();
  $('resultInfo').innerHTML = activeCat === '全部'
    ? '共 <b>' + total + '</b> 条' + (list.length !== total ? ' · 筛选出 <b>' + list.length + '</b> 条' : '')
    : '<b>' + esc(activeCat) + '</b> · <b>' + list.length + '</b> 条';

  const grid = $('grid');
  if (!list.length) {
    grid.innerHTML = '<div class="empty"><div class="empty-icon">📝</div>' +
      '<div class="empty-title">' + (q ? '没有匹配的备忘录' : '这个分类还是空的') + '</div>' +
      '<div class="empty-sub">' + (q ? '换个关键词试试' : '点右上角「＋ 添加」写下第一条') + '</div></div>';
    return;
  }
  let html = list.slice(0, shown).map(cardHTML).join('');
  if (list.length > shown) {
    html += '<div class="load-more"><button class="btn" onclick="more()">加载更多（还有 ' +
            (list.length - shown) + ' 条）</button></div>';
  }
  grid.innerHTML = html;
}
function more() { shown += PAGE; render(); }

function cardHTML(m) {
  const cat = m.category || '未分类';
  const c = catColor(cat);
  const date = new Date(m.createdAt).toLocaleDateString('zh-CN');
  const tags = (m.tags || []).slice(0, 3).map(t => '<span class="tag-chip">' + esc(t) + '</span>').join('');
  return '<div class="card">' +
    '<div class="card-top">' +
      '<h3 onclick="viewMemo(\'' + m.id + '\')">' + esc(m.title) + '</h3>' +
      '<button class="star' + (m.favorite ? ' on' : '') + '" onclick="toggleFav(\'' + m.id + '\')">' +
        (m.favorite ? '★' : '☆') + '</button>' +
    '</div>' +
    '<div class="card-body" onclick="viewMemo(\'' + m.id + '\')">' + esc(m.content) + '</div>' +
    '<div class="card-foot">' +
      '<span class="cat-tag" style="background:' + c + '14;color:' + c + '">' + esc(cat) + '</span>' +
      tags + '<span class="card-date">' + date + '</span>' +
    '</div>' +
    '<div class="card-actions">' +
      '<button class="btn" onclick="copyMemo(\'' + m.id + '\')">复制</button>' +
      '<button class="btn" onclick="editMemo(\'' + m.id + '\')">编辑</button>' +
      '<button class="btn" onclick="delMemo(\'' + m.id + '\')">删除</button>' +
    '</div></div>';
}

function openEditor() {
  if (!getToken()) { openTokenModal(); toast('请先配置写入令牌', true); return; }
  editingId = null;
  $('editTitle').textContent = '添加备忘录';
  ['f_title', 'f_category', 'f_tags', 'f_content'].forEach(i => $(i).value = '');
  $('editMask').classList.add('show');
  setTimeout(() => $('f_title').focus(), 60);
}
function editMemo(id) {
  if (!getToken()) { openTokenModal(); toast('请先配置写入令牌', true); return; }
  const m = memos.find(x => x.id === id); if (!m) return;
  editingId = id;
  $('editTitle').textContent = '编辑备忘录';
  $('f_title').value = m.title; $('f_category').value = m.category || '';
  $('f_tags').value = (m.tags || []).join(', '); $('f_content').value = m.content;
  $('viewMask').classList.remove('show');
  $('editMask').classList.add('show');
}
function editFromView() { editMemo(currentViewId); }
function closeEditor() { $('editMask').classList.remove('show'); }

async function saveMemo() {
  const title = $('f_title').value.trim(), content = $('f_content').value.trim();
  if (!title || !content) return toast('标题和内容必填', true);
  const btn = $('saveBtn'); btn.disabled = true; btn.textContent = '保存中…';
  try {
    const latest = await fetchLatest();
    const list = latest.data.memos || [];
    const now = Date.now();
    if (editingId) {
      const t = list.find(x => x.id === editingId);
      if (!t) throw new Error('原记录不存在，请刷新');
      t.title = title; t.content = content;
      t.category = $('f_category').value.trim();
      t.tags = parseTags($('f_tags').value); t.updatedAt = now;
    } else {
      list.unshift({
        id: 'm' + now.toString(36) + Math.random().toString(36).slice(2, 6),
        title: title, content: content,
        category: $('f_category').value.trim(),
        tags: parseTags($('f_tags').value),
        favorite: false, createdAt: now, updatedAt: now
      });
    }
    await putFile({ memos: list }, latest.sha, (editingId ? '编辑：' : '添加：') + title);
    memos = list; closeEditor(); renderNav(); render();
    toast('已保存并同步到 GitHub');
  } catch (e) { toast(e.message, true); }
  finally { btn.disabled = false; btn.textContent = '保存'; }
}

function viewMemo(id) {
  const m = memos.find(x => x.id === id); if (!m) return;
  currentViewId = id;
  $('v_title').textContent = m.title;
  $('v_star').textContent = m.favorite ? '★' : '☆';
  $('v_star').className = 'star' + (m.favorite ? ' on' : '');
  const cat = m.category || '未分类', c = catColor(cat);
  $('v_meta').innerHTML =
    '<span class="cat-tag" style="background:' + c + '14;color:' + c + '">' + esc(cat) + '</span>' +
    (m.tags || []).map(t => '<span class="tag-chip">' + esc(t) + '</span>').join('') +
    '<span class="hint">' + new Date(m.createdAt).toLocaleString('zh-CN') + '</span>';
  $('v_content').textContent = m.content;
  $('viewMask').classList.add('show');
}
function closeView() { $('viewMask').classList.remove('show'); }

async function toggleFav(id, fromView) {
  if (!getToken()) { openTokenModal(); toast('请先配置写入令牌', true); return; }
  const m = memos.find(x => x.id === id); if (!m) return;
  m.favorite = !m.favorite;
  try {
    const latest = await fetchLatest();
    const t = (latest.data.memos || []).find(x => x.id === id);
    if (t) t.favorite = m.favorite;
    await putFile(latest.data, latest.sha, (m.favorite ? '收藏：' : '取消收藏：') + m.title);
    if (fromView) {
      $('v_star').textContent = m.favorite ? '★' : '☆';
      $('v_star').className = 'star' + (m.favorite ? ' on' : '');
    }
    render();
  } catch (e) { m.favorite = !m.favorite; toast(e.message, true); }
}
function toggleFavView() { toggleFav(currentViewId, true); }

async function delMemo(id) {
  if (!getToken()) { openTokenModal(); toast('请先配置写入令牌', true); return; }
  const m = memos.find(x => x.id === id); if (!m) return;
  if (!confirm('确定删除「' + m.title + '」吗？此操作会同步到 GitHub。')) return;
  try {
    const latest = await fetchLatest();
    latest.data.memos = (latest.data.memos || []).filter(x => x.id !== id);
    await putFile(latest.data, latest.sha, '删除：' + m.title);
    memos = latest.data.memos; renderNav(); render(); toast('已删除');
  } catch (e) { toast(e.message, true); }
}

async function copyMemo(id) {
  const m = memos.find(x => x.id === id); if (!m) return;
  try { await navigator.clipboard.writeText(m.content); toast('已复制到剪贴板'); }
  catch (e) { toast('复制失败', true); }
}
function copyView() { copyMemo(currentViewId); }

function parseTags(v) { return v.split(/[,，]/).map(s => s.trim()).filter(Boolean); }
function esc(s) {
  return String(s == null ? '' : s).replace(/[&<>"']/g, m =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));
}
function toast(msg, isErr) {
  const t = $('toast'); t.textContent = msg;
  t.className = isErr ? 'err show' : 'show';
  clearTimeout(t._t); t._t = setTimeout(() => t.classList.remove('show'), 2400);
}

function openTokenModal() {
  $('tokenInput').value = getToken();
  $('tokenMask').classList.add('show');
  setTimeout(() => $('tokenInput').focus(), 60);
}
function closeTokenModal() { $('tokenMask').classList.remove('show'); }
function saveToken() {
  const v = $('tokenInput').value.trim();
  if (v) localStorage.setItem(TOKEN_KEY, v); else localStorage.removeItem(TOKEN_KEY);
  closeTokenModal(); toast(v ? '令牌已保存' : '令牌已清除');
}
function clearToken() { localStorage.removeItem(TOKEN_KEY); closeTokenModal(); toast('令牌已清除'); }

$('search').addEventListener('input', () => { shown = PAGE; render(); });
$('sortBy').addEventListener('change', () => { shown = PAGE; render(); });
$('btnSettings').addEventListener('click', openTokenModal);
$('btnAdd').addEventListener('click', openEditor);
[['tokenMask', closeTokenModal], ['editMask', closeEditor], ['viewMask', closeView]]
  .forEach(pair => $(pair[0]).addEventListener('click', e => { if (e.target.id === pair[0]) pair[1](); }));
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') { closeEditor(); closeView(); closeTokenModal(); }
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); $('search').focus(); }
  if (e.ctrlKey && e.key === 'Enter' && $('editMask').classList.contains('show')) saveMemo();
});

load();

/* ── 顶栏高度写入 --bar-h：让分类条 sticky 时正好贴在顶栏下沿 ── */
(function(){
  var tb = document.querySelector('.topbar');
  if (!tb) return;
  function fit(){ document.documentElement.style.setProperty('--bar-h', tb.offsetHeight + 'px'); }
  fit();
  window.addEventListener('resize', fit);
  window.addEventListener('load', fit);
  window.__MEMO_BARH = fit;
})();

</script></div>
