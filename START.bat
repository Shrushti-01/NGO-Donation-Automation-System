@echo off
title NGO Donation Chatbot - Starting...
color 0A

echo.
echo  ==========================================
echo   YUVA Rural Association - Donation Chatbot
echo  ==========================================
echo.

:: ── Check Node.js ──
node --version >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Node.js is not installed!
    echo.
    echo  Please install Node.js from https://nodejs.org
    echo  Download the LTS version and install it.
    echo.
    pause
    exit
)

:: ── Check Python ──
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python is not installed!
    echo.
    echo  Please install Python from https://python.org
    echo.
    pause
    exit
)

:: ── Install Node dependencies if not already installed ──
if not exist "whatsapp-service\node_modules" (
    echo  Installing WhatsApp service dependencies...
    echo  This only happens once, please wait...
    cd whatsapp-service
    npm install
    cd ..
    echo.
)

:: ── Install Python dependencies if needed ──
echo  Checking Python dependencies...
pip install -r requirements.txt -q
echo.

:: ── Start WhatsApp Service in a new window ──
echo  Starting WhatsApp Service...
start "WhatsApp Service" cmd /k "cd /d %~dp0whatsapp-service && node index.js"

:: ── Wait for WhatsApp service to initialize ──
echo  Waiting for WhatsApp service to start...
timeout /t 5 /nobreak >nul

:: ── Start Python Server in a new window ──
echo  Starting Python Server...
start "Python Server" cmd /k "cd /d %~dp0 && uvicorn app.main:app --host 0.0.0.0 --port 8000"

:: ── Wait for Python server to start ──
echo  Waiting for Python server to start...
timeout /t 4 /nobreak >nul

:: ── Open the website in browser ──
echo  Opening website in browser...
start "" "%~dp0frontend\index.html"

echo.
echo  ==========================================
echo   Everything is running!
echo  ==========================================
echo.
echo  IMPORTANT - First time only:
echo  Look at the "WhatsApp Service" window.
echo  If a QR code appears, scan it with your
echo  WhatsApp: Settings - Linked Devices - Link a Device
echo.
echo  After scanning once, you never need to scan again.
echo.
echo  To STOP everything, run STOP.bat
echo.
echo  You can minimize this window.
pause
