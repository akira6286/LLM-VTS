# rin_core.py

import requests
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
        "model": qwen3_14B,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
        "stream": False
    }

    raw_reply = response.json()["choices"][0]["message"]["content"]

    # 🧪 【DEBUG】印出原始回覆，確認 <think> 標籤樣貌
    print("🧪 [DEBUG] raw_reply:\n", raw_reply)

    # 接著再做清理
    return clean_qwen_response(raw_reply) if STRIP_THINK_BLOCK else raw_reply

    try:
        response = requests.post(QWEN_API_URL, headers={"Content-Type": "application/json"}, json=payload)
        response.raise_for_status()
        raw_reply = response.json()["choices"][0]["message"]["content"]
        return clean_qwen_response(raw_reply) if STRIP_THINK_BLOCK else raw_reply
    except Exception as e:
        return f"⚠️ 凜無法回覆：{e}"
