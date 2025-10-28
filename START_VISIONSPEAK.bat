@echo off
title VisionSpeak - Starting All Services
color 0A

echo ==========================================
echo    VISIONSPEAK - Smart Glasses Platform
echo ==========================================
echo.

:: Check if virtual environment exists
if not exist "visionspeak_env\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run SETUP_VISIONSPEAK.bat first.
    pause
    exit /b 1
)

:: Activate virtual environment
echo [1/3] Activating virtual environment...
call visionspeak_env\Scripts\activate.bat

:: Check if database exists, create if not
if not exist "vision_logs.db" (
    echo [2/3] Creating database...
    python db_setup.py
) else (
    echo [2/3] Database already exists, skipping...
)

:: Start Flask backend
echo [3/3] Starting Flask backend server...
echo.
echo ==========================================
echo   Backend running on http://localhost:5000
echo   Open visionspeak.html in your browser
echo   Press Ctrl+C to stop the server
echo ==========================================
echo.

python app.py

pause

