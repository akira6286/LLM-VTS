# utils/text_cleaner.py

import re

# 🧹 清除 <think> 區塊，保留主體回覆

def clean_qwen_response(text):
    """
    移除所有 <think …>…</think> 區塊（含屬性、大小寫、跨行）
    """
    pattern = re.compile(r"<think[^>]*>[\s\S]*?</think>", re.IGNORECASE)
    return pattern.sub("", text).strip()

# 🧪 進階用法：分離主文與思考段
def split_qwen_sections(text):
    """
    拆分 Qwen 回覆為主文與 <think> 內容。
    回傳值：(main_text, think_content)
    """
    think_block = re.findall(r"<think>(.*?)</think>", text, flags=re.DOTALL)
    main_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    return main_text, think_block[0] if think_block else None
