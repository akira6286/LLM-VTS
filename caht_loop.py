import openai

def chat_with_rin(user_input):
    messages = [
        {"role": "system", "content": "你是凜，一位人格被載入 AI 的虛擬室友..."},
        {"role": "user", "content": user_input}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 或使用 LM Studio 本地模型
        messages=messages
    )
    rin_reply = response['choices'][0]['message']['content']
    return rin_reply
