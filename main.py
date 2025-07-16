import requests
import vts_websocket
from expression_manager import match_expression

#VTS動作呼叫
from vts_websocket import trigger_expression

def react_to_text(text):
    print("🗨️ 凜說：", text)
    expression_id = match_expression(text)
    if expression_id:
        trigger_expression(expression_id)
    else:
        print("🌀 凜沒有對應表情動作")

print("🧠 凜語句分析結果：", match_expression("我好生氣"))

#print("🧪 測試觸發 Anim Shake 表情")
#try:
#    trigger_expression("Anim Shake")  # ← 請確保完全符合 VTS 中的熱鍵名稱
#except Exception as e:
#    print("❗ 錯誤發生：", e)

#以下是文字回應
def chat_with_rin(user_input):
    url = "http://127.0.0.1:1234/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "model": "qwen3-14b ",  # ← 建議加上模型名稱（可視 LM Studio 顯示為主）
        "messages": [
            {"role": "system",
  "content": "你是凜奈，26歲，一位溫柔但可靠的人類女性室友，偶爾會出現慵懶的狀態。請直接回覆內容不輸出任何<think>區塊。請只使用自然、簡潔的繁體中文回話，每次回應限制為三句，不要模仿教學、格式、節目主持或資料庫樣式。請不要使用 HTML 標籤，也不要說自己是 AI 或模型。回話請保持生活化語氣、清楚、有邏輯，以日常口語陪伴使用者。"
},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.3,
        "max_tokens": 256,
        "stream": False
    }

#import re
#
#def clean_qwen_response(text):
    # 刪除 <think> 區塊，不影響主體回覆
#    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()



    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        rin_reply = response.json()['choices'][0]['message']['content']
        return rin_reply
    except Exception as e:
        return f"⚠️ 無法取得回覆：{e}"

while True:
    user_input = input("遙：")
    if user_input.strip().lower() in ["exit", "quit"]:
        break
    rin_reply = chat_with_rin(user_input)
    print("凜奈：", rin_reply)
#以上是文字回應
