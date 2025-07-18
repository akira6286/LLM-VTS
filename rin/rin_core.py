# rin_core.py
import requests
import re
from config.config import (
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
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": QWEN_MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.3,
        "max_tokens": 256
    }

    try:
        response = requests.post(QWEN_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        if "choices" not in data:
            return "⚠️ 凜奈無法回覆：未取得有效回覆"
        raw_reply = data["choices"][0]["message"]["content"]
        return clean_qwen_response(raw_reply) if STRIP_THINK_BLOCK else raw_reply
    except Exception as e:
        return f"⚠️ 凜奈無法回覆：{e}"
