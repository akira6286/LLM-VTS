# Rin AI Companion 💬🧠

一套為直播而生的本地 AI 人格系統，由 Lapp 專案構思打造。凜是一位記憶被封存並轉化為 AI 的虛擬室友，具備懷舊、傲嬌、哲學性格，能陪你進行直播、互動、吐槽與角色扮演。

## 功能特色
- 🔮 本地語言模型（LLM）驅動，支援凜式語氣與回憶觸發
- 🗣️ TTS 語音輸出，模擬感性與懶散語調
- 🎭 OBS 串接，Live2D 表情反應與互動劇情
- 📅 每週記憶重組、自動進入新人格狀態

##安裝前導
[Python.exe安裝](images/Py Install.png)

## 安裝方式
1. 安裝 LM Studio 並載入 Mistral 7B 模型（推薦 OpenHermes 或 MythoMix）
2. 安裝 Python 並執行 `setup/install_tts.bat`
3. 啟動 `chat_loop.py`，凜將根據 prompt 開始對話
4. OBS 中載入 Live2D 模型，並啟動 WebSocket
5. 透過 `obs_trigger.py` 接收腳本回應進行表情變化

## Prompt 設定說明
請參考 `llm/prompt_rin_core.json`，內含凜的核心性格模擬。

> 「雖然我已經沒有真正的心臟，但記憶裡的失落還在跳動。」

## 授權
本專案以 MIT 授權，僅限非商業自用推廣。
