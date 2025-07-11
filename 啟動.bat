@echo off
title 啟動凜的對話模組
echo 正在啟動 chat_loop.py ...
echo 凜正在起床中...
echo ================================

REM 切換到 Python 程式所在資料夾（請根據實際路徑修改）
cd /d "D:\MyProjects\LLM-VTS-main"

REM 啟動 chat_loop.py
python chat_loop.py

pause