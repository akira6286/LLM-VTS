# config.py
import json

with open("config/settings.json", "r", encoding="utf-8") as f:
    settings = json.load(f)

# 🧠 Qwen 模型設定
QWEN_API_URL = settings["qwen"]["api_url"]
QWEN_MODEL_NAME = "qwen3-14b"

# 🔧 回應行為
TEMPERATURE = 0.3
MAX_TOKENS = 256
STRIP_THINK_BLOCK = True  # 是否清除 <think> 區塊

# 🗣️ TTS 設定（如果有串接）
TTS_ENABLED = False
TTS_VOICE = "zh-TW-HsiaoYuNeural"
TTS_STYLE = "chat"
TTS_DEBUG = False

# 🎭 VTS 表情設定
VTS_ENABLED = True
VTS_DEBUG = False

# 👤 凜的人設 prompt
SYSTEM_PROMPT = (
    "你是凜奈，26歲，因事故身亡的人類女性，記憶被保留下來的女性AI室友，具備懷舊、傲嬌、哲學性格。"
    "請用自然、簡潔的繁體中文回話，每次回應最多三句。"
    "不要模仿資料庫或節目風格，不使用 <think> 區塊、不使用 HTML 標籤，也不說自己是 AI。"
    "請保持生活化語氣，以日常口語陪伴使用者。"
)
