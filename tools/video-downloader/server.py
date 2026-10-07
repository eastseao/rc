#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkGrab —— 本地视频下载器（嵌入式引擎版 V0.1.1）
粘贴一个链接 → 自动解析 → 选择清晰度 → 默认下载 MP4

架构：Python 标准库 HTTP 服务器 + yt-dlp（Python API 解析/下载）+ FFmpeg（合并/转码）
- 电脑端：pip install yt-dlp 后直接 python server.py
- 安卓端：由 Chaquopy 内嵌 Python 运行时导入本模块，configure() + start() 启动
"""
import json
import re
import shutil
import socket
import sys
import threading
import time
import urllib.parse
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    yt_dlp = None

BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = BASE_DIR / "downloads"
COOKIES_FILE = BASE_DIR / "cookies.txt"
INDEX_FILE = BASE_DIR / "index.html"

FFMPEG_LOCATION = None            # 安卓端由 configure() 指向内置 ffmpeg 目录
PORT = 8765

TIERS = [
    ("best",  "最高画质", None),
    ("2160",  "4K",       2160),
    ("1440",  "2K",       1440),
    ("1080",  "1080P",    1080),
    ("720",   "720P",     720),
    ("480",   "480P",     480),
    ("360",   "360P",     360),
]
FORMATS = ["mp4", "mp3", "m4a"]


# ---------------------------------------------------------------------------
# 配置（安卓端嵌入时调用）
# ---------------------------------------------------------------------------
def configure(download_dir=None, ffmpeg_location=None, cookies_file=None, port=8765):
    """安卓端启动前调用：覆盖下载目录、ffmpeg 路径、Cookie、端口。"""
    global DOWNLOAD_DIR, FFMPEG_LOCATION, COOKIES_FILE, PORT
    if download_dir:
        DOWNLOAD_DIR = Path(download_dir)
    if ffmpeg_location:
        FFMPEG_LOCATION = str(ffmpeg_location)
    if cookies_file:
        COOKIES_FILE = Path(cookies_file)
    PORT = port
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


def _has_ffmpeg():
    if FFMPEG_LOCATION:
        d = Path(FFMPEG_LOCATION)
        return (d / "ffmpeg").is_file() or (d / "ffmpeg.exe").is_file()
    return bool(shutil.which("ffmpeg"))


def _ffmpeg_opts():
    if FFMPEG_LOCATION:
        return {"ffmpeg_location": FFMPEG_LOCATION}
    return {}


def base_opts():
    opts = {
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "retries": 3,
        "socket_timeout": 30,
    }
    opts.update(_ffmpeg_opts())
    if COOKIES_FILE.exists():
        opts["cookiefile"] = str(COOKIES_FILE)
    return opts


# ---------------------------------------------------------------------------
# 解析
# ---------------------------------------------------------------------------
def parse_info(url):
    if yt_dlp is None:
        raise RuntimeError("未找到 yt-dlp 库，请先安装：pip install -U yt-dlp")
    with yt_dlp.YoutubeDL(base_opts()) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except yt_dlp.utils.DownloadError as e:
            raise RuntimeError(str(e).strip().splitlines()[-1][:500] or "解析失败，请检查链接是否有效")
    if info and info.get("entries") and "url" not in info:   # 极少数播放列表兜底
        info = info["entries"][0]

    heights, has_video, has_audio_only = set(), False, False
    for f in (info.get("formats") or []):
        vcodec = f.get("vcodec") or "none"
        acodec = f.get("acodec") or "none"
        if vcodec != "none":
            has_video = True
            if f.get("height"):
                heights.add(int(f["height"]))
        if acodec != "none" and vcodec == "none":
            has_audio_only = True
    max_h = max(heights) if heights else 0

    tiers = []
    if has_video:
        tiers.append({"key": "best", "label": "最高画质"})
        for key, label, th in TIERS[1:]:
            if max_h >= th:
                tiers.append({"key": key, "label": label})
        if len(tiers) == 1:
            tiers.append({"key": "360", "label": "360P"})
    if has_audio_only or max_h == 0:
        tiers.append({"key": "audio", "label": "仅音频"})

    duration = info.get("duration")
    thumb = info.get("thumbnail") or ""
    if not thumb and info.get("thumbnails"):
        thumb = info["thumbnails"][-1].get("url", "") or ""
    return {
        "title": info.get("title") or "未命名视频",
        "thumbnail": thumb,
        "duration": round(duration, 1) if isinstance(duration, (int, float)) else None,
        "uploader": info.get("uploader") or info.get("channel") or info.get("creator") or "",
        "webpage_url": info.get("webpage_url") or url,
        "extractor": (info.get("extractor") or "unknown").replace("_", " "),
        "max_height": max_h,
        "tiers": tiers,
        "ffmpeg": _has_ffmpeg(),
    }


def build_selector(tier, fmt):
    if fmt in ("mp3", "m4a") or tier == "audio":
        return "bestaudio/best"
    if tier == "best":
        return "bv*+ba/b"
    h = int(tier)
    if _has_ffmpeg():
        return f"bestvideo[height<={h}]+bestaudio/best[height<={h}]/best"
    return f"best[height<={h}][ext=mp4]/best[height<={h}]/best"


# ---------------------------------------------------------------------------
# 下载任务
# ---------------------------------------------------------------------------
TASKS = {}
TASKS_LOCK = threading.Lock()


def _make_progress_hook(task):
    def hook(d):
        try:
            if d.get("status") == "downloading":
                total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
                done = d.get("downloaded_bytes") or 0
                pct = (done / total * 100) if total else 0
                task["percent"] = round(pct, 1)
                task["stage"] = "下载中 %.1f%%" % pct
            elif d.get("status") == "finished":
                task["percent"] = 100
                task["stage"] = "已下载，处理中…"
        except Exception:
            pass
    return hook


def _make_pp_hook(task):
    def hook(d):
        if d.get("status") == "started":
            task["stage"] = "正在%s…" % d.get("postprocessor", "后处理")
    return hook


def new_task(url, tier, fmt):
    task_id = uuid.uuid4().hex[:10]
    task = {
        "id": task_id, "url": url, "tier": tier, "format": fmt,
        "status": "queued", "percent": 0, "stage": "排队中…",
        "filename": None, "error": None, "created": time.time(),
    }
    with TASKS_LOCK:
        cutoff = time.time() - 3600
        stale = [k for k, t in TASKS.items() if t["status"] in ("done", "error") and t["created"] < cutoff]
        for k in stale:
            TASKS.pop(k, None)
        TASKS[task_id] = task
    threading.Thread(target=download_worker, args=(task,), daemon=True).start()
    return task


def download_worker(task):
    if yt_dlp is None:
        task["status"], task["error"] = "error", "未找到 yt-dlp 库"
        return
    opts = base_opts()
    opts.update({
        "format": build_selector(task["tier"], task["format"]),
        "outtmpl": str(DOWNLOAD_DIR / "%(title)s [%(id)s].%(ext)s"),
        "progress_hooks": [_make_progress_hook(task)],
        "postprocessor_hooks": [_make_pp_hook(task)],
    })
    if task["format"] == "mp4" and _has_ffmpeg():
        opts["merge_output_format"] = "mp4"
    elif task["format"] in ("mp3", "m4a") and _has_ffmpeg():
        opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": task["format"],
            "preferredquality": "192",
        }]
    try:
        task["status"] = "running"
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([task["url"]])
        task["status"] = "done"
        task["percent"] = 100
        task["stage"] = "下载完成"
        task["filename"] = guess_latest_file(task["created"])
    except Exception as e:
        task["status"] = "error"
        task["error"] = str(e).strip().splitlines()[-1][:400]


def guess_latest_file(after_ts):
    try:
        candidates = [p for p in DOWNLOAD_DIR.iterdir() if p.is_file() and p.suffix.lower() in
                      (".mp4", ".m4a", ".mp3", ".webm", ".mkv", ".mov", ".flv", ".opus", ".aac", ".wav")]
        recent = [p for p in candidates if p.stat().st_mtime >= after_ts - 10]
        pool = recent or candidates
        if pool:
            return sorted(pool, key=lambda p: p.stat().st_mtime, reverse=True)[0].name
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# HTTP 服务
# ---------------------------------------------------------------------------
class Handler(BaseHTTPRequestHandler):
    server_version = "LinkGrab/1.0"

    def log_message(self, fmt, *args):
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))

    def _send_json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            return json.loads(raw.decode("utf-8"))
        except Exception:
            raise ValueError("请求体不是有效的 JSON")

    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        try:
            if path in ("/", "/index.html"):
                body = INDEX_FILE.read_bytes() if INDEX_FILE.is_file() else b"index.html missing"
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            elif path == "/api/files":
                self._api_files()
            elif path == "/api/tasks":
                with TASKS_LOCK:
                    tasks = [t for t in TASKS.values() if t["status"] in ("queued", "running", "done")][-20:]
                self._send_json({"tasks": tasks})
            elif path.startswith("/files/"):
                self._api_file_download(urllib.parse.unquote(path[len("/files/"):]))
            else:
                self._send_json({"error": "接口不存在"}, 404)
        except Exception as e:
            self._send_json({"error": str(e)[:400]}, 500)

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        try:
            if path == "/api/info":
                self._api_info()
            elif path == "/api/download":
                self._api_download()
            elif path == "/api/progress":
                self._api_progress()
            else:
                self._send_json({"error": "接口不存在"}, 404)
        except ValueError as e:
            self._send_json({"error": str(e)}, 400)
        except Exception as e:
            self._send_json({"error": str(e)[:400]}, 500)

    def _api_info(self):
        data = self._read_json()
        url = (data.get("url") or "").strip()
        if not url:
            self._send_json({"error": "请输入链接"}, 400)
            return
        if not re.match(r"^https?://", url):
            url = "https://" + url
        self._send_json({"ok": True, "info": parse_info(url)})

    def _api_download(self):
        data = self._read_json()
        url = (data.get("url") or "").strip()
        tier = data.get("tier") or "best"
        fmt = (data.get("format") or "mp4").lower()
        if not url:
            self._send_json({"error": "请输入链接"}, 400)
            return
        if fmt not in FORMATS:
            self._send_json({"error": "不支持的格式：%s" % fmt}, 400)
            return
        if fmt in ("mp3", "m4a") and tier != "audio":
            tier = "audio"
        valid_tiers = {t[0] for t in TIERS} | {"audio"}
        if tier not in valid_tiers:
            tier = "best"
        if not _has_ffmpeg() and fmt == "mp3":
            self._send_json({"error": "未检测到 FFmpeg，无法转换 MP3"}, 400)
            return
        task = new_task(url, tier, fmt)
        self._send_json({"ok": True, "task": task})

    def _api_progress(self):
        data = self._read_json()
        task_id = data.get("id") or ""
        with TASKS_LOCK:
            task = TASKS.get(task_id)
        if not task:
            self._send_json({"error": "任务不存在"}, 404)
            return
        self._send_json({"ok": True, "task": task})

    def _api_files(self):
        files = []
        for p in sorted(DOWNLOAD_DIR.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
            if p.is_file() and p.suffix.lower() in (".mp4", ".m4a", ".mp3", ".webm", ".mkv", ".mov", ".flv", ".opus", ".aac", ".wav"):
                st = p.stat()
                files.append({"name": p.name, "size": st.st_size, "mtime": st.st_mtime,
                              "url": "/files/" + urllib.parse.quote(p.name)})
        self._send_json({"files": files})

    def _api_file_download(self, raw_name):
        name = Path(raw_name).name
        p = DOWNLOAD_DIR / name
        if not p.is_file():
            self._send_json({"error": "文件不存在"}, 404)
            return
        size = p.stat().st_size
        disp = "attachment; filename*=UTF-8''" + urllib.parse.quote(name)
        self.send_response(200)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("Content-Disposition", disp)
        self.send_header("Content-Length", str(size))
        self.end_headers()
        with open(p, "rb") as f:
            shutil.copyfileobj(f, self.wfile)


# ---------------------------------------------------------------------------
def start(port=8765):
    """启动 HTTP 服务（阻塞）。安卓端在子线程中调用。"""
    global PORT
    PORT = port
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print("LinkGrab server on http://127.0.0.1:%d, downloads: %s" % (PORT, DOWNLOAD_DIR))
    server.serve_forever()


def local_ip():
    try:
        ips = socket.gethostbyname_ex(socket.gethostname())[2]
        for ip in ips:
            if ip.startswith("192.168.") or ip.startswith("10."):
                return ip
        if ips:
            return ips[0]
    except Exception:
        pass
    return "127.0.0.1"


def main():
    if yt_dlp is None:
        print("✗ 未找到 yt-dlp 库，请先运行：pip install -U yt-dlp")
        input("按回车退出…")
        sys.exit(1)
    print("=" * 56)
    print("  LinkGrab · 本地视频下载器 V0.1.1")
    print("  本机访问   : http://127.0.0.1:%d" % PORT)
    ip = local_ip()
    if ip != "127.0.0.1":
        print("  局域网访问 : http://%s:%d" % (ip, PORT))
    print("  下载目录   : %s" % DOWNLOAD_DIR)
    print("  FFmpeg     : %s" % ("已检测到 ✓" if _has_ffmpeg() else "未检测到（仅直链格式）"))
    print("  按 Ctrl+C 停止服务")
    print("=" * 56)
    try:
        start(PORT)
    except KeyboardInterrupt:
        print("\n已停止。")

if __name__ == "__main__":
    main()
