# emotion_engine.py

from vts_websocket import trigger_expression
from expression_manager import match_expression

# 🎭 分析回覆並執行表情動作
def react_to_text(text, debug=False):
    if debug:
        print("🧠 凜語句分析中：", text)
    expression_id = match_expression(text)
    if expression_id:
        trigger_expression(expression_id)
        if debug:
            print(f"🎭 已觸發表情：{expression_id}")
    else:
        if debug:
            print("🌀 沒有找到對應表情")
