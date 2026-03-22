@echo off
title Bloom Burrow Launcher

echo =====================================
echo   Starting Bloom Burrow
echo =====================================
echo.

REM Move to script directory
cd /d "%~dp0"

REM Fix cloudflared config to use 127.0.0.1 (not localhost which can resolve to IPv6)
echo Patching cloudflared config...
powershell -Command "(Get-Content '$env:USERPROFILE\.cloudflared\config.yml') -replace 'localhost:5000','127.0.0.1:5000' | Set-Content '$env:USERPROFILE\.cloudflared\config.yml'" >nul 2>&1

REM Kill ALL cloudflared and Flask processes + their CMD windows
echo Cleaning up old processes...
taskkill /F /IM cloudflared.exe >nul 2>&1
taskkill /F /FI "WINDOWTITLE eq Cloudflare Tunnel" >nul 2>&1
taskkill /F /FI "WINDOWTITLE eq Flask - Bloom Burrow" >nul 2>&1
wmic process where "name='cloudflared.exe'" delete >nul 2>&1
timeout /t 3 >nul

REM Confirm cloudflared is fully gone
taskkill /F /IM cloudflared.exe >nul 2>&1
timeout /t 2 >nul

echo Installing Python packages if needed...
pip install -r requirements.txt -q
pip install waitress -q
echo.

echo Starting Flask server...
start "Flask - Bloom Burrow" /D "%~dp0" cmd /k "waitress-serve --host=127.0.0.1 --port=5000 --threads=8 app:app"

echo Waiting for Flask to start...
timeout /t 5 >nul

echo Starting Cloudflare Tunnel...
start "Cloudflare Tunnel" cmd /k "cloudflared tunnel run --url http://127.0.0.1:5000 bloomburrow"

echo.
echo =====================================
echo Bloom Burrow is now running.
echo Local:   http://localhost:5000
echo Public:  https://bloomburrow.sg
echo =====================================
pause
