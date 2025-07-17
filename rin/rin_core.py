# rin_core.py
import requests
import re
from config import (
    QWEN_API_URL,
    QWEN_MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
    SYSTEM_PROMPT,
    STRIP_THINK_BLOCK
)
from utils.text_cleaner import clean_qwen_response

# 🧠 呼叫凜（Qwen 回應）
def chat_with_rin(user_input):
    payload = {
        "model": QWEN_MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
        "stream": False
    }

    try:
        response = requests.post(QWEN_API_URL, headers={"Content-Type": "application/json"}, json=payload)
        response.raise_for_status()
        raw_reply = response.json()["choices"][0]["message"]["content"]
        print("🧪 [DEBUG] raw_reply:\n", raw_reply)
        # 改進的清理，忽略大小寫並處理多種情況
        clean_reply = re.sub(r'<think>[\s\S]*?</think>', '', raw_reply, flags=re.IGNORECASE)
        return clean_reply
    except Exception as e:
        return f"⚠️ 凜奈無法回覆：{e}"
