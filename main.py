from rin.rin_core import chat_with_rin
from emotion.emo_eng import react_to_text

while True:
    user_input = input("我：")
    if user_input.strip().lower() in ["exit", "quit"]:
        break

    rin_reply = chat_with_rin(user_input)
    clean_response = rin_reply.replace("<think>", "").replace("</think>", "")

    print("凜奈：", clean_response)
    #print("🧪 [DEBUG] full_response:\n", rin_reply)  # debug 印原始回覆

    react_to_text(clean_response)
