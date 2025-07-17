from llm_core import chat_with_rin
from emotion_engine import react_to_text
from config import QWEN_MODEL_NAME, SYSTEM_PROMPT, STRIP_THINK_BLOCK
import re


while True:
    user_input = input("我：")
    if user_input.strip().lower() in ["exit", "quit"]:
        break
    rin_reply = chat_with_rin(user_input)
    clean_response = response.replace("<think>", "").replace("</think>", "")
    print("凜奈：", rin_reply)
    print("🧪 [DEBUG] full_response:\n", response.json())
    react_to_text(rin_reply)
