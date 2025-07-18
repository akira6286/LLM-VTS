@echo off
title Starting Rinna's language module
echo Module loaded：Rinna（main.py）
echo Starting main.py ...
echo 50%%...
echo Rinna waking up
echo ================================

REM 切換到 Python 程式所在資料夾（請根據實際路徑修改）
cd /d "%~dp0"

REM 啟動 main.py
python main.py

pause
