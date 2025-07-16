# Rinna AI Companion 💬🧠

一套為直播而生的本地 AI 人格系統，由 木村遙 專案構思打造。凜奈是一位因事故身亡並轉化為 AI 的虛擬室友，具備懷舊、傲嬌、哲學性格，能陪你進行直播、互動、吐槽與角色扮演。

## 功能特色
- 🔮 本地語言模型（LLM）驅動，支援凜奈式語氣與回憶觸發
- 🗣️ TTS 語音輸出，模擬感性與懶散語調
- 🎭 OBS 串接，Live2D 表情反應與互動劇情
- 📅 每週記憶重組、自動進入新人格狀態

## 建議配備
- 需要 64 位元的處理器及作業系統
- 處理器: i7-11代以上(AMD用戶請自行斟酌)
- 記憶體: 32 GB 記憶體
- 顯示卡: geforce RTX 2070

## 需要下載的檔案
- [LM Studio](https://installers.lmstudio.ai/win32/x64/0.3.18-3/LM-Studio-0.3.18-3-x64.exe)
- [Python官方網站](https://www.python.org/downloads/)

## 環境安裝
- 建議安裝Python3.13.5以上的版本。記得勾選"Add python.exe to PATH


![Py 安裝畫面](https://raw.githubusercontent.com/akira6286/LLM-VTS/main/images/Py_Install.png)
## LM Studio
- 左下角切換到Developer
- 左方放大鏡符號搜尋qwen3-14b並下載
- 在左側開發者頁面中於上方"選擇要載入的模型"
- 並在左上角將Status狀態變為Running
  
## 安裝方式
1. 安裝 LM Studio 並載入 qwen3-14b 模型（推薦 OpenHermes 或 MythoMix）
2. 安裝 Python 並執行 `setup/install_tts.bat`
3. 啟動 `chat_loop.py`，凜將根據 prompt 開始對話
4. OBS 中載入 Live2D 模型，並啟動 WebSocket
5. 透過 `obs_trigger.py` 接收腳本回應進行表情變化

## Prompt 設定說明 (暫時沒用，目前都在Main.py中)
請參考 `llm/prompt_rin_core.json`，內含凜的核心性格模擬。

> 「雖然我已經沒有真正的心臟，但記憶裡的失落還在跳動。」

## 授權
本專案以 MIT 授權，僅限非商業自用推廣。
