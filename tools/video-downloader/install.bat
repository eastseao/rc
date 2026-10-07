@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo [1/2] 更新 yt-dlp...
pip install -U yt-dlp
echo [2/2] 检查 FFmpeg...
where ffmpeg >nul 2>nul && echo FFmpeg: 已安装 OK || echo FFmpeg: 未安装（MP4合并/MP3转换需要，可到 https://www.gyan.dev/ffmpeg/builds/ 下载后加入PATH）
echo.
echo 依赖就绪。双击 start.bat 启动服务。
pause
