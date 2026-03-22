@echo off
title QuantiesUnite — Local Server
echo.
echo  ============================================
echo   QuantiesUnite Learning Platform
echo   Starting local server...
echo  ============================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo  ERROR: Python not found. Please install Python 3.9+ from https://python.org
    pause
    exit /b 1
)

:: Install dependencies if not already installed
echo  Checking dependencies...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo  Installing Flask and Waitress...
    pip install flask waitress
    echo.
)

:: Change to script directory
cd /d "%~dp0"

:: Start the server
echo  Server starting at: http://localhost:5001
echo  Press Ctrl+C to stop the server.
echo.
start "" http://localhost:5001
python app.py

pause
