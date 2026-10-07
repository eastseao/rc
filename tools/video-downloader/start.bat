@echo off
chcp 65001 >nul
cd /d "%~dp0"
title LinkGrab 本地视频下载器
echo ============================================
echo   LinkGrab 本地视频下载器
echo   启动中... 启动完成后浏览器访问 http://127.0.0.1:8765
echo ============================================
python server.py
pause
