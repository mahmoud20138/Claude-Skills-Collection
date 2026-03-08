@echo off
title Trading Command Center - Live Dashboard
echo.
echo  ======================================================
echo   TRADING COMMAND CENTER - Starting...
echo  ======================================================
echo.
echo   This will:
echo     1. Start the HTTP server on port 8888
echo     2. Connect to MT5 for live data
echo     3. Open the dashboard in your browser
echo.
echo   Dashboard URL: http://localhost:8888
echo   Press Ctrl+C to stop.
echo.
echo  ======================================================
echo.

cd /d "%~dp0"
python data_bridge.py

pause
