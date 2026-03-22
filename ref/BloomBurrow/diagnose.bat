@echo off
echo ================================================
echo   Bloom Bar - Diagnostics
echo ================================================
echo.

echo [1] Checking Python...
python --version
if errorlevel 1 (echo FAIL: Python not found) else (echo OK)

echo.
echo [2] Checking pip...
pip --version
if errorlevel 1 (echo FAIL: pip not found) else (echo OK)

echo.
echo [3] Checking ngrok...
where ngrok
if errorlevel 1 (
    if exist "%~dp0ngrok.exe" (
        echo OK: ngrok.exe found in this folder
    ) else (
        echo FAIL: ngrok.exe not found
    )
) else (echo OK)

echo.
echo [4] Checking Flask install...
python -c "import flask; print('Flask', flask.__version__)"
if errorlevel 1 (echo FAIL: Flask not installed) else (echo OK)

echo.
echo [5] Checking project files...
if exist "%~dp0app.py" (echo OK: app.py found) else (echo FAIL: app.py missing)
if exist "%~dp0.env" (echo OK: .env found) else (echo WARN: .env missing)

echo.
echo ================================================
echo   Done. Screenshot this window and share it.
echo ================================================
pause
