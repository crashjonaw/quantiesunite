@echo off
title Bloom Bar Public Server Launcher

echo =====================================
echo   Starting Bloom Bar Public Server
echo =====================================
echo.

REM Move to script directory
cd /d "%~dp0"

echo Installing Python packages if needed...
pip install -r requirements.txt
echo.

echo Configuring ngrok authtoken...
ngrok.exe config add-authtoken 3AvwkQkkLkHMSbwOITQbqnRtdcY_PrEEhBKZELM7qeVW2osC
echo.

echo -------------------------------------
echo Starting Flask server...
echo -------------------------------------
start cmd /k "cd /d %cd% && python app.py"

echo Waiting for Flask to boot...
timeout /t 5 >nul

echo -------------------------------------
echo Starting ngrok tunnel...
echo -------------------------------------
start cmd /k "cd /d %cd% && ngrok.exe http 5000"

echo.
echo =====================================
echo Two windows should now be open:
echo 1) Flask server
echo 2) ngrok tunnel
echo.
echo In the ngrok window look for:
echo Forwarding https://xxxxx.ngrok-free.app
echo =====================================
pause
