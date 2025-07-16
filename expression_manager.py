# expression_manager.py

expression_map = {
    "Angry Sign": ["生氣","火大","不爽", "氣死人了","氣死我了","好生氣"],
    "Heart Eyes": ["愛心眼"],
    "Anim Shake": ["搖晃"],
    "Shock Sign": ["驚訝"],
    "Eyes Cry": ["哭哭"],
    "": []
}

def match_expression(text):
    for emotion, keywords in expression_map.items():  # ✅ 改成 expression_map
        if any(word in text for word in keywords):
            return emotion
    return None
