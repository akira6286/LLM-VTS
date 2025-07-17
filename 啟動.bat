@echo off
title 啟動凜的對話模組
echo 已載入模組：凜（main.py）
echo 正在啟動 main.py ...
echo 50%%...
echo 凜奈正在起床中...
echo ================================

REM 切換到 Python 程式所在資料夾（請根據實際路徑修改）
cd /d "%~dp0"

REM 啟動 main.py
python main.py

pause
